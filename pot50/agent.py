"""One run of the pot50 loop. Invoked by GitHub Actions twice a day."""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from . import config as C, ledger as L, gumroad, approvals, prompts

MEMORY = Path("memory.md")
LOG = Path("decisions.log")
DRY = os.environ.get("DRY_RUN", "false").lower() == "true"


def log(msg):
    line = f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def reconcile_sales(ledger):
    try:
        seen = set(ledger.setdefault("reconciled_sale_ids", []))
        new = 0
        for s in gumroad.sales():
            if s["id"] in seen or s.get("refunded"):
                continue
            net = gumroad.net_eur(s)
            L.add(ledger, "revenue", net, f"Gumroad sale: {s.get('product_name')} ({s.get('price')} cents gross)", s["id"])
            ledger["reconciled_sale_ids"].append(s["id"])
            new += 1
        if new:
            log(f"reconciled {new} new sale(s)")
    except Exception as e:
        log(f"WARN gumroad reconcile failed: {e}")


def apply_verdicts(ledger):
    try:
        for issue, verdict in approvals.resolve():
            L.add(ledger, "info", 0, f"approval #{issue['number']} {verdict}: {issue['title']}")
            log(f"approval #{issue['number']} {verdict}")
    except Exception as e:
        log(f"WARN approvals failed: {e}")


def tree(root):
    p = Path(root)
    return [str(x) for x in p.rglob("*") if x.is_file()] if p.exists() else []


def build_context(ledger):
    s = L.summary(ledger)
    try:
        pend = [f"#{i['number']} {i['title']}" for i in approvals.pending()]
    except Exception:
        pend = ["(unavailable)"]
    recent = ledger["entries"][-15:]
    return (
        f"LEDGER SUMMARY\n{json.dumps(s, indent=1)}\n\n"
        f"RECENT LEDGER ENTRIES\n{json.dumps(recent, indent=1)}\n\n"
        f"PENDING APPROVALS\n" + ("\n".join(pend) or "none") + "\n\n"
        f"FILES\ndrafts: {tree('drafts')}\nproducts: {tree('products')}\n\n"
        f"MEMORY.MD\n{MEMORY.read_text() if MEMORY.exists() else '(empty)'}\n\n"
        "Decide and act."
    )


def token_cost_eur(usage):
    usd = (usage.input_tokens * C.PRICE_INPUT_PER_M_USD + usage.output_tokens * C.PRICE_OUTPUT_PER_M_USD) / 1e6
    return usd * C.USD_TO_EUR


def run_model(ledger):
    import anthropic
    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": build_context(ledger)}]
    total_cost = 0.0
    approval_opened = False
    for _ in range(8):  # hard cap on tool turns per run
        resp = client.messages.create(model=C.MODEL, max_tokens=C.MAX_TOKENS, system=prompts.SYSTEM,
                                      tools=prompts.TOOLS, messages=messages)
        total_cost += token_cost_eur(resp.usage)
        messages.append({"role": "assistant", "content": resp.content})
        results, done = [], False
        for block in resp.content:
            if block.type != "tool_use":
                continue
            name, inp = block.name, block.input
            out = "ok"
            if name == "write_file":
                p = Path(inp["path"])
                if p.parts[0] not in ("drafts", "products") or ".." in p.parts:
                    out = "refused: path must be under drafts/ or products/"
                else:
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(inp["content"])
                    log(f"wrote {p}")
            elif name == "request_approval":
                kind = inp["kind"]
                if approval_opened:
                    out = "refused: one approval per run"
                elif kind == "spend" and not L.can_spend(ledger, float(inp.get("amount_eur", 0))):
                    out = "refused: exceeds spend cap"
                else:
                    n = approvals.open_request(kind, inp["title"], inp["body"])
                    approval_opened = True
                    out = f"opened issue #{n}"
                    log(f"approval requested #{n} [{kind}] {inp['title']}")
            elif name == "update_memory":
                MEMORY.write_text(inp["content"])
            elif name == "finish":
                log(f"finish: {inp['summary']}")
                done = True
            results.append({"type": "tool_result", "tool_use_id": block.id, "content": out})
        if done or not results:
            break
        messages.append({"role": "user", "content": results})
    return total_cost


def main():
    ledger = L.load()
    if ledger.get("status") == "dead":
        log("agent is dead; exiting")
        return 0
    if not ledger["entries"]:
        L.add(ledger, "info", 0, f"seeded with {C.SEED_EUR} {C.CURRENCY}")
    reconcile_sales(ledger)
    apply_verdicts(ledger)
    reason = L.check_kill(ledger)
    if reason:
        ledger["status"] = "dead"
        L.add(ledger, "info", 0, f"KILL: {reason}")
        L.save(ledger)
        log(f"KILL: {reason}")
        return 0
    if DRY:
        L.add(ledger, "info", 0, "dry run, no model call")
        L.save(ledger)
        log(f"dry run ok: {L.summary(ledger)}")
        return 0
    cost = run_model(ledger)
    L.add(ledger, "spend", cost, "compute (tokens)")
    L.save(ledger)
    log(f"run cost {cost:.4f} EUR; {L.summary(ledger)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
