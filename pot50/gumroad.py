"""Read-only Gumroad client. Product creation is done by the human via an approval issue;
the API is used to reconcile sales into the ledger."""
import os
import requests
from . import config as C

BASE = "https://api.gumroad.com/v2"


def _tok():
    return os.environ["GUMROAD_ACCESS_TOKEN"]


def products():
    r = requests.get(f"{BASE}/products", params={"access_token": _tok()}, timeout=30)
    r.raise_for_status()
    return r.json().get("products", [])


def sales(after=None):
    params = {"access_token": _tok()}
    if after:
        params["after"] = after  # YYYY-MM-DD
    out, page = [], 1
    while True:
        params["page"] = page
        r = requests.get(f"{BASE}/sales", params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        out.extend(data.get("sales", []))
        if not data.get("next_page_url"):
            break
        page += 1
    return out


def net_eur(sale):
    """Estimate net payout in EUR from a Gumroad sale record."""
    gross_usd = float(sale.get("price", 0)) / 100.0
    net_usd = gross_usd * (1 - C.GUMROAD_FEE_RATE - C.PAYMENT_PROCESSING_RATE) - C.GUMROAD_FIXED_FEE_USD
    return max(net_usd, 0) * C.USD_TO_EUR
