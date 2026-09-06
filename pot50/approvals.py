"""Human approval gate via GitHub Issues. The agent opens issues; the repo owner comments
'approve' or 'reject'; the next run reads the verdict and closes the issue."""
import os
import requests
from . import config as C

API = "https://api.github.com"


def _h():
    return {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "Accept": "application/vnd.github+json"}


def _repo():
    return os.environ["GITHUB_REPOSITORY"]


def open_request(kind, title, body):
    """kind: spend | publish | account"""
    label = f"{C.APPROVAL_LABEL_PREFIX}:{kind}"
    _ensure_label(label)
    r = requests.post(f"{API}/repos/{_repo()}/issues", headers=_h(), timeout=30,
                      json={"title": f"[{kind.upper()}] {title}", "body": body, "labels": [label]})
    r.raise_for_status()
    return r.json()["number"]


def _ensure_label(label):
    requests.post(f"{API}/repos/{_repo()}/labels", headers=_h(), timeout=30,
                  json={"name": label, "color": "d93f0b"})  # 422 if exists; ignored


def pending():
    r = requests.get(f"{API}/repos/{_repo()}/issues", headers=_h(), timeout=30,
                     params={"state": "open", "labels": "", "per_page": 50})
    r.raise_for_status()
    return [i for i in r.json() if any(l["name"].startswith(C.APPROVAL_LABEL_PREFIX) for l in i["labels"])]


def resolve():
    """Return list of (issue, verdict) for issues that received a verdict; closes them."""
    owner = _repo().split("/")[0].lower()
    out = []
    for issue in pending():
        n = issue["number"]
        r = requests.get(f"{API}/repos/{_repo()}/issues/{n}/comments", headers=_h(), timeout=30)
        r.raise_for_status()
        verdict = None
        for c in r.json():
            if c["user"]["login"].lower() != owner:
                continue
            t = c["body"].strip().lower()
            if t.startswith("approve"):
                verdict = "approved"
            elif t.startswith("reject"):
                verdict = "rejected"
        if verdict:
            requests.patch(f"{API}/repos/{_repo()}/issues/{n}", headers=_h(), timeout=30,
                           json={"state": "closed"})
            out.append((issue, verdict))
    return out
