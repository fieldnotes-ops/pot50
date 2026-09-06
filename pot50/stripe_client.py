"""Minimal Stripe client: create sellable products, reconcile payments."""
import os
import requests
from . import config as C

BASE = "https://api.stripe.com/v1"


def _auth():
    return (os.environ["STRIPE_SECRET_KEY"], "")


def _post(path, data):
    r = requests.post(f"{BASE}{path}", auth=_auth(), data=data, timeout=30)
    r.raise_for_status()
    return r.json()


def _get(path, params=None):
    r = requests.get(f"{BASE}{path}", auth=_auth(), params=params or {}, timeout=30)
    r.raise_for_status()
    return r.json()


def create_sellable(name, description, price_eur, delivery_url):
    """Product + price + payment link. Returns (payment_link_url, ids)."""
    prod = _post("/products", {"name": name, "description": description[:500]})
    price = _post("/prices", {"product": prod["id"], "unit_amount": int(round(price_eur * 100)),
                              "currency": "eur"})
    link = _post("/payment_links", {
        "line_items[0][price]": price["id"], "line_items[0][quantity]": 1,
        "after_completion[type]": "redirect",
        "after_completion[redirect][url]": delivery_url,
        "metadata[pot50_product]": name,
    })
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
        amt *= C.USD_TO_EUR  # rough
    return max(amt * (1 - C.STRIPE_FEE_RATE) - C.STRIPE_FIXED_FEE_EUR, 0)
