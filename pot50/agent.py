"""One run of the pot50 loop. No human in the loop."""
import json
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

from . import config as C, ledger as L, stripe_client as S, devto, prompts

MEMORY, LOG, STATE = Path("memory.md"), Path("decisions.log"), Path("state.json")
DRY = os.environ.get("DRY_RUN", "false").lower() == "true"
ALLOWED_ROOTS = ("docs", "products", "drafts")


def now():
    return datetime.now(timezone.utc)


def log(msg):
    line = f"{now().isoformat(timespec='seconds')} {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def load_state():
    return json.loads(STATE.read_text()) if STATE.exists() else {"products": [], "articles": []}


def reconcile(ledger):
    try:
        seen = set(ledger.setdefault("reconciled_ids", []))
        n = 0
        for ch in S.succeeded_charges():
            if ch["id"] in seen:
                continue
            L.add(ledger, "revenue", S.net_eur(ch), f"Stripe charge {ch['amount']/100:.2f} {ch['currency']}", ch["id"])
            ledger["reconciled_ids"].append(ch["id"])
            n += 1
        if n:
            log(f"reconciled {n} new payment(s)")
    except Exception as e:
        log(f"WARN stripe reconcile failed: {e}")


def tree(root):
    p = Path(root)
    return sorted(str(x) for x in p.rglob("*") if x.is_file()) if p.exists() else []


def context(ledger, state):
    s = L.summary(ledger)
    return (f"LEDGER\n{json.dumps(s)}\n\nRECENT ENTRIES\n{json.dumps(ledger['entries'][-12:])}\n\n"
            f"LIVE PRODUCTS\n{json.dumps(state['products'], indent=1)}\n\n"
            f"ARTICLES\n{json.dumps(state['articles'][-10:], indent=1)}\n\n"
            f"FILES\n{json.dumps({r: tree(r) for r in ALLOWED_ROOTS})}\n\n"
            f"DEVTO ENABLED: {devto.enabled()}\n\nMEMORY.MD\n{MEMORY.read_text() if MEMORY.exists() else '(empty)'}\n\nDecide and act.")


def cost_eur(u):
    return (u.input_tokens * C.PRICE_INPUT_PER_M_USD + u.output_tokens * C.PRICE_OUTPUT_PER_M_USD) / 1e6 * C.USD_TO_EUR


def recent(items, key, days):
    cutoff = now() - timedelta(days=days)
    return [i for i in items if datetime.fromisoformat(i[key]) > cutoff]


PROTECTED = {"docs/index.md", "docs/index.html", "docs/assets/playbook.css", "docs/_config.yml", "docs/CNAME"}


def safe_path(p):
    p = Path(p)
    return p.parts and p.parts[0] in ALLOWED_ROOTS and ".." not in p.parts


def write_guard(path, content):
    """Return a refusal string, or None if the write is allowed."""
    if path in PROTECTED:
        return "refused: protected file. The homepage renders docs/catalog.json; edit that instead."
    if path.startswith("docs/") and path.endswith(".md"):
        if Path(path).exists() and content.lstrip().startswith("---\nlayout: null"):
            return None
        return "refused: no Markdown under docs/ (it gets themed). Write index.html files instead."
    if path.startswith("docs/") and path.endswith(".html") and "assets/playbook.css" not in content:
        return "refused: public pages must link the shared stylesheet assets/playbook.css."
    return None


def run_model(ledger, state):
    import anthropic
    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": context(ledger, state)}]
    total = 0.0
    for _ in range(C.MAX_TOOL_TURNS):
        resp = client.messages.create(model=C.MODEL, max_tokens=C.MAX_TOKENS, system=prompts.SYSTEM,
                                      tools=prompts.TOOLS, messages=messages)
        total += cost_eur(resp.usage)
        messages.append({"role": "assistant", "content": resp.content})
        results, done = [], False
        for b in resp.content:
            if b.type != "tool_use":
                continue
            name, inp, out = b.name, b.input, "ok"
            try:
                if name == "write_file":
                    guard = None if not safe_path(inp["path"]) else write_guard(inp["path"], inp["content"])
                    if not safe_path(inp["path"]):
                        out = "refused: path must be under docs/, products/ or drafts/"
                    elif guard:
                        out = guard; log(f"write refused {inp['path']}: {guard}")
                    else:
                        p = Path(inp["path"]); p.parent.mkdir(parents=True, exist_ok=True)
                        p.write_text(inp["content"]); log(f"wrote {p}")
                elif name == "create_sellable":
                    dp = inp["delivery_path"]
                    if len(recent(state["products"], "created", 7)) >= C.MAX_PRODUCTS_PER_WEEK:
                        out = "refused: product throttle (1 per week)"
                    elif not (safe_path(dp) and dp.startswith("docs/") and Path(dp).exists()):
                        out = "refused: delivery_path must be an existing file under docs/"
                    else:
                        rel = dp[len("docs/"):]
                        rel = rel[:-len("index.html")] if rel.endswith("index.html") else rel
                        url, ids = S.create_sellable(inp["name"], inp["description"], float(inp["price_eur"]),
                                                     f"{C.SITE_BASE}/{rel}")
                        state["products"].append({"name": inp["name"], "price_eur": inp["price_eur"],
                                                  "checkout_url": url, "delivery": f"{C.SITE_BASE}/{rel}",
                                                  "stripe": ids, "created": now().isoformat()})
                        out = f"created. checkout_url={url}"
                        log(f"product created: {inp['name']} EUR {inp['price_eur']} -> {url}")
                elif name == "publish_article":
                    if not devto.enabled():
                        out = "refused: dev.to not configured"
                    elif len(recent(state["articles"], "published", 1)) >= C.MAX_ARTICLES_PER_DAY:
                        out = "refused: article throttle (1 per day)"
                    else:
                        url = devto.publish(inp["title"], inp["body_markdown"], inp.get("tags", []))
                        state["articles"].append({"title": inp["title"], "url": url, "published": now().isoformat()})
                        out = f"published: {url}"; log(f"article: {url}")
                elif name == "update_memory":
                    MEMORY.write_text(inp["content"])
                elif name == "finish":
                    log(f"finish: {inp['summary']}"); done = True
            except Exception as e:
                out = f"error: {e}"; log(f"ERROR {name}: {e}")
            results.append({"type": "tool_result", "tool_use_id": b.id, "content": out})
        if done or not results:
            break
        messages.append({"role": "user", "content": results})
    return total


def main():
    ledger, state = L.load(), load_state()
    if ledger.get("status") == "dead":
        log("agent is dead; exiting"); return 0
    if not ledger["entries"]:
        L.add(ledger, "info", 0, f"seeded with {C.SEED_EUR} {C.CURRENCY}")
    reconcile(ledger)
    reason = L.check_kill(ledger)
    if reason:
        ledger["status"] = "dead"; L.add(ledger, "info", 0, f"KILL: {reason}"); L.save(ledger)
        log(f"KILL: {reason}"); return 0
    if DRY:
        L.add(ledger, "info", 0, "dry run"); L.save(ledger); STATE.write_text(json.dumps(state, indent=2))
        log(f"dry run ok: {L.summary(ledger)}"); return 0
    cost = run_model(ledger, state)
    L.add(ledger, "spend", cost, "compute (tokens)")
    L.save(ledger); STATE.write_text(json.dumps(state, indent=2))
    log(f"run cost {cost:.4f} EUR; {L.summary(ledger)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
