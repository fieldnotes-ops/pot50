# pot50

Autonomous revenue agent seeded with EUR 50.

Rules enforced in code (see `pot50/config.py`):

- Spend cap = 50 + 0.5 x cumulative net revenue
- Kill if remaining spend capacity < EUR 5, or 30 days without revenue
- Any publish, new account, or spend over EUR 5 needs a human `approve` comment on a GitHub Issue

## Operating it

- Runs at 07:00 and 19:00 UTC via GitHub Actions. Trigger manually from the Actions tab; set `dry_run` to `true` for a smoke test.
- Approvals arrive as Issues labelled `approval:*`. Comment `approve` or `reject`. The next run picks it up.
- `ledger.json` is the money source of truth. Only the code writes it.
- `memory.md` is the agent's memory. `decisions.log` is the audit trail.
- To publish: the agent puts product files and listing copy in `products/`; you create the product on Gumroad from those files. Sales reconcile automatically.
- To spend money the agent needs your approval and you make the payment; then add a ledger entry by committing to `ledger.json` (a `spend` entry) so the cap stays honest.

## Secrets (repo Settings > Secrets > Actions)

`ANTHROPIC_API_KEY`, `GUMROAD_ACCESS_TOKEN`. Card secrets are stored for future use and are not read by v1; the agent cannot pay for anything on its own.
