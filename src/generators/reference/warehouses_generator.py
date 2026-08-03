"""
=========================================================
ShopSphere Analytics
warehouses_generator.py

Generates:
    reference_data/warehouses.csv

Author : Prasanta Kumar Deb
=========================================================
"""

import random
import pandas as pd

from config.config import REFERENCE_DATA

# =========================================================
# Warehouse Names
# =========================================================

WAREHOUSE_NAMES = [

    "North Distribution Center",
    "South Distribution Center",
    "East Distribution Center",
    "West Distribution Center",
    "Central Distribution Center",

    "National Fulfillment Center",
    "Prime Fulfillment Center",
    "Express Fulfillment Center",

    "Regional Warehouse",
    "Smart Warehouse",

    "Mega Fulfillment Hub",
    "Metro Distribution Hub",
    "Urban Logistics Hub",
    "E-Commerce Hub",
    "Retail Fulfillment Hub"
]

# =========================================================
# Warehouse Managers
# =========================================================

MANAGERS = [

    "Rahul Sharma",
    "Amit Kumar",
    "Rakesh Gupta",
    "Sanjay Das",
    "Arun Singh",
    "Vivek Roy",
    "Ankit Verma",
    "Rohit Mishra",
    "Sourav Dutta",
    "Prakash Deb",
    "Deepak Jain",
    "Rajesh Yadav",
    "Neeraj Sharma",
    "Ajay Patel",
    "Manish Roy"

]

# =========================================================
# Load Cities
# =========================================================

cities = pd.read_csv(

    REFERENCE_DATA / "cities.csv"

)

# =========================================================
# Generate Warehouses
# =========================================================

def generate_warehouses(total=40):

    rows = []

    used_cities = set()

    warehouse_id = 1

    while warehouse_id <= total:

        city = cities.sample(1).iloc[0]

        if city.CityID in used_cities:
            continue

        used_cities.add(city.CityID)

        warehouse_name = (

            city.CityName

            + " "

            + random.choice(WAREHOUSE_NAMES)

        )

        rows.append({

            "WarehouseID": warehouse_id,

            "WarehouseName": warehouse_name,

            "CityID": city.CityID,

            "Capacity": random.randint(

                5000,

                50000

            ),

            "ManagerName": random.choice(

                MANAGERS

            ),

            "IsActive": 1

        })

        warehouse_id += 1

    df = pd.DataFrame(rows)

    output = REFERENCE_DATA / "warehouses.csv"

    df.to_csv(

        output,

        index=False

    )

    print("=" * 60)
    print("Warehouses Generated Successfully")
    print("=" * 60)
    print(f"Rows   : {len(df)}")
    print(f"Output : {output}")
    print("=" * 60)

    return df


# =========================================================
# Main
# =========================================================

if __name__ == "__main__":

    generate_warehouses()