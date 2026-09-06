"""Minimal Stripe client: create sellable products, reconcile payments."""
import os
import requests
from . import config as C

BASE = "https://api.stripe.com/v1"
TAX_CODE_DIGITAL = "txcd_10000000"  # General - Electronically Supplied Services


def _auth():
    return (os.environ["STRIPE_SECRET_KEY"], "")


def _post(path, data):
    r = requests.post(f"{BASE}{path}", auth=_auth(), data=data, timeout=30)
    if r.status_code >= 400:
        try:
            msg = r.json().get("error", {}).get("message", r.text)
        except Exception:
            msg = r.text
        raise RuntimeError(f"stripe {path} {r.status_code}: {msg[:300]}")
    return r.json()


def _get(path, params=None):
    r = requests.get(f"{BASE}{path}", auth=_auth(), params=params or {}, timeout=30)
    r.raise_for_status()
    return r.json()


def create_sellable(name, description, price_eur, delivery_url):
    """Product + price + payment link. Returns (payment_link_url, ids)."""
    prod = _post("/products", {"name": name, "description": description[:500], "tax_code": TAX_CODE_DIGITAL})
    price = _post("/prices", {"product": prod["id"], "unit_amount": int(round(price_eur * 100)),
                              "currency": "eur"})
    body = {
        "line_items[0][price]": price["id"], "line_items[0][quantity]": 1,
        "after_completion[type]": "redirect",
        "after_completion[redirect][url]": delivery_url,
        "metadata[pot50_product]": name,
    }
    try:
        link = _post("/payment_links", body)
    except RuntimeError as e:
        if "managed" in str(e).lower() or "tax code" in str(e).lower():
            link = _post("/payment_links", {**body, "managed_payments[enabled]": "false"})
        else:
            raise
    return link["url"], {"product": prod["id"], "price": price["id"], "payment_link": link["id"]}


def succeeded_charges(limit=100):
    out, params = [], {"limit": limit}
    while True:
        data = _get("/charges", params)
        out.extend(c for c in data["data"] if c["status"] == "succeeded" and not c.get("refunded"))
        if not data.get("has_more"):
            return out
        params["starting_after"] = data["data"][-1]["id"]


def net_eur(charge):
    amt = charge["amount"] / 100.0
    if charge.get("currency", "eur").lower() != "eur":
        amt *= C.USD_TO_EUR
    return max(amt * (1 - C.STRIPE_FEE_RATE) - C.STRIPE_FIXED_FEE_EUR, 0)
