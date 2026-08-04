"""
=========================================================
ShopSphere Analytics

inventory_generator.py

Generates:
    output/csv/inventory.csv

Author : Prasanta Kumar Deb
=========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import random

from datetime import datetime

import pandas as pd

from config.config import (

    CSV_OUTPUT,

    REFERENCE_DATA,

    RANDOM_SEED

)

# ==========================================================
# Random Seed
# ==========================================================

random.seed(

    RANDOM_SEED

)

# ==========================================================
# Generator Configuration
# ==========================================================

START_DATE = datetime(

    2022,

    1,

    1

)

END_DATE = datetime.today()

MIN_WAREHOUSES_PER_PRODUCT = 2

MAX_WAREHOUSES_PER_PRODUCT = 8

PROGRESS_INTERVAL = 10000

# ==========================================================
# Load Master Data
# ==========================================================

def load_master_data():

    data = {

        "Products": pd.read_csv(

            CSV_OUTPUT / "products.csv"

        ),

        "Warehouses": pd.read_csv(

            REFERENCE_DATA / "warehouses.csv"

        ),

        "Categories": pd.read_csv(

            REFERENCE_DATA / "categories.csv"

        )

    }

    return data


# ==========================================================
# Load Once
# ==========================================================

MASTER = load_master_data()

PRODUCTS = MASTER["Products"]

WAREHOUSES = MASTER["Warehouses"]

CATEGORIES = MASTER["Categories"]

# ==========================================================
# Validation
# ==========================================================

def validate_master_data():

    print("=" * 60)

    print("Inventory Generator Configuration")

    print("=" * 60)

    if PRODUCTS.empty:

        raise ValueError(

            "products.csv is empty."

        )

    if WAREHOUSES.empty:

        raise ValueError(

            "warehouses.csv is empty."

        )

    if CATEGORIES.empty:

        raise ValueError(

            "categories.csv is empty."

        )

    print(f"Products               : {len(PRODUCTS):,}")

    print(f"Warehouses            : {len(WAREHOUSES):,}")

    print(f"Categories            : {len(CATEGORIES):,}")

    print(f"Warehouse/Product Min : {MIN_WAREHOUSES_PER_PRODUCT}")

    print(f"Warehouse/Product Max : {MAX_WAREHOUSES_PER_PRODUCT}")

    print("=" * 60)
# ==========================================================
# Warehouses Per Product
# ==========================================================

WAREHOUSE_DISTRIBUTION = {

    2: 10,

    3: 15,

    4: 25,

    5: 25,

    6: 15,

    7: 7,

    8: 3

}

# ==========================================================
# Category Stock Rules
# (Min Stock, Max Stock)
# ==========================================================

CATEGORY_STOCK_RULES = {

    "Electronics": (20, 250),

    "Fashion": (100, 1200),

    "Home & Kitchen": (50, 600),

    "Beauty & Personal Care": (200, 2000),

    "Grocery": (1000, 5000),

    "Books": (50, 800),

    "Sports & Fitness": (40, 500),

    "Toys & Games": (50, 400),

    "Automotive": (20, 300),

    "Baby Products": (100, 1000),

    "Health": (100, 1500),

    "Jewellery": (5, 50),

    "Pet Supplies": (50, 600),

    "Office Supplies": (100, 1000),

    "Garden & Outdoor": (30, 400)

}

# ==========================================================
# Reserved Stock %
# ==========================================================

RESERVED_STOCK_PERCENTAGE = {

    "minimum": 0.00,

    "maximum": 0.20

}

# ==========================================================
# Reorder Level %
# ==========================================================

REORDER_PERCENTAGE = {

    "minimum": 0.10,

    "maximum": 0.30

}

# ==========================================================
# Safety Stock %
# ==========================================================

SAFETY_STOCK_PERCENTAGE = {

    "minimum": 0.30,

    "maximum": 0.80

}

# ==========================================================
# Warehouse Allocation
# ==========================================================

WAREHOUSE_WEIGHTS = {

    1: 15,

    2: 12,

    3: 10,

    4: 8,

    5: 8,

    6: 7,

    7: 6,

    8: 5,

    9: 5,

    10: 4,

    11: 4,

    12: 4,

    13: 3,

    14: 3,

    15: 3,

    16: 2,

    17: 2,

    18: 2,

    19: 2,

    20: 2,

    21: 1,

    22: 1,

    23: 1,

    24: 1,

    25: 1,

    26: 1,

    27: 1,

    28: 1,

    29: 1,

    30: 1,

    31: 1,

    32: 1,

    33: 1,

    34: 1,

    35: 1,

    36: 1,

    37: 1,

    38: 1,

    39: 1,

    40: 1

}
# ==========================================================
# Weighted Warehouse Pool
# ==========================================================

WAREHOUSE_POOL = []

for warehouse_id, weight in WAREHOUSE_WEIGHTS.items():

    WAREHOUSE_POOL.extend(

        [warehouse_id] * weight

    )

# ==========================================================
# Warehouse Capacity Utilization
# ==========================================================

TARGET_UTILIZATION = {

    "minimum": 0.70,

    "maximum": 0.95

}

# ==========================================================
# Active Inventory Probability
# ==========================================================

ACTIVE_PRODUCT_PERCENTAGE = 98

# ==========================================================
# Warehouse Capacity Tracker
# ==========================================================

warehouse_capacity = {

     row.WarehouseID: row.Capacity

    for row in WAREHOUSES.itertuples(index=False)

}

warehouse_used = {

    warehouse_id: 0

    for warehouse_id in warehouse_capacity

}

# ==========================================================
# Select Warehouses
# ==========================================================

def select_warehouses():

    number_of_warehouses = random.choices(

        population=list(
            WAREHOUSE_DISTRIBUTION.keys()
        ),

        weights=list(
            WAREHOUSE_DISTRIBUTION.values()
        ),

        k=1

    )[0]

    warehouses = set()

    while len(warehouses) < number_of_warehouses:

        warehouses.add(

            random.choice(

                WAREHOUSE_POOL

            )

        )

    return list(warehouses)

# ==========================================================
# Stock Quantity
# ==========================================================

def generate_stock(

    category_name

):

    minimum, maximum = CATEGORY_STOCK_RULES[

        category_name

    ]

    return random.randint(

        minimum,

        maximum

    )

# ==========================================================
# Reserved Quantity
# ==========================================================

def generate_reserved_quantity(

    stock

):

    reserved = int(

        stock *

        random.uniform(

            RESERVED_STOCK_PERCENTAGE["minimum"],

            RESERVED_STOCK_PERCENTAGE["maximum"]

        )

    )

    return reserved

# ==========================================================
# Reorder Level
# ==========================================================

def generate_reorder_level(

    stock

):

    reorder = int(

        stock *

        random.uniform(

            REORDER_PERCENTAGE["minimum"],

            REORDER_PERCENTAGE["maximum"]

        )

    )

    return max(

        reorder,

        1

    )

# ==========================================================
# Safety Stock
# ==========================================================

def generate_safety_stock(

    reorder_level

):

    safety = int(

        reorder_level *

        random.uniform(

            SAFETY_STOCK_PERCENTAGE["minimum"],

            SAFETY_STOCK_PERCENTAGE["maximum"]

        )

    )

    return max(

        safety,

        1

    )

# ==========================================================
# Restock Date
# ==========================================================

def generate_last_restocked():

    days = (

        END_DATE -

        START_DATE

    ).days

    return (

        START_DATE +

        pd.Timedelta(

            days=random.randint(

                0,

                days

            )

        )

    ).date()

# ==========================================================
# Stock Updated Date
# ==========================================================

def generate_last_stock_updated(

    last_restocked

):

    today = datetime.today().date()

    days = (

        today -

        last_restocked

    ).days

    return (

        last_restocked +

        pd.Timedelta(

            days=random.randint(

                0,

                max(

                    days,

                    0

                )

            )

        )

    )

# ==========================================================
# Capacity Allocation
# ==========================================================

def allocate_stock(

    warehouse_id,

    stock

):

    capacity = warehouse_capacity[

        warehouse_id

    ]

    used = warehouse_used[

        warehouse_id

    ]

    if used + stock > capacity:

        return False

    warehouse_used[

        warehouse_id

    ] += stock

    return True
# ==========================================================
# Generate Inventory
# ==========================================================

def generate_inventory():

    print("=" * 60)
    print("Generating Inventory")
    print("=" * 60)

    # ------------------------------------------------------
    # Validate Master Data
    # ------------------------------------------------------

    validate_master_data()

    # ------------------------------------------------------
    # Category Lookup
    # ------------------------------------------------------

    category_lookup = (

        CATEGORIES

        .set_index(

            "CategoryID"

        )

        ["CategoryName"]

        .to_dict()

    )

    # ------------------------------------------------------
    # Output File
    # ------------------------------------------------------

    CSV_OUTPUT.mkdir(

        parents=True,

        exist_ok=True

    )

    output_file = (

        CSV_OUTPUT /

        "inventory.csv"

    )

    # Remove existing file

    if output_file.exists():

        output_file.unlink()

    # ------------------------------------------------------
    # Configuration
    # ------------------------------------------------------

    CHUNK_SIZE = 100000

    inventory_id = 1

    total_records = 0

    chunk_number = 1

    rows = []

    write_header = True

    # ------------------------------------------------------
    # Products Iterator
    # ------------------------------------------------------

    products = PRODUCTS.itertuples(

        index=False

    )

    print()

    print("Inventory generation started...")

    print(f"Chunk Size : {CHUNK_SIZE:,}")

    print()
    # ------------------------------------------------------
    # Generate Inventory
    # ------------------------------------------------------

    for product in products:

        # ----------------------------------------------
        # Category
        # ----------------------------------------------

        category_name = category_lookup.get(

            product.CategoryID

        )

        if category_name is None:

            continue

        # ----------------------------------------------
        # Warehouses
        # ----------------------------------------------

        selected_warehouses = select_warehouses()

        # ----------------------------------------------
        # Generate Inventory
        # ----------------------------------------------

        for warehouse_id in selected_warehouses:

            # --------------------------------------
            # Stock
            # --------------------------------------

            stock = generate_stock(

                category_name

            )

            # --------------------------------------
            # Capacity Check
            # --------------------------------------

            if not allocate_stock(

                warehouse_id,

                stock

            ):

                continue

            # --------------------------------------
            # Reserved
            # --------------------------------------

            reserved = generate_reserved_quantity(

                stock

            )

            # --------------------------------------
            # Reorder
            # --------------------------------------

            reorder = generate_reorder_level(

                stock

            )

            # --------------------------------------
            # Safety Stock
            # --------------------------------------

            safety = generate_safety_stock(

                reorder

            )

            # --------------------------------------
            # Dates
            # --------------------------------------

            last_restocked = generate_last_restocked()

            last_updated = generate_last_stock_updated(

                last_restocked

            )

            # --------------------------------------
            # Store Row
            # --------------------------------------

            rows.append(

                {

                    "InventoryID": int(

                        inventory_id

                    ),

                    "ProductID": int(

                        product.ProductID

                    ),

                    "WarehouseID": int(

                        warehouse_id

                    ),

                    "StockQuantity": int(

                        stock

                    ),

                    "ReservedQuantity": int(

                        reserved

                    ),

                    "ReorderLevel": int(

                        reorder

                    ),

                    "SafetyStock": int(

                        safety

                    ),

                    "LastRestocked": last_restocked,

                    "LastStockUpdated": last_updated

                }

            )

            inventory_id += 1

            total_records += 1
            # --------------------------------------
            # Chunk Write
            # --------------------------------------

            if len(rows) >= CHUNK_SIZE:

                chunk = pd.DataFrame(

                    rows

                )

                chunk.to_csv(

                    output_file,

                    mode="w" if write_header else "a",

                    header=write_header,

                    index=False

                )

                print(

                    f"Chunk {chunk_number:,} Saved | "

                    f"Records : {total_records:,}"

                )

                chunk_number += 1

                write_header = False

                rows.clear()
    # ------------------------------------------------------
    # Write Remaining Records
    # ------------------------------------------------------

    if rows:

        chunk = pd.DataFrame(

            rows

        )

        chunk.to_csv(

            output_file,

            mode="w" if write_header else "a",

            header=write_header,

            index=False

        )

        print(

            f"Chunk {chunk_number:,} Saved | "

            f"Records : {total_records:,}"

        )

        rows.clear()

    # ------------------------------------------------------
    # Warehouse Utilization Summary
    # ------------------------------------------------------

    print()

    print("=" * 60)

    print("WAREHOUSE UTILIZATION")

    print("=" * 60)

    utilization_rows = []

    for warehouse in WAREHOUSES.itertuples(index=False):

        capacity = warehouse_capacity[

            warehouse.WarehouseID

        ]

        used = warehouse_used[

            warehouse.WarehouseID

        ]

        utilization = (

            used / capacity * 100

            if capacity > 0

            else 0

        )

        utilization_rows.append({

            "WarehouseID": warehouse.WarehouseID,

            "WarehouseName": warehouse.WarehouseName,

            "Capacity": capacity,

            "Used": used,

            "Utilization%": round(

                utilization,

                2

            )

        })

    utilization_df = pd.DataFrame(

        utilization_rows

    )

    print(

        utilization_df

    )

    # ------------------------------------------------------
    # Generation Summary
    # ------------------------------------------------------

    print()

    print("=" * 60)

    print("INVENTORY GENERATION COMPLETED")

    print("=" * 60)

    print(

        f"Products Processed : {len(PRODUCTS):,}"

    )

    print(

        f"Warehouses         : {len(WAREHOUSES):,}"

    )

    print(

        f"Inventory Records  : {total_records:,}"

    )

    print(

        f"Output File        : {output_file}"

    )

    print("=" * 60)

    return output_file
# ==========================================================
# Validate Inventory
# ==========================================================

def validate_inventory():

    print("=" * 60)
    print("Validating Inventory")
    print("=" * 60)

    inventory_file = (

        CSV_OUTPUT /

        "inventory.csv"

    )

    if not inventory_file.exists():

        raise FileNotFoundError(

            "inventory.csv not found."

        )

    inventory = pd.read_csv(

        inventory_file,

        parse_dates=[

            "LastRestocked",

            "LastStockUpdated"

        ]

    )

    # ------------------------------------------------------
    # Empty Dataset
    # ------------------------------------------------------

    if inventory.empty:

        raise ValueError(

            "Inventory dataset is empty."

        )

    print("✓ Dataset Validation Passed")

    # ------------------------------------------------------
    # Duplicate InventoryID
    # ------------------------------------------------------

    if inventory["InventoryID"].duplicated().any():

        raise ValueError(

            "Duplicate InventoryID found."

        )

    print("✓ InventoryID Validation Passed")

    # ------------------------------------------------------
    # Duplicate Product + Warehouse
    # ------------------------------------------------------

    duplicate_pairs = inventory.duplicated(

        subset=[

            "ProductID",

            "WarehouseID"

        ]

    ).sum()

    if duplicate_pairs > 0:

        raise ValueError(

            f"{duplicate_pairs:,} duplicate Product/Warehouse combinations found."

        )

    print("✓ Product/Warehouse Validation Passed")

    # ------------------------------------------------------
    # Stock Validation
    # ------------------------------------------------------

    if (

        inventory["StockQuantity"] < 0

    ).any():

        raise ValueError(

            "Negative StockQuantity found."

        )

    print("✓ Stock Validation Passed")

    # ------------------------------------------------------
    # Reserved Quantity
    # ------------------------------------------------------

    invalid_reserved = inventory[

        inventory["ReservedQuantity"] >

        inventory["StockQuantity"]

    ]

    if len(invalid_reserved) > 0:

        raise ValueError(

            "ReservedQuantity exceeds StockQuantity."

        )

    print("✓ Reserved Quantity Validation Passed")

    # ------------------------------------------------------
    # Reorder Level
    # ------------------------------------------------------

    invalid_reorder = inventory[

        inventory["ReorderLevel"] >

        inventory["StockQuantity"]

    ]

    if len(invalid_reorder) > 0:

        raise ValueError(

            "ReorderLevel exceeds StockQuantity."

        )

    print("✓ Reorder Level Validation Passed")

    # ------------------------------------------------------
    # Safety Stock
    # ------------------------------------------------------

    invalid_safety = inventory[

        inventory["SafetyStock"] >

        inventory["ReorderLevel"]

    ]

    if len(invalid_safety) > 0:

        raise ValueError(

            "SafetyStock exceeds ReorderLevel."

        )

    print("✓ Safety Stock Validation Passed")

    # ------------------------------------------------------
    # Date Validation
    # ------------------------------------------------------

    today = pd.Timestamp.today().normalize()

    if (

        inventory["LastRestocked"] >

        today

    ).any():

        raise ValueError(

            "Future LastRestocked found."

        )

    if (

        inventory["LastStockUpdated"] >

        today

    ).any():

        raise ValueError(

            "Future LastStockUpdated found."

        )

    if (

        inventory["LastStockUpdated"] <

        inventory["LastRestocked"]

    ).any():

        raise ValueError(

            "LastStockUpdated earlier than LastRestocked."

        )

    print("✓ Date Validation Passed")

    # ------------------------------------------------------
    # Warehouse Capacity Validation
    # ------------------------------------------------------

    warehouse_summary = (

        inventory

        .groupby(

            "WarehouseID"

        )["StockQuantity"]

        .sum()

    )

    for warehouse in WAREHOUSES.itertuples(index=False):

        total_stock = warehouse_summary.get(

            warehouse.WarehouseID,

            0

        )

        if total_stock > warehouse.Capacity:

            raise ValueError(

                f"Warehouse {warehouse.WarehouseID} exceeds capacity."

            )

    print("✓ Warehouse Capacity Validation Passed")

    # ------------------------------------------------------
    # Summary
    # ------------------------------------------------------

    print("=" * 60)

    print("ALL INVENTORY VALIDATIONS PASSED")

    print("=" * 60)

    print(f"Inventory Records : {len(inventory):,}")

    print(f"Products          : {inventory['ProductID'].nunique():,}")

    print(f"Warehouses        : {inventory['WarehouseID'].nunique():,}")

    print(f"Total Stock       : {inventory['StockQuantity'].sum():,}")

    print(f"Average Stock     : {inventory['StockQuantity'].mean():.2f}")

    print("=" * 60)

    return True
# ==========================================================
# Main
# ==========================================================

def main():

    print()

    print("=" * 60)
    print("SHOPSPHERE INVENTORY GENERATOR")
    print("=" * 60)

    start_time = datetime.now()

    # ------------------------------------------------------
    # Generate Inventory
    # ------------------------------------------------------

    output_file = generate_inventory()

    # ------------------------------------------------------
    # Validate Inventory
    # ------------------------------------------------------

    validate_inventory()

    # ------------------------------------------------------
    # Execution Time
    # ------------------------------------------------------

    end_time = datetime.now()

    duration = end_time - start_time

    print()

    print("=" * 60)
    print("GENERATION COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print(f"Output File   : {output_file}")

    print(f"Started At    : {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    print(f"Completed At  : {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

    print(f"Duration      : {duration}")

    print("=" * 60)


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    main()
    