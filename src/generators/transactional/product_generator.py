"""
=========================================================
ShopSphere Analytics
product_generator.py

Generates:
    output/csv/products.csv
=========================================================
"""

import random
import string
from datetime import datetime, timedelta

import pandas as pd

from config.config import (
    CSV_OUTPUT,
    REFERENCE_DATA,
    RANDOM_SEED
)

random.seed(RANDOM_SEED)

# ==========================================================
# Load Reference Files
# ==========================================================

def load_reference_data():

    categories = pd.read_csv(
        REFERENCE_DATA / "categories.csv"
    )

    subcategories = pd.read_csv(
        REFERENCE_DATA / "subcategories.csv"
    )

    brands = pd.read_csv(
        REFERENCE_DATA / "brands.csv"
    )

    suppliers = pd.read_csv(
        REFERENCE_DATA / "suppliers.csv"
    )

    return (
        categories,
        subcategories,
        brands,
        suppliers
    )
# ==========================================================
# Product Count
# ==========================================================
NUM_PRODUCTS = 15000

# ==========================================================
# Product Attributes
# ==========================================================
COLORS = [

    "Black",
    "White",
    "Blue",
    "Red",
    "Green",
    "Silver",
    "Gold",
    "Grey",
    "Pink",
    "Brown"

]

SIZES = [

    "XS",
    "S",
    "M",
    "L",
    "XL",
    "XXL"

]

STORAGE = [

    "64GB",
    "128GB",
    "256GB",
    "512GB"

]

RAM = [

    "4GB",
    "6GB",
    "8GB",
    "12GB",
    "16GB"

]

# ==========================================================
# Category Pricing Rules
# ==========================================================
CATEGORY_PRICE = {

    "Electronics": (500,120000),

    "Fashion": (300,8000),

    "Home & Kitchen": (200,35000),

    "Beauty & Personal Care": (100,3000),

    "Grocery": (20,2500),

    "Books": (150,2500),

    "Sports & Fitness": (300,50000),

    "Toys & Games": (100,10000),

    "Automotive": (500,75000),

    "Baby Products": (150,15000),

    "Health": (100,5000),

    "Jewellery": (1000,250000),

    "Pet Supplies": (100,8000),

    "Office Supplies": (50,20000),

    "Garden & Outdoor": (100,30000)

}

# ==========================================================
# GST Rules
# ==========================================================

GST = {

    "Electronics":18,

    "Fashion":12,

    "Home & Kitchen":18,

    "Beauty & Personal Care":18,

    "Grocery":5,

    "Books":0,

    "Sports & Fitness":18,

    "Toys & Games":12,

    "Automotive":28,

    "Baby Products":12,

    "Health":12,

    "Jewellery":3,

    "Pet Supplies":18,

    "Office Supplies":18,

    "Garden & Outdoor":18

}
# ==========================================================
# SKU Generator
# ==========================================================

def generate_sku(category, product_id):

    prefix = "".join(

        word[0]

        for word in category.split()

    ).upper()

    return f"{prefix}-{product_id:06d}"
# ==========================================================
# Launch Date
# ==========================================================

def random_launch_date():

    start = datetime(2022,1,1)

    end = datetime(2025,12,31)

    days = (end-start).days

    return start + timedelta(

        days=random.randint(0,days)

    )
# ==========================================================
# Product Name Generator
# ==========================================================

def generate_product_name(brand, category, subcategory):

    if category == "Electronics":

        if subcategory == "Mobiles":
            return f"{brand} Galaxy M{random.randint(10,60)} 5G {random.choice(RAM)} {random.choice(STORAGE)}"

        elif subcategory == "Laptops":
            return f"{brand} Pavilion {random.randint(13,17)} Ryzen {random.choice([5,7,9])}"

        elif subcategory == "Headphones":
            return f"{brand} Rockerz {random.randint(100,999)} Pro"

        elif subcategory == "Televisions":
            return f'{brand} Smart TV {random.choice([32,43,50,55,65])}"'

        else:
            return f"{brand} {subcategory}"

    elif category == "Fashion":

        return f"{brand} {subcategory} {random.choice(COLORS)}"

    elif category == "Books":

        titles = [

            "Complete SQL Guide",

            "Python Programming",

            "Data Analytics Handbook",

            "Power BI Mastery",

            "Machine Learning Basics",

            "Excel for Business",

            "Statistics Simplified"

        ]

        return random.choice(titles)

    elif category == "Grocery":

        return f"{brand} Premium {subcategory}"

    elif category == "Beauty & Personal Care":

        return f"{brand} {subcategory} Pack"

    elif category == "Sports & Fitness":

        return f"{brand} {subcategory}"

    elif category == "Home & Kitchen":

        return f"{brand} {subcategory}"

    else:

        return f"{brand} {subcategory}"
    
# ==========================================================
# Generate Products
# ==========================================================

