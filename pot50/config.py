"""All tunable numbers live here."""
CURRENCY = "EUR"
SEED_EUR = 50.00
REINVEST_RATE = 0.5
KILL_BALANCE_EUR = 5.00
KILL_DAYS_NO_REVENUE = 30

MODEL = "claude-sonnet-5"
MAX_TOKENS = 8000
MAX_TOOL_TURNS = 10
USD_TO_EUR = 0.92
PRICE_INPUT_PER_M_USD = 3.00     # verify: https://docs.claude.com/en/docs/about-claude/pricing
PRICE_OUTPUT_PER_M_USD = 15.00

STRIPE_FEE_RATE = 0.015          # EU cards; verify against your Stripe pricing
STRIPE_FIXED_FEE_EUR = 0.25

# Anti-spam throttles, enforced in code
MAX_PRODUCTS_PER_WEEK = 1
MAX_ARTICLES_PER_DAY = 1

SITE_BASE = "https://fieldnotesops.com"
BRAND = "Fieldnotes Ops"          # public brand; the operator's name never appears
