"""All tunable numbers live here. Change them in a commit, not in the agent's head."""

CURRENCY = "EUR"
SEED_EUR = 50.00                 # pot balance at start
REINVEST_RATE = 0.5              # agent may spend SEED + REINVEST_RATE * cumulative net revenue
KILL_BALANCE_EUR = 5.00          # stop when remaining spend capacity falls below this
KILL_DAYS_NO_REVENUE = 30        # stop after this many days without a sale
APPROVAL_SPEND_THRESHOLD_EUR = 5.00

MODEL = "claude-sonnet-5"        # keep cheap; upgrade only if revenue justifies it
MAX_TOKENS = 4000
USD_TO_EUR = 0.92                # update occasionally
# Token prices in USD per 1M tokens. Verify against https://docs.claude.com/en/docs/about-claude/pricing
PRICE_INPUT_PER_M_USD = 3.00
PRICE_OUTPUT_PER_M_USD = 15.00

# Gumroad fee model used for net revenue estimates. Verify against current Gumroad pricing.
GUMROAD_FEE_RATE = 0.10
GUMROAD_FIXED_FEE_USD = 0.30
PAYMENT_PROCESSING_RATE = 0.029

APPROVAL_LABEL_PREFIX = "approval"
