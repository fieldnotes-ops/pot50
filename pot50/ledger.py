"""Single source of truth for money. Only this module writes ledger.json."""
import json
from datetime import datetime, timezone, date
from pathlib import Path
from . import config as C

PATH = Path("ledger.json")


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load():
    if not PATH.exists():
        return {
            "currency": C.CURRENCY,
            "seed": C.SEED_EUR,
            "started": _now(),
            "status": "active",
            "entries": [],
            "reconciled_sale_ids": [],
        }
    return json.loads(PATH.read_text())


def save(ledger):
    PATH.write_text(json.dumps(ledger, indent=2))


def add(ledger, kind, amount_eur, note, ref=None):
    """kind: 'revenue' (positive, net) | 'spend' (positive, money out) | 'info'"""
    ledger["entries"].append({
        "ts": _now(), "kind": kind, "amount": round(float(amount_eur), 4), "note": note, "ref": ref,
    })


def summary(ledger):
    earned = sum(e["amount"] for e in ledger["entries"] if e["kind"] == "revenue")
    spent = sum(e["amount"] for e in ledger["entries"] if e["kind"] == "spend")
    cap = ledger["seed"] + C.REINVEST_RATE * earned
    remaining = cap - spent
    rev_dates = [e["ts"] for e in ledger["entries"] if e["kind"] == "revenue"]
    anchor = max(rev_dates) if rev_dates else ledger["started"]
    days_since_rev = (datetime.now(timezone.utc) - datetime.fromisoformat(anchor)).days
    return {
        "seed": ledger["seed"],
        "cumulative_net_revenue": round(earned, 2),
        "cumulative_spend": round(spent, 2),
        "spend_cap": round(cap, 2),
        "remaining_spend_capacity": round(remaining, 2),
        "days_since_last_revenue": days_since_rev,
        "return_multiple": round(earned / ledger["seed"], 3) if ledger["seed"] else 0,
        "status": ledger.get("status", "active"),
    }


def check_kill(ledger):
    s = summary(ledger)
    if s["remaining_spend_capacity"] < C.KILL_BALANCE_EUR:
        return f"remaining spend capacity {s['remaining_spend_capacity']} < {C.KILL_BALANCE_EUR}"
    if s["days_since_last_revenue"] >= C.KILL_DAYS_NO_REVENUE:
        return f"{s['days_since_last_revenue']} days without revenue"
    return None


def can_spend(ledger, amount_eur):
    return summary(ledger)["remaining_spend_capacity"] - amount_eur >= 0
