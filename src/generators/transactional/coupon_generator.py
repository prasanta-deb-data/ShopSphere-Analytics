"""
=========================================================
ShopSphere Analytics
coupon_generator.py

Generates:
    output/csv/coupons.csv

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
# Configuration
# ==========================================================

NUM_COUPONS = 200

START_DATE = datetime(2023,1,1)
END_DATE = datetime(2025,12,31)

# ==========================================================
# Coupon Prefixes
# ==========================================================
COUPON_PREFIX = [

    "WELCOME",
    "SAVE",
    "FIRST",
    "SUPER",
    "MEGA",
    "SHOP",
    "BIG",
    "DIWALI",
    "HOLI",
    "FESTIVE",
    "SUMMER",
    "WINTER",
    "FLASH",
    "EXTRA",
    "VIP",
    "NEWUSER",
    "SPECIAL",
    "REWARD",
    "BONUS",
    "FREESHIP"

]
# ==========================================================
# Discount Types
# ==========================================================
DISCOUNT_TYPES = [

    "Flat",

    "Percentage"

]
# ==========================================================
# Generate Coupon Code
# ==========================================================
used_codes = set()

def generate_coupon_code():

    while True:

        code = (

            random.choice(COUPON_PREFIX)

            +

            str(

                random.randint(

                    10,

                    999

                )

            )

        )

        if code not in used_codes:

            used_codes.add(code)

            return code
# ==========================================================
# Generate Coupons
# ==========================================================

def generate_coupons():

    coupons = []

    print("=" * 60)
    print("Generating Coupons...")
    print("=" * 60)

    for coupon_id in range(1, NUM_COUPONS + 1):

        discount_type = random.choice(DISCOUNT_TYPES)

        if discount_type == "Flat":

            discount_value = random.choice(
                [50, 100, 150, 200, 250, 500, 750, 1000]
            )

            max_discount = discount_value

        else:

            discount_value = random.choice(
                [5, 10, 15, 20, 25, 30, 40, 50]
            )

            max_discount = random.choice(
                [250, 500, 750, 1000, 1500, 2000]
            )

        start_date = START_DATE + timedelta(
            days=random.randint(0, 900)
        )

        end_date = start_date + timedelta(
            days=random.randint(30, 180)
        )

        usage_limit = random.choice(
            [100, 500, 1000, 5000, 10000]
        )

        used_count = random.randint(
            0,
            usage_limit
        )

        coupons.append({

            "CouponID": coupon_id,

            "CouponCode": generate_coupon_code(),

            "Description": "Marketing Promotion",

            "DiscountType": discount_type,

            "DiscountValue": discount_value,

            "MinimumOrderAmount": random.choice(
                [499, 999, 1499, 1999, 2499, 4999]
            ),

            "MaximumDiscount": max_discount,

            "StartDate": start_date,

            "EndDate": end_date,

            "UsageLimit": usage_limit,

            "UsedCount": used_count,

            "IsActive": random.choice([0, 1]),

            "CreatedAt": start_date,

            "UpdatedAt": end_date

        })

    return pd.DataFrame(coupons)
# ==========================================================
# Validate
# ==========================================================

def validate_coupons(df):

    print("\n" + "=" * 60)
    print("Validating Coupons")
    print("=" * 60)

    assert df["CouponID"].is_unique
    assert df["CouponCode"].is_unique

    if df.isnull().sum().sum() > 0:
        raise ValueError("Null values found.")

    invalid = df[df["StartDate"] >= df["EndDate"]]

    if len(invalid):

        raise ValueError("Invalid coupon dates.")

    invalid = df[df["UsedCount"] > df["UsageLimit"]]

    if len(invalid):

        raise ValueError("UsedCount exceeds UsageLimit.")

    print("✔ CouponID Unique")
    print("✔ CouponCode Unique")
    print("✔ Dates Valid")
    print("✔ Usage Valid")
    print("=" * 60)
    
# ==========================================================
# Export
# ==========================================================

def export_coupons(df):

    output = CSV_OUTPUT / "coupons.csv"

    output.parent.mkdir(

        parents=True,

        exist_ok=True

    )

    df.to_csv(

        output,

        index=False

    )

    print("\n" + "=" * 60)
    print("Coupons Exported Successfully")
    print("=" * 60)
    print(f"Rows   : {len(df):,}")
    print(f"Output : {output}")
# ==========================================================
# Summary
# ==========================================================

def print_summary(df):

    print("\n" + "=" * 60)
    print("Coupon Summary")
    print("=" * 60)

    print(df["DiscountType"].value_counts())

    print()

    print(df["IsActive"].value_counts())

    print("=" * 60)
# ==========================================================
# Main
# ==========================================================

def main():

    print("\n")
    print("=" * 70)
    print("ShopSphere Analytics")
    print("Coupon Generator")
    print("=" * 70)

    coupons = generate_coupons()

    validate_coupons(coupons)

    export_coupons(coupons)

    print_summary(coupons)

    print("\nCompleted Successfully.")


if __name__ == "__main__":

    main()
