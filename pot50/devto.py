"""Publish articles to dev.to via its API (optional; skipped if DEVTO_API_KEY is unset)."""
import os
import requests


def enabled():
    return bool(os.environ.get("DEVTO_API_KEY"))


def publish(title, body_markdown, tags, canonical_url=None):
    payload = {"article": {"title": title, "body_markdown": body_markdown,
                           "published": True, "tags": tags[:4]}}
    if canonical_url:
        payload["article"]["canonical_url"] = canonical_url
    r = requests.post("https://dev.to/api/articles", json=payload, timeout=30,
                      headers={"api-key": os.environ["DEVTO_API_KEY"], "Content-Type": "application/json"})
    r.raise_for_status()
    return r.json().get("url")
