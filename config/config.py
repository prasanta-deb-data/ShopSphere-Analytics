"""
=========================================================
ShopSphere Analytics
config.py

Central Configuration File
=========================================================
"""

from pathlib import Path

# =========================================================
# Project Paths
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

REFERENCE_DATA = PROJECT_ROOT / "reference_data"

OUTPUT_FOLDER = PROJECT_ROOT / "output"

CSV_OUTPUT = OUTPUT_FOLDER / "csv"

LOG_FOLDER = OUTPUT_FOLDER / "logs"

# =========================================================
# SQL Server
# =========================================================

SQL_SERVER = r"localhost"

DATABASE = "ShopSphereAnalytics"

DRIVER = "ODBC Driver 17 for SQL Server"

TRUSTED_CONNECTION = "yes"

# =========================================================
# Random Seed
# =========================================================

RANDOM_SEED = 42

# =========================================================
# Data Generation Size
# =========================================================

NUM_STATES = 28

NUM_CITIES = 500

NUM_CATEGORIES = 15

NUM_SUBCATEGORIES = 60

NUM_BRANDS = 300

NUM_SUPPLIERS = 250

NUM_WAREHOUSES = 40

NUM_CUSTOMERS = 100_000

NUM_PRODUCTS = 15_000

NUM_INVENTORY = 60_000

NUM_COUPONS = 500

NUM_ORDERS = 500_000

NUM_ORDER_ITEMS = 1_500_000

NUM_PAYMENTS = 500_000

NUM_SHIPMENTS = 500_000

NUM_REVIEWS = 250_000

NUM_RETURNS = 40_000

NUM_SUPPORT_TICKETS = 50_000

NUM_WEBSITE_TRAFFIC = 2_000_000

# =========================================================
# Date Range
# =========================================================

START_DATE = "2023-01-01"

END_DATE = "2025-12-31"

# =========================================================
# Product Pricing
# =========================================================

MIN_COST = 100

MAX_COST = 50000

MIN_MARGIN = 0.10

MAX_MARGIN = 0.45

GST_RATE = 0.18

# =========================================================
# Inventory
# =========================================================

MIN_STOCK = 0

MAX_STOCK = 1000

DEFAULT_REORDER_LEVEL = 25

DEFAULT_SAFETY_STOCK = 10

# =========================================================
# Orders
# =========================================================

MIN_ITEMS_PER_ORDER = 1

MAX_ITEMS_PER_ORDER = 8

MAX_ORDER_DISCOUNT = 3000

MAX_SHIPPING_CHARGE = 250

# =========================================================
# Review Distribution
# =========================================================

RATING_WEIGHTS = {

    5: 0.48,

    4: 0.26,

    3: 0.14,

    2: 0.07,

    1: 0.05

}

# =========================================================
# Return Probability
# =========================================================

RETURN_RATE = 0.08

# =========================================================
# Website Traffic
# =========================================================

CONVERSION_RATE = 0.035

BOUNCE_RATE = 0.38

# =========================================================
# Faker Locale
# =========================================================

FAKER_LOCALE = "en_IN"

# =========================================================
# Output Encoding
# =========================================================

CSV_ENCODING = "utf-8"

# =========================================================
# Create Required Folders
# =========================================================

CSV_OUTPUT.mkdir(parents=True, exist_ok=True)

LOG_FOLDER.mkdir(parents=True, exist_ok=True)

# ==========================================================
# SQL Server Configuration
# ==========================================================

SQL_SERVER = r"localhost\SQLEXPRESS"

DATABASE_NAME = "ShopSphereAnalytics"

ODBC_DRIVER = "ODBC Driver 17 for SQL Server"

TRUSTED_CONNECTION = "yes"