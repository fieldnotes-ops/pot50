# pot50

Fully autonomous revenue agent seeded with EUR 50. No human in the loop after setup.

Enforced in code (`pot50/config.py`): spend cap = 50 + 0.5 x net revenue; kill at < EUR 5 capacity or 30 days without revenue; max 1 product per week, 1 article per day.

How it works: the agent writes product and delivery pages into `docs/` (served by GitHub Pages), creates Stripe products and payment links, publishes dev.to articles for traffic, and reconciles Stripe payments into `ledger.json`. `memory.md` is its memory, `decisions.log` the audit trail, `state.json` the live product list.

Secrets: `ANTHROPIC_API_KEY`, `STRIPE_SECRET_KEY` (restricted key: Products, Prices, Payment Links write; Charges read), `DEVTO_API_KEY` (optional).
