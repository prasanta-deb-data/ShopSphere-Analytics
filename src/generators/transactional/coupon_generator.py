"""
=========================================================
ShopSphere Analytics

coupon_generator.py

Generates:
    output/csv/coupons.csv

Author : Prasanta Kumar Deb
=========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import random

from datetime import (

    datetime,

    timedelta

)

import pandas as pd

from config.config import (

    CSV_OUTPUT,

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

NUM_COUPONS = 250

START_DATE = datetime(

    2023,

    1,

    1

)

END_DATE = datetime(

    2025,

    12,

    31

)

PROGRESS_INTERVAL = 50

# ==========================================================
# Used Coupon Codes
# ==========================================================

USED_COUPON_CODES = set()

# ==========================================================
# Validate Configuration
# ==========================================================

def validate_configuration():

    print("=" * 60)

    print(

        "Coupon Generator Configuration"

    )

    print("=" * 60)

    if NUM_COUPONS <= 0:

        raise ValueError(

            "NUM_COUPONS must be greater than zero."

        )

    if START_DATE >= END_DATE:

        raise ValueError(

            "START_DATE must be earlier than END_DATE."

        )

    print(

        f"Coupons          : {NUM_COUPONS:,}"

    )

    print(

        f"Start Date       : {START_DATE.date()}"

    )

    print(

        f"End Date         : {END_DATE.date()}"

    )

    print(

        f"Progress Interval: {PROGRESS_INTERVAL}"

    )

    print("=" * 60)
# ==========================================================
# Coupon Prefixes
# ==========================================================

COUPON_PREFIXES = [

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
# Coupon Descriptions
# ==========================================================

COUPON_DESCRIPTIONS = {

    "WELCOME": "Welcome Offer",

    "SAVE": "Savings Promotion",

    "FIRST": "First Purchase Offer",

    "SUPER": "Super Saver Offer",

    "MEGA": "Mega Sale Promotion",

    "SHOP": "Shopping Discount",

    "BIG": "Big Savings Campaign",

    "DIWALI": "Diwali Festival Sale",

    "HOLI": "Holi Festival Offer",

    "FESTIVE": "Festive Season Discount",

    "SUMMER": "Summer Sale",

    "WINTER": "Winter Sale",

    "FLASH": "Flash Sale",

    "EXTRA": "Extra Discount",

    "VIP": "VIP Exclusive Offer",

    "NEWUSER": "New Customer Offer",

    "SPECIAL": "Special Promotion",

    "REWARD": "Reward Program Offer",

    "BONUS": "Bonus Savings",

    "FREESHIP": "Free Shipping Promotion"

}

# ==========================================================
# Discount Types
# ==========================================================

DISCOUNT_TYPES = [

    "Flat",

    "Percentage"

]

# ==========================================================
# Flat Discount Values
# ==========================================================

FLAT_DISCOUNTS = [

    50,

    100,

    150,

    200,

    250,

    500,

    750,

    1000

]

# ==========================================================
# Percentage Discount Values
# ==========================================================

PERCENTAGE_DISCOUNTS = [

    5,

    10,

    15,

    20,

    25,

    30,

    40,

    50

]

# ==========================================================
# Maximum Discount Values
# ==========================================================

MAXIMUM_DISCOUNTS = [

    250,

    500,

    750,

    1000,

    1500,

    2000

]

# ==========================================================
# Minimum Order Values
# ==========================================================

MINIMUM_ORDER_VALUES = [

    499,

    999,

    1499,

    1999,

    2499,

    4999

]

# ==========================================================
# Usage Limits
# ==========================================================

USAGE_LIMITS = [

    100,

    500,

    1000,

    5000,

    10000

]

# ==========================================================
# Coupon Validity
# ==========================================================

MIN_VALIDITY_DAYS = 30

MAX_VALIDITY_DAYS = 180

# ==========================================================
# Active Coupon Probability
# ==========================================================

ACTIVE_COUPON_PERCENTAGE = 80
# ==========================================================
# Generate Coupon Code
# ==========================================================

def generate_coupon_code():

    while True:

        prefix = random.choice(

            COUPON_PREFIXES

        )

        code = (

            prefix +

            str(

                random.randint(

                    10,

                    999

                )

            )

        )

        if code not in USED_COUPON_CODES:

            USED_COUPON_CODES.add(

                code

            )

            return code


# ==========================================================
# Coupon Description
# ==========================================================

def generate_coupon_description(

    coupon_code

):

    prefix = "".join(

        [

            character

            for character in coupon_code

            if character.isalpha()

        ]

    )

    return COUPON_DESCRIPTIONS[

        prefix

    ]


# ==========================================================
# Discount Type
# ==========================================================

def get_discount_type():

    return random.choice(

        DISCOUNT_TYPES

    )


# ==========================================================
# Discount Values
# ==========================================================

def generate_discount(

    discount_type

):

    if discount_type == "Flat":

        value = random.choice(

            FLAT_DISCOUNTS

        )

        maximum = value

    else:

        value = random.choice(

            PERCENTAGE_DISCOUNTS

        )

        maximum = random.choice(

            MAXIMUM_DISCOUNTS

        )

    return value, maximum


# ==========================================================
# Minimum Order Value
# ==========================================================

def generate_minimum_order_value():

    return random.choice(

        MINIMUM_ORDER_VALUES

    )


# ==========================================================
# Coupon Dates
# ==========================================================

def generate_coupon_dates():

    total_days = (

        END_DATE -

        START_DATE

    ).days

    start_date = (

        START_DATE +

        timedelta(

            days=random.randint(

                0,

                total_days

            )

        )

    )

    validity = random.randint(

        MIN_VALIDITY_DAYS,

        MAX_VALIDITY_DAYS

    )

    end_date = (

        start_date +

        timedelta(

            days=validity

        )

    )

    return start_date, end_date


# ==========================================================
# Usage
# ==========================================================

def generate_usage():

    usage_limit = random.choice(

        USAGE_LIMITS

    )

    used_count = random.randint(

        0,

        usage_limit

    )

    return usage_limit, used_count


# ==========================================================
# Active Status
# ==========================================================

def generate_is_active(

    start_date,

    end_date

):

    today = datetime.today()

    if end_date < today:

        return 0

    if start_date > today:

        return 0

    return (

        1

        if random.randint(

            1,

            100

        ) <= ACTIVE_COUPON_PERCENTAGE

        else 0

    )


# ==========================================================
# Progress Logger
# ==========================================================

def log_progress(

    coupon_id

):

    if coupon_id % PROGRESS_INTERVAL == 0:

        print(

            f"{coupon_id:,} Coupons Generated..."

        )
# ==========================================================
# Generate Coupons
# ==========================================================

def generate_coupons():

    print("=" * 60)

    print(

        "Generating Coupons"

    )

    print("=" * 60)

    validate_configuration()

    coupons = []

    today = datetime.today()

    # ------------------------------------------------------
    # Generate
    # ------------------------------------------------------

    for coupon_id in range(

        1,

        NUM_COUPONS + 1

    ):

        coupon_code = generate_coupon_code()

        coupon_description = generate_coupon_description(

            coupon_code

        )

        discount_type = get_discount_type()

        discount_value, maximum_discount = generate_discount(

            discount_type

        )

        minimum_order_value = generate_minimum_order_value()

        start_date, end_date = generate_coupon_dates()

        usage_limit, used_count = generate_usage()

        is_active = generate_is_active(

            start_date,

            end_date

        )

        coupons.append(

            {

                "CouponID": coupon_id,

                "CouponCode": coupon_code,

                "CouponDescription": coupon_description,

                "DiscountType": discount_type,

                "DiscountValue": discount_value,

                "MinimumOrderValue": minimum_order_value,

                "MaximumDiscount": maximum_discount,

                "StartDate": start_date.date(),

                "EndDate": end_date.date(),

                "UsageLimit": usage_limit,

                "UsedCount": used_count,

                "IsActive": is_active

            }

        )

        log_progress(

            coupon_id

        )

    # ------------------------------------------------------
    # DataFrame
    # ------------------------------------------------------

    coupons = pd.DataFrame(

        coupons,

        columns=[

            "CouponID",

            "CouponCode",

            "CouponDescription",

            "DiscountType",

            "DiscountValue",

            "MinimumOrderValue",

            "MaximumDiscount",

            "StartDate",

            "EndDate",

            "UsageLimit",

            "UsedCount",

            "IsActive"

        ]

    )

    print()

    print("=" * 60)

    print(

        "Coupon Generation Completed"

    )

    print("=" * 60)

    print(

        f"Coupons Generated : {len(coupons):,}"

    )

    print()

    print(

        "Discount Type Distribution"

    )

    print(

        coupons["DiscountType"]

        .value_counts()

    )

    print()

    print(

        "Active Coupons"

    )

    print(

        coupons["IsActive"]

        .value_counts()

    )

    print("=" * 60)

    return coupons
# ==========================================================
# Validate Coupons
# ==========================================================

def validate_coupons(

    coupons

):

    print("=" * 60)

    print(

        "Validating Coupons"

    )

    print("=" * 60)

    # ------------------------------------------------------
    # Dataset
    # ------------------------------------------------------

    if coupons.empty:

        raise ValueError(

            "Coupon dataset is empty."

        )

    print(

        "✓ Dataset Validation Passed"

    )

    # ------------------------------------------------------
    # CouponID
    # ------------------------------------------------------

    if coupons["CouponID"].duplicated().any():

        raise ValueError(

            "Duplicate CouponID found."

        )

    print(

        "✓ CouponID Validation Passed"

    )

    # ------------------------------------------------------
    # CouponCode
    # ------------------------------------------------------

    if coupons["CouponCode"].duplicated().any():

        raise ValueError(

            "Duplicate CouponCode found."

        )

    print(

        "✓ CouponCode Validation Passed"

    )

    # ------------------------------------------------------
    # Required Columns
    # ------------------------------------------------------

    required_columns = [

        "CouponCode",

        "CouponDescription",

        "DiscountType",

        "DiscountValue",

        "MinimumOrderValue",

        "MaximumDiscount",

        "StartDate",

        "EndDate",

        "UsageLimit",

        "UsedCount",

        "IsActive"

    ]

    for column in required_columns:

        if coupons[

            column

        ].isnull().any():

            raise ValueError(

                f"{column} contains NULL values."

            )

    print(

        "✓ Required Column Validation Passed"

    )

    # ------------------------------------------------------
    # Discount Type
    # ------------------------------------------------------

    valid_types = set(

        DISCOUNT_TYPES

    )

    invalid = coupons.loc[

        ~coupons["DiscountType"].isin(

            valid_types

        )

    ]

    if not invalid.empty:

        raise ValueError(

            "Invalid DiscountType found."

        )

    print(

        "✓ Discount Type Validation Passed"

    )

    # ------------------------------------------------------
    # Discount Values
    # ------------------------------------------------------

    if (

        coupons["DiscountValue"] <= 0

    ).any():

        raise ValueError(

            "Invalid DiscountValue."

        )

    if (

        coupons["MinimumOrderValue"] <= 0

    ).any():

        raise ValueError(

            "Invalid MinimumOrderValue."

        )

    if (

        coupons["MaximumDiscount"] <= 0

    ).any():

        raise ValueError(

            "Invalid MaximumDiscount."

        )

    print(

        "✓ Discount Validation Passed"

    )

    # ------------------------------------------------------
    # Dates
    # ------------------------------------------------------

    coupons["StartDate"] = pd.to_datetime(

        coupons["StartDate"]

    )

    coupons["EndDate"] = pd.to_datetime(

        coupons["EndDate"]

    )

    invalid = coupons.loc[

        coupons["StartDate"] >=

        coupons["EndDate"]

    ]

    if not invalid.empty:

        raise ValueError(

            "Invalid coupon dates."

        )

    print(

        "✓ Date Validation Passed"

    )

    # ------------------------------------------------------
    # Usage
    # ------------------------------------------------------

    invalid = coupons.loc[

        coupons["UsedCount"] >

        coupons["UsageLimit"]

    ]

    if not invalid.empty:

        raise ValueError(

            "UsedCount exceeds UsageLimit."

        )

    print(

        "✓ Usage Validation Passed"

    )

    # ------------------------------------------------------
    # Coupon Description
    # ------------------------------------------------------

    for row in coupons.itertuples(index=False):

        prefix = "".join(

            [

                character

                for character in row.CouponCode

                if character.isalpha()

            ]

        )

        expected = COUPON_DESCRIPTIONS[

            prefix

        ]

        if row.CouponDescription != expected:

            raise ValueError(

                f"Invalid description for {row.CouponCode}"

            )

    print(

        "✓ Coupon Description Validation Passed"

    )

    # ------------------------------------------------------
    # Active Status
    # ------------------------------------------------------

    invalid = coupons.loc[

        ~coupons["IsActive"].isin(

            [0, 1]

        )

    ]

    if not invalid.empty:

        raise ValueError(

            "Invalid IsActive value."

        )

    print(

        "✓ Active Status Validation Passed"

    )

    # ------------------------------------------------------
    # Summary
    # ------------------------------------------------------

    print("=" * 60)

    print(

        "ALL VALIDATIONS PASSED"

    )

    print("=" * 60)

    print(

        f"Coupons        : {len(coupons):,}"

    )

    print(

        f"Active Coupons : {coupons['IsActive'].sum():,}"

    )

    print(

        f"Flat Discounts : {(coupons['DiscountType']=='Flat').sum():,}"

    )

    print(

        f"Percentage     : {(coupons['DiscountType']=='Percentage').sum():,}"

    )

    print("=" * 60)

    return True
# ==========================================================
# Export Coupons
# ==========================================================

def export_coupons(

    coupons

):

    print("=" * 60)

    print(

        "Exporting Coupons"

    )

    print("=" * 60)

    output_file = (

        CSV_OUTPUT /

        "coupons.csv"

    )

    output_file.parent.mkdir(

        parents=True,

        exist_ok=True

    )

    coupons.to_csv(

        output_file,

        index=False

    )

    print(

        f"✓ File Saved : {output_file}"

    )

    print(

        f"✓ Rows Exported : {len(coupons):,}"

    )

    print("=" * 60)

    return output_file


# ==========================================================
# Main
# ==========================================================

def main():

    print()

    print("=" * 70)

    print("SHOPSPHERE ANALYTICS")

    print("COUPON GENERATOR")

    print("=" * 70)

    start_time = datetime.now()

    # ------------------------------------------------------
    # Generate
    # ------------------------------------------------------

    coupons = generate_coupons()

    # ------------------------------------------------------
    # Validate
    # ------------------------------------------------------

    validate_coupons(

        coupons

    )

    # ------------------------------------------------------
    # Export
    # ------------------------------------------------------

    output_file = export_coupons(

        coupons

    )

    # ------------------------------------------------------
    # Execution Summary
    # ------------------------------------------------------

    end_time = datetime.now()

    duration = end_time - start_time

    print()

    print("=" * 70)

    print(

        "COUPON GENERATION COMPLETED"

    )

    print("=" * 70)

    print(

        f"Coupons Generated : {len(coupons):,}"

    )

    print(

        f"Active Coupons    : {coupons['IsActive'].sum():,}"

    )

    print(

        f"Inactive Coupons  : {(coupons['IsActive'] == 0).sum():,}"

    )

    print(

        f"Flat Coupons      : {(coupons['DiscountType'] == 'Flat').sum():,}"

    )

    print(

        f"Percentage Coupons: {(coupons['DiscountType'] == 'Percentage').sum():,}"

    )

    print(

        f"Output File       : {output_file}"

    )

    print(

        f"Started At        : {start_time.strftime('%Y-%m-%d %H:%M:%S')}"

    )

    print(

        f"Completed At      : {end_time.strftime('%Y-%m-%d %H:%M:%S')}"

    )

    print(

        f"Duration          : {duration}"

    )

    print("=" * 70)

    print()

    print(

        "Coupon Generator Finished Successfully."

    )


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    main()
    