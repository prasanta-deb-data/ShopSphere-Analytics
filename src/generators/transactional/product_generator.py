"""
=========================================================
ShopSphere Analytics

product_generator.py

Generates:
    output/csv/products.csv

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

random.seed(RANDOM_SEED)

# ==========================================================
# Generator Configuration
# ==========================================================

NUM_PRODUCTS = 300000

START_DATE = datetime(2022, 1, 1)

END_DATE = datetime(2025, 12, 31)

# ==========================================================
# Load Reference Tables
# ==========================================================

def load_reference_data():

    references = {

        "Categories": pd.read_csv(
            REFERENCE_DATA / "categories.csv"
        ),

        "SubCategories": pd.read_csv(
            REFERENCE_DATA / "subcategories.csv"
        ),

        "Brands": pd.read_csv(
            REFERENCE_DATA / "brands.csv"
        ),

        "Suppliers": pd.read_csv(
            REFERENCE_DATA / "suppliers.csv"
        )

    }

    return references


# ==========================================================
# Load Once
# ==========================================================

REFERENCE = load_reference_data()

CATEGORIES = REFERENCE["Categories"]

SUBCATEGORIES = REFERENCE["SubCategories"]

BRANDS = REFERENCE["Brands"]

SUPPLIERS = REFERENCE["Suppliers"]


# ==========================================================
# Category Price Rules
# (MRP Range)
# ==========================================================

CATEGORY_PRICE = {

    "Electronics": (5000, 150000),

    "Fashion": (300, 15000),

    "Home & Kitchen": (200, 50000),

    "Beauty & Personal Care": (100, 5000),

    "Grocery": (20, 3000),

    "Books": (100, 3000),

    "Sports & Fitness": (300, 75000),

    "Toys & Games": (100, 15000),

    "Automotive": (500, 100000),

    "Baby Products": (100, 20000),

    "Health": (100, 10000),

    "Jewellery": (1000, 500000),

    "Pet Supplies": (100, 10000),

    "Office Supplies": (100, 25000),

    "Garden & Outdoor": (100, 50000)

}

# ==========================================================
# Validate Reference Data
# ==========================================================

def validate_reference_data():

    print("=" * 60)
    print("Validating Reference Data")
    print("=" * 60)

    if CATEGORIES.empty:
        raise ValueError("Categories reference is empty.")

    if SUBCATEGORIES.empty:
        raise ValueError("SubCategories reference is empty.")

    if BRANDS.empty:
        raise ValueError("Brands reference is empty.")

    if SUPPLIERS.empty:
        raise ValueError("Suppliers reference is empty.")

    print(f"Categories     : {len(CATEGORIES)}")

    print(f"SubCategories  : {len(SUBCATEGORIES)}")

    print(f"Brands         : {len(BRANDS)}")

    print(f"Suppliers      : {len(SUPPLIERS)}")

    print("=" * 60)
# ==========================================================
# Category → Brand Mapping
# ==========================================================

CATEGORY_BRANDS = {

    "Electronics": [
        "Samsung", "Apple", "Sony", "LG", "OnePlus",
        "Xiaomi", "Dell", "HP", "Lenovo", "ASUS",
        "Acer", "Boat", "JBL", "Realme", "Nothing"
    ],

    "Fashion": [
        "Nike", "Adidas", "Puma", "Levi's",
        "Allen Solly", "Van Heusen", "US Polo",
        "Peter England", "H&M", "Zara"
    ],

    "Home & Kitchen": [
        "Prestige", "Pigeon", "Butterfly",
        "Milton", "Cello", "Philips",
        "Borosil", "Hawkins"
    ],

    "Beauty & Personal Care": [
        "Lakme", "L'Oreal", "Nivea",
        "Mamaearth", "Dove", "Ponds",
        "Himalaya", "Cetaphil"
    ],

    "Grocery": [
        "Aashirvaad", "Fortune", "Tata",
        "Nestle", "Amul", "Britannia",
        "Parle", "Sunfeast"
    ],

    "Books": [
        "Penguin",
        "McGraw Hill",
        "Pearson",
        "O'Reilly",
        "BPB"
    ],

    "Sports & Fitness": [
        "Nike", "Adidas", "Puma",
        "Cosco", "Yonex", "Nivia"
    ],

    "Toys & Games": [
        "Lego",
        "Funskool",
        "Mattel",
        "Hasbro"
    ],

    "Automotive": [
        "Bosch",
        "Castrol",
        "3M",
        "Shell"
    ],

    "Baby Products": [
        "Pampers",
        "Johnson's",
        "Huggies",
        "Mee Mee"
    ],

    "Health": [
        "Dr. Morepen",
        "Accu-Chek",
        "Omron",
        "Dettol"
    ],

    "Jewellery": [
        "Tanishq",
        "Kalyan",
        "Malabar"
    ],

    "Pet Supplies": [
        "Pedigree",
        "Drools",
        "Whiskas"
    ],

    "Office Supplies": [
        "Classmate",
        "Faber-Castell",
        "Camel",
        "Kangaro"
    ],

    "Garden & Outdoor": [
        "Ugaoo",
        "Bosch",
        "Falcon"
    ]

}

# ==========================================================
# Category Colors
# ==========================================================

CATEGORY_COLORS = {

    "Electronics": [
        "Black",
        "White",
        "Blue",
        "Silver",
        "Grey",
        "Gold"
    ],

    "Fashion": [
        "Black",
        "White",
        "Blue",
        "Red",
        "Green",
        "Pink",
        "Brown"
    ],

    "Home & Kitchen": [
        "Silver",
        "Black",
        "White",
        "Blue"
    ],

    "Beauty & Personal Care": [
        None
    ],

    "Grocery": [
        None
    ],

    "Books": [
        None
    ],

    "Sports & Fitness": [
        "Black",
        "Blue",
        "Red",
        "White"
    ],

    "Toys & Games": [
        "Red",
        "Blue",
        "Yellow",
        "Green"
    ],

    "Automotive": [
        "Black",
        "Grey",
        "Silver"
    ],

    "Baby Products": [
        "Pink",
        "Blue",
        "White"
    ],

    "Health": [
        None
    ],

    "Jewellery": [
        "Gold",
        "Silver",
        "Rose Gold"
    ],

    "Pet Supplies": [
        None
    ],

    "Office Supplies": [
        "Black",
        "Blue"
    ],

    "Garden & Outdoor": [
        "Green",
        "Black"
    ]

}

# ==========================================================
# Category Sizes
# ==========================================================

CATEGORY_SIZES = {

    "Fashion": [
        "XS",
        "S",
        "M",
        "L",
        "XL",
        "XXL"
    ],

    "Electronics": [
        None
    ],

    "Books": [
        None
    ],

    "Beauty & Personal Care": [
        None
    ],

    "Grocery": [
        None
    ],

    "Sports & Fitness": [
        "S",
        "M",
        "L",
        "XL"
    ],

    "Jewellery": [
        "6",
        "7",
        "8",
        "9"
    ],

    "Home & Kitchen": [
        None
    ],

    "Automotive": [
        None
    ],

    "Baby Products": [
        "Small",
        "Medium",
        "Large"
    ],

    "Health": [
        None
    ],

    "Pet Supplies": [
        None
    ],

    "Office Supplies": [
        None
    ],

    "Garden & Outdoor": [
        None
    ],

    "Toys & Games": [
        None
    ]

}

# ==========================================================
# Category Weight (Kg)
# ==========================================================

CATEGORY_WEIGHT = {

    "Electronics": (0.20, 8.00),

    "Fashion": (0.10, 2.00),

    "Home & Kitchen": (0.20, 25.00),

    "Beauty & Personal Care": (0.05, 1.00),

    "Grocery": (0.10, 10.00),

    "Books": (0.20, 2.00),

    "Sports & Fitness": (0.20, 40.00),

    "Toys & Games": (0.10, 8.00),

    "Automotive": (0.50, 40.00),

    "Baby Products": (0.10, 8.00),

    "Health": (0.05, 5.00),

    "Jewellery": (0.01, 0.50),

    "Pet Supplies": (0.10, 15.00),

    "Office Supplies": (0.05, 8.00),

    "Garden & Outdoor": (0.50, 35.00)

}
# ==========================================================
# Random Brand
# ==========================================================

def get_random_brand(category_name):

    allowed_brands = CATEGORY_BRANDS.get(

        category_name,

        []

    )

    brand_df = BRANDS[

        BRANDS["BrandName"].isin(

            allowed_brands

        )

    ]

    # Fallback if no matching brands exist
    if brand_df.empty:

        brand_df = BRANDS

    return brand_df.sample(

        1

    ).iloc[0]


# ==========================================================
# Random Supplier
# ==========================================================

def get_random_supplier():

    return SUPPLIERS.sample(

        1

    ).iloc[0]


# ==========================================================
# SKU Generator
# Example:
# ELE-000001
# FAS-000250
# ==========================================================

def generate_sku(

    category_name,

    product_id

):

    prefix = "".join(

        word[0]

        for word in category_name.split()

    ).upper()

    return f"{prefix}-{product_id:06d}"


# ==========================================================
# Random Launch Date
# ==========================================================

def random_launch_date():

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
# Pricing Engine
# ==========================================================

def generate_prices(

    category_name

):

    min_price, max_price = CATEGORY_PRICE[

        category_name

    ]

    selling_price = random.randint(

        min_price,

        max_price

    )

    cost_price = round(

        selling_price *

        random.uniform(

            0.55,

            0.85

        ),

        2

    )

    mrp = round(

        selling_price *

        random.uniform(

            1.05,

            1.20

        ),

        2

    )

    return (

        mrp,

        selling_price,

        cost_price

    )


# ==========================================================
# Product Attributes
# ==========================================================

def get_product_attributes(

    category_name

):

    colors = CATEGORY_COLORS.get(

        category_name,

        [None]

    )

    sizes = CATEGORY_SIZES.get(

        category_name,

        [None]

    )

    min_weight, max_weight = CATEGORY_WEIGHT.get(

        category_name,

        (0.10, 5.00)

    )

    return {

        "Color":

        random.choice(colors),

        "Size":

        random.choice(sizes),

        "Weight":

        round(

            random.uniform(

                min_weight,

                max_weight

            ),

            2

        )

    }


# ==========================================================
# Product Description
# ==========================================================

def generate_description(

    brand,

    subcategory

):

    return (

        f"{brand} {subcategory} manufactured "

        f"using high-quality materials "

        f"and designed for everyday use."

    )
# ==========================================================
# Product Models
# ==========================================================

PRODUCT_MODELS = {

    "Mobiles": [
        "Galaxy S25",
        "Galaxy A56",
        "Galaxy M35",
        "Galaxy F16",
        "iPhone 16",
        "iPhone 16 Pro",
        "Nord 5",
        "Nord CE 5",
        "Redmi Note 14",
        "Nothing Phone 3"
    ],

    "Laptops": [
        "Inspiron 15",
        "Pavilion 14",
        "IdeaPad Slim 5",
        "Vivobook 15",
        "MacBook Air M4",
        "ThinkPad E16",
        "Aspire 7"
    ],

    "Headphones": [
        "Buds Pro",
        "AirPods",
        "Neckband Pro",
        "Wireless Headset",
        "Noise Cancelling Headphones"
    ],

    "Televisions": [
        "Smart TV",
        "QLED TV",
        "OLED TV",
        "Android TV"
    ],

    "Shoes": [
        "Air Max",
        "Ultraboost",
        "Running Shoes",
        "Casual Sneakers",
        "Sports Shoes"
    ],

    "Shirts": [
        "Slim Fit Shirt",
        "Regular Fit Shirt",
        "Formal Shirt",
        "Casual Shirt"
    ],

    "Jeans": [
        "Slim Fit Jeans",
        "Regular Fit Jeans",
        "Stretch Jeans"
    ],

    "Books": [
        "Complete SQL Guide",
        "Python Programming",
        "Power BI Masterclass",
        "Excel for Business",
        "Machine Learning Basics",
        "Statistics for Data Analysis"
    ]

}

# ==========================================================
# Product Name Generator
# ==========================================================

def generate_product_name(

    brand_name,

    category_name,

    subcategory_name

):

    # ------------------------------------------------------
    # Electronics
    # ------------------------------------------------------

    if category_name == "Electronics":

        if subcategory_name == "Mobiles":

            return (

                f"{brand_name} "

                f"{random.choice(PRODUCT_MODELS['Mobiles'])} "

                f"{random.choice(['128GB','256GB','512GB'])}"

            )

        elif subcategory_name == "Laptops":

            return (

                f"{brand_name} "

                f"{random.choice(PRODUCT_MODELS['Laptops'])}"

            )

        elif subcategory_name == "Headphones":

            return (

                f"{brand_name} "

                f"{random.choice(PRODUCT_MODELS['Headphones'])}"

            )

        elif subcategory_name == "Televisions":

            return (

                f"{brand_name} "

                f"{random.choice([32,43,50,55,65])}"

                f" Inch "

                f"{random.choice(PRODUCT_MODELS['Televisions'])}"

            )

        else:

            return f"{brand_name} {subcategory_name}"

    # ------------------------------------------------------
    # Fashion
    # ------------------------------------------------------

    elif category_name == "Fashion":

        if subcategory_name == "Shoes":

            return (

                f"{brand_name} "

                f"{random.choice(PRODUCT_MODELS['Shoes'])}"

            )

        elif subcategory_name == "Shirts":

            return (

                f"{brand_name} "

                f"{random.choice(PRODUCT_MODELS['Shirts'])}"

            )

        elif subcategory_name == "Jeans":

            return (

                f"{brand_name} "

                f"{random.choice(PRODUCT_MODELS['Jeans'])}"

            )

        else:

            return f"{brand_name} {subcategory_name}"

    # ------------------------------------------------------
    # Books
    # ------------------------------------------------------

    elif category_name == "Books":

        return random.choice(

            PRODUCT_MODELS["Books"]

        )

    # ------------------------------------------------------
    # Grocery
    # ------------------------------------------------------

    elif category_name == "Grocery":

        return (

            f"{brand_name} Premium "

            f"{subcategory_name}"

        )

    # ------------------------------------------------------
    # Beauty
    # ------------------------------------------------------

    elif category_name == "Beauty & Personal Care":

        return (

            f"{brand_name} "

            f"{subcategory_name}"

        )

    # ------------------------------------------------------
    # Default
    # ------------------------------------------------------

    else:

        return (

            f"{brand_name} "

            f"{subcategory_name}"

        )
  # ==========================================================
# Generate Products
# ==========================================================

def generate_products():

    print("=" * 60)
    print("Generating Products")
    print("=" * 60)

    validate_reference_data()

    rows = []

    for product_id in range(1, NUM_PRODUCTS + 1):

        # ------------------------------------------
        # Category
        # ------------------------------------------

        category = CATEGORIES.sample(1).iloc[0]

        category_id = category["CategoryID"]

        category_name = category["CategoryName"]

        # ------------------------------------------
        # SubCategory
        # ------------------------------------------

        sub_df = SUBCATEGORIES[
            SUBCATEGORIES["CategoryID"] == category_id
        ]

        if sub_df.empty:
            continue

        subcategory = sub_df.sample(1).iloc[0]

        subcategory_id = subcategory["SubCategoryID"]

        subcategory_name = subcategory["SubCategoryName"]

        # ------------------------------------------
        # Brand
        # ------------------------------------------

        brand = get_random_brand(
            category_name
        )

        brand_id = brand["BrandID"]

        brand_name = brand["BrandName"]

        # ------------------------------------------
        # Supplier
        # ------------------------------------------

        supplier = get_random_supplier()

        supplier_id = supplier["SupplierID"]

        # ------------------------------------------
        # Product Name
        # ------------------------------------------

        product_name = generate_product_name(

            brand_name,

            category_name,

            subcategory_name

        )

        # ------------------------------------------
        # SKU
        # ------------------------------------------

        sku = generate_sku(

            category_name,

            product_id

        )

        # ------------------------------------------
        # Prices
        # ------------------------------------------

        mrp, selling_price, cost_price = generate_prices(

            category_name

        )

        # ------------------------------------------
        # Attributes
        # ------------------------------------------

        attributes = get_product_attributes(

            category_name

        )

        # ------------------------------------------
        # Description
        # ------------------------------------------

        description = generate_description(

            brand_name,

            subcategory_name

        )

        # ------------------------------------------
        # Launch Date
        # ------------------------------------------

        launch_date = random_launch_date()

        # ------------------------------------------
        # Active
        # ------------------------------------------

        is_active = random.choices(

            [1, 0],

            weights=[98, 2]

        )[0]

        # ------------------------------------------
        # Append
        # ------------------------------------------

        rows.append({

            "ProductID": product_id,

            "SKU": sku,

            "ProductName": product_name,

            "ProductDescription": description,

            "CategoryID": category_id,

            "SubCategoryID": subcategory_id,

            "BrandID": brand_id,

            "SupplierID": supplier_id,

            "MRP": mrp,

            "SellingPrice": selling_price,

            "CostPrice": cost_price,

            "Weight": attributes["Weight"],

            "Color": attributes["Color"],

            "Size": attributes["Size"],

            "LaunchDate": launch_date,

            "IsActive": is_active

        })

        # ------------------------------------------
        # Progress
        # ------------------------------------------

        if product_id % 10000 == 0:

            print(

                f"{product_id:,} Products Generated..."

            )

    products = pd.DataFrame(rows)

    print("=" * 60)
    print("Generation Completed")
    print("=" * 60)

    print(f"Rows : {len(products):,}")

    return products

# ==========================================================
# Validate Products
# ==========================================================

def validate_products(products):

    print("=" * 60)
    print("Validating Products")
    print("=" * 60)

    # ------------------------------------------------------
    # Empty Dataset
    # ------------------------------------------------------

    if products.empty:

        raise ValueError(
            "Generated products dataset is empty."
        )

    # ------------------------------------------------------
    # Duplicate ProductID
    # ------------------------------------------------------

    duplicate_ids = products["ProductID"].duplicated().sum()

    if duplicate_ids > 0:

        raise ValueError(
            f"Duplicate ProductID found : {duplicate_ids}"
        )

    print("✓ ProductID Validation Passed")

    # ------------------------------------------------------
    # Duplicate SKU
    # ------------------------------------------------------

    duplicate_sku = products["SKU"].duplicated().sum()

    if duplicate_sku > 0:

        raise ValueError(
            f"Duplicate SKU found : {duplicate_sku}"
        )

    print("✓ SKU Validation Passed")

    # ------------------------------------------------------
    # Product Name
    # ------------------------------------------------------

    if products["ProductName"].isnull().any():

        raise ValueError(
            "Null ProductName found."
        )

    print("✓ Product Name Validation Passed")

    # ------------------------------------------------------
    # Foreign Keys
    # ------------------------------------------------------

    fk_columns = [

        "CategoryID",
        "SubCategoryID",
        "BrandID",
        "SupplierID"

    ]

    for column in fk_columns:

        if products[column].isnull().any():

            raise ValueError(
                f"Null values found in {column}"
            )

    print("✓ Foreign Key Validation Passed")

    # ------------------------------------------------------
    # Price Validation
    # ------------------------------------------------------

    invalid_price = products[

        (products["CostPrice"] > products["SellingPrice"]) |

        (products["SellingPrice"] > products["MRP"])

    ]

    if len(invalid_price) > 0:

        raise ValueError(

            f"{len(invalid_price)} invalid price records found."

        )

    print("✓ Price Validation Passed")

    # ------------------------------------------------------
    # Weight
    # ------------------------------------------------------

    invalid_weight = products[

        products["Weight"] <= 0

    ]

    if len(invalid_weight) > 0:

        raise ValueError(

            f"{len(invalid_weight)} invalid weights found."

        )

    print("✓ Weight Validation Passed")

    # ------------------------------------------------------
    # Launch Date
    # ------------------------------------------------------

    invalid_date = products[

        products["LaunchDate"] >

        pd.Timestamp.today().date()

    ]

    if len(invalid_date) > 0:

        raise ValueError(

            f"{len(invalid_date)} future launch dates found."

        )

    print("✓ Launch Date Validation Passed")

    # ------------------------------------------------------
    # IsActive
    # ------------------------------------------------------

    invalid_active = products[

        ~products["IsActive"].isin([0, 1])

    ]

    if len(invalid_active) > 0:

        raise ValueError(

            f"{len(invalid_active)} invalid IsActive values."

        )

    print("✓ IsActive Validation Passed")

    # ------------------------------------------------------
    # Required Columns
    # ------------------------------------------------------

    required_columns = [

        "ProductID",
        "SKU",
        "ProductName",
        "CategoryID",
        "SubCategoryID",
        "BrandID",
        "SupplierID",
        "MRP",
        "SellingPrice",
        "CostPrice"

    ]

    for column in required_columns:

        if products[column].isnull().any():

            raise ValueError(

                f"Null values found in {column}"

            )

    print("✓ Required Column Validation Passed")

    # ------------------------------------------------------
    # Summary
    # ------------------------------------------------------

    print("=" * 60)
    print("ALL PRODUCT VALIDATIONS PASSED")
    print("=" * 60)

    print(f"Products : {len(products):,}")

    print(
        f"Categories : {products['CategoryID'].nunique()}"
    )

    print(
        f"SubCategories : {products['SubCategoryID'].nunique()}"
    )

    print(
        f"Brands : {products['BrandID'].nunique()}"
    )

    print(
        f"Suppliers : {products['SupplierID'].nunique()}"
    )

    print("=" * 60)

    return True
# ==========================================================
# Export Products
# ==========================================================

def export_products(products):

    print("=" * 60)
    print("Exporting Products")
    print("=" * 60)

    CSV_OUTPUT.mkdir(

        parents=True,

        exist_ok=True

    )

    output_file = (

        CSV_OUTPUT /

        "products.csv"

    )

    products.to_csv(

        output_file,

        index=False

    )

    print(f"SUCCESS : {len(products):,} products exported.")

    print(f"Location : {output_file}")

    return output_file


# ==========================================================
# Product Summary
# ==========================================================

def print_summary(products):

    print("\n" + "=" * 60)
    print("PRODUCT GENERATION SUMMARY")
    print("=" * 60)

    print(f"Total Products      : {len(products):,}")

    print(f"Categories          : {products['CategoryID'].nunique()}")

    print(f"SubCategories       : {products['SubCategoryID'].nunique()}")

    print(f"Brands              : {products['BrandID'].nunique()}")

    print(f"Suppliers           : {products['SupplierID'].nunique()}")

    print()

    print(f"Average MRP         : ₹{products['MRP'].mean():,.2f}")

    print(f"Average Selling     : ₹{products['SellingPrice'].mean():,.2f}")

    print(f"Average Cost        : ₹{products['CostPrice'].mean():,.2f}")

    print()

    print(f"Minimum Selling     : ₹{products['SellingPrice'].min():,.2f}")

    print(f"Maximum Selling     : ₹{products['SellingPrice'].max():,.2f}")

    print()

    print("Top Categories")

    print(

        products["CategoryID"]

        .value_counts()

        .head(10)

    )

    print("=" * 60)


# ==========================================================
# Main
# ==========================================================

def main():

    print("\n")
    print("=" * 60)
    print("SHOPSPHERE PRODUCT GENERATOR")
    print("=" * 60)

    products = generate_products()

    validate_products(products)

    export_products(products)

    print_summary(products)

    print("\nSUCCESS : Product generation completed successfully.")

    print("=" * 60)


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    main()
  