def generate_products():

    (
        categories,
        subcategories,
        brands,
        suppliers
    ) = load_reference_data()

    products = []

    print("=" * 60)
    print("Generating Products...")
    print("=" * 60)

    for product_id in range(1, NUM_PRODUCTS + 1):

        category = categories.sample(1).iloc[0]

        category_id = category["CategoryID"]

        category_name = category["CategoryName"]

        sub_df = subcategories[

            subcategories["CategoryID"] == category_id

        ]

        subcategory = sub_df.sample(1).iloc[0]

        subcategory_id = subcategory["SubCategoryID"]

        subcategory_name = subcategory["SubCategoryName"]

        brand = brands.sample(1).iloc[0]

        supplier = suppliers.sample(1).iloc[0]

        brand_id = brand["BrandID"]

        supplier_id = supplier["SupplierID"]

        brand_name = brand["BrandName"]

        # ------------------------------------------------

        product_name = generate_product_name(

            brand_name,

            category_name,

            subcategory_name

        )

        # ------------------------------------------------

        min_price, max_price = CATEGORY_PRICE[

            category_name

        ]

        selling_price = random.randint(

            min_price,

            max_price

        )

        cost_price = round(

            selling_price * random.uniform(

                0.55,

                0.85

            ),

            2

        )

        mrp = round(

            selling_price * random.uniform(

                1.05,

                1.20

            ),

            2

        )

        rating = round(

            random.uniform(

                3.5,

                5.0

            ),

            1

        )

        review_count = random.randint(

            0,

            5000

        )

        launch_date = random_launch_date()

        warranty = random.choice(

            [0,6,12,24]

        )

        weight = round(

            random.uniform(

                0.10,

                20.00

            ),

            2

        )

        products.append({

            "ProductID": product_id,

            "SKU": generate_sku(

                category_name,

                product_id

            ),

            "ProductName": product_name,
            "ProductDescription":
               f"High quality {subcategory_name} from {brand_name}",

            "CategoryID": category_id,

            "SubCategoryID": subcategory_id,

            "BrandID": brand_id,

            "SupplierID": supplier_id,

            "CostPrice": cost_price,

            "SellingPrice": selling_price,

            "MRP": mrp,

           

            "Weight": weight,

            "Color": random.choice(

                COLORS

            ),
            "Size": random.choice(SIZES),

          

            

            

            "LaunchDate": launch_date,

            "IsActive": 1,

            "CreatedAt": launch_date,

            "UpdatedAt": launch_date

        })

        if product_id % 1000 == 0:

            print(

                f"{product_id:,} products generated..."

            )

    print("=" * 60)

    return pd.DataFrame(products)
# ==========================================================
# Validate Product Data
# ==========================================================

def validate_products(df):

    print("\n" + "=" * 60)
    print("Validating Product Data")
    print("=" * 60)

    assert df["ProductID"].is_unique, \
        "Duplicate ProductID found."

    assert df["SKU"].is_unique, \
        "Duplicate SKU found."

    if df.isnull().sum().sum() > 0:
        raise ValueError("Null values detected.")

    # ------------------------------------------------------

    invalid = df[df["CostPrice"] > df["SellingPrice"]]

    if len(invalid) > 0:

        raise ValueError(

            "Cost Price cannot exceed Selling Price."

        )

    # ------------------------------------------------------

    invalid = df[df["SellingPrice"] > df["MRP"]]

    if len(invalid) > 0:

        raise ValueError(

            "Selling Price cannot exceed MRP."

        )

    # ------------------------------------------------------

   

    print("✔ ProductID Unique")
    print("✔ SKU Unique")
    print("✔ No Null Values")
    print("✔ Pricing Validation Passed")
 

    print("=" * 60)
    
# ==========================================================
# Export CSV
# ==========================================================

def export_products(df):

    output = CSV_OUTPUT / "products.csv"

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
    print("Products Exported Successfully")
    print("=" * 60)
    print(f"Rows   : {len(df):,}")
    print(f"Output : {output}")
    print("=" * 60)
    
# ==========================================================
# Summary
# ==========================================================

def print_summary(df):

    print("\n" + "=" * 60)
    print("Product Summary")
    print("=" * 60)

    print(f"Products : {len(df):,}")

    print()

    print("Top Categories")

    print(

        df["CategoryID"]

        .value_counts()

        .sort_index()

    )

    print()

    print("Average Selling Price")

    print(

        round(

            df["SellingPrice"]

            .mean(),

            2

        )

    )

    print()

    print("Average Rating")

   

    print("=" * 60)
    
# ==========================================================
# Main
# ==========================================================

def main():

    print("\n")
    print("=" * 70)
    print("ShopSphere Analytics")
    print("Product Generator")
    print("=" * 70)

    products = generate_products()

    validate_products(products)

    export_products(products)

    print_summary(products)

    print("\nCompleted Successfully.")


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":

    main()
    
