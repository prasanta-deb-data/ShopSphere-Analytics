"""
=========================================================
ShopSphere Analytics
inventory_generator.py

Generates:
    output/csv/inventory.csv

Author : Prasanta Kumar Deb
=========================================================
"""

import random
from datetime import datetime, timedelta

import pandas as pd

from config.config import (
    CSV_OUTPUT,
    RANDOM_SEED
)

random.seed(RANDOM_SEED)

# ==========================================================
# Load Data
# ==========================================================

def load_data():

    products = pd.read_csv(
        CSV_OUTPUT / "products.csv"
    )

    warehouses = pd.read_csv(
        "reference_data/warehouses.csv"
    )

    return products, warehouses

# ==========================================================
# Distribution
# ==========================================================
WAREHOUSE_DISTRIBUTION = {

    1:0.25,

    2:0.35,

    3:0.25,

    4:0.10,

    5:0.05

}

# ==========================================================
# Weighted Choice
# ==========================================================
def weighted_choice(mapping):

    return random.choices(

        list(mapping.keys()),

        weights=list(mapping.values()),

        k=1

    )[0]

# ==========================================================
# Restock Date
# ==========================================================
def random_restock_date():

    start = datetime(2023,1,1)

    end = datetime(2025,12,31)

    days = (end-start).days

    return start + timedelta(

        days=random.randint(0,days)

    )
    
# ==========================================================
# Generate Inventory
# ==========================================================

def generate_inventory():

    products, warehouses = load_data()

    inventory = []

    inventory_id = 1

    print("=" * 60)
    print("Generating Inventory...")
    print("=" * 60)

    for _, product in products.iterrows():

        product_id = int(product["ProductID"])

        warehouse_count = weighted_choice(
            WAREHOUSE_DISTRIBUTION
        )

        # ---------------------------------------------
        # Select unique warehouses
        # ---------------------------------------------

        selected = warehouses.sample(
            n=min(warehouse_count, len(warehouses)),
            replace=False
        )

        priority = 1

        for _, warehouse in selected.iterrows():

            warehouse_id = int(
                warehouse["WarehouseID"]
            )

            stock = random.randint(
                10,
                500
            )

            reserved = random.randint(
                0,
                int(stock * 0.30)
            )

            available = stock - reserved

            reorder_level = random.randint(
                10,
                100
            )

            reorder_quantity = random.randint(
                50,
                500
            )

            last_restock = random_restock_date()

            inventory.append({

                "InventoryID": inventory_id,

                "ProductID": product_id,

                "WarehouseID": warehouse_id,
                "SafetyStock": int(reorder_level * 0.5),


                "StockQuantity": stock,

                "ReservedQuantity": reserved,

                

                "ReorderLevel": reorder_level,


                "LastRestocked": last_restock,

                "LastStockUpdated": last_restock,

                

            })

            inventory_id += 1
            priority += 1

        if product_id % 1000 == 0:

            print(

                f"{product_id:,} products processed..."

            )

    print("=" * 60)

    return pd.DataFrame(inventory)
# ==========================================================
# Validate Inventory
# ==========================================================

def validate_inventory(df):

    print("\n" + "=" * 60)
    print("Validating Inventory")
    print("=" * 60)

    # ------------------------------------------------------

    assert df["InventoryID"].is_unique, \
        "Duplicate InventoryID found."

    # ------------------------------------------------------

    duplicate = df.duplicated(
        subset=["ProductID", "WarehouseID"]
    ).sum()

    if duplicate > 0:

        raise ValueError(
            "Duplicate Product-Warehouse combination found."
        )

    # ------------------------------------------------------

    if df.isnull().sum().sum() > 0:

        raise ValueError(
            "Null values detected."
        )

    # ------------------------------------------------------



    # ------------------------------------------------------

    invalid = df[
        df["ReservedQuantity"]
        >
        df["StockQuantity"]
    ]

    if len(invalid) > 0:

        raise ValueError(
            "Reserved Quantity exceeds Stock Quantity."
        )

    print("✔ InventoryID Unique")
    print("✔ Product-Warehouse Unique")
    print("✔ No Null Values")
    print("✔ Stock Validation Passed")
    print("=" * 60)
    
# ==========================================================
# Export Inventory
# ==========================================================

def export_inventory(df):

    output = CSV_OUTPUT / "inventory.csv"

    output.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        output,
        index=False,
        encoding="utf-8"
    )

    print("\n" + "=" * 60)
    print("Inventory Exported Successfully")
    print("=" * 60)
    print(f"Rows   : {len(df):,}")
    print(f"Output : {output}")
    print("=" * 60)
    
# ==========================================================
# Summary
# ==========================================================

def print_summary(df):

    print("\n" + "=" * 60)
    print("Inventory Summary")
    print("=" * 60)

    print(f"Inventory Records : {len(df):,}")

    print()

    print("Average Stock")

    print(
        round(
            df["StockQuantity"].mean(),
            2
        )
    )

    print()

    print("Average Reserved")

    print(
        round(
            df["ReservedQuantity"].mean(),
            2
        )
    )

    print()

    print("Average Available")

    print("Average Stock")
    print(round(df["StockQuantity"].mean(), 2))

    print()

    print("Average Reserved")
    print(round(df["ReservedQuantity"].mean(), 2))

    print()

    print("Average Safety Stock")
    print(round(df["SafetyStock"].mean(), 2))

    print()

    print("Warehouses Per Product")

    warehouse_counts = (
        df.groupby("ProductID")
          .size()
          .value_counts()
          .sort_index()
    )

    print(warehouse_counts)

    print("=" * 60)
    
# ==========================================================
# Main
# ==========================================================

def main():

    print("\n")
    print("=" * 70)
    print("ShopSphere Analytics")
    print("Inventory Generator")
    print("=" * 70)

    inventory = generate_inventory()

    validate_inventory(inventory)

    export_inventory(inventory)

    print_summary(inventory)

    print("\nCompleted Successfully.")


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":

    main()
