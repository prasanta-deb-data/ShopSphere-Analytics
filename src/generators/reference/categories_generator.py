"""
=========================================================
ShopSphere Analytics
categories_generator.py

Generates:
    reference_data/categories.csv
    reference_data/subcategories.csv

Author : Prasanta Kumar Deb
=========================================================
"""

import pandas as pd

from config.config import REFERENCE_DATA

# =========================================================
# Category -> SubCategory Mapping
# =========================================================

CATEGORY_DATA = {

    "Electronics": [
        "Mobiles",
        "Laptops",
        "Tablets",
        "Smart Watches",
        "Headphones",
        "Speakers",
        "Televisions",
        "Cameras"
    ],

    "Fashion": [
        "Men Clothing",
        "Women Clothing",
        "Kids Clothing",
        "Footwear",
        "Watches",
        "Handbags",
        "Sunglasses",
        "Ethnic Wear"
    ],

    "Home & Kitchen": [
        "Furniture",
        "Kitchen Appliances",
        "Cookware",
        "Home Decor",
        "Storage",
        "Lighting",
        "Beds",
        "Dining"
    ],

    "Beauty & Personal Care": [
        "Skincare",
        "Haircare",
        "Makeup",
        "Fragrances",
        "Personal Hygiene"
    ],

    "Grocery": [
        "Rice",
        "Pulses",
        "Cooking Oil",
        "Snacks",
        "Beverages",
        "Dry Fruits"
    ],

    "Books": [
        "Fiction",
        "Non Fiction",
        "Academic",
        "Children Books",
        "Comics"
    ],

    "Sports & Fitness": [
        "Cricket",
        "Football",
        "Gym Equipment",
        "Yoga",
        "Cycling"
    ],

    "Toys & Games": [
        "Educational Toys",
        "Board Games",
        "Action Figures",
        "Remote Control Toys",
        "Puzzles"
    ],

    "Automotive": [
        "Car Accessories",
        "Bike Accessories",
        "Car Care",
        "Helmets",
        "Tyres"
    ],

    "Baby Products": [
        "Diapers",
        "Baby Food",
        "Baby Clothing",
        "Baby Toys",
        "Baby Care"
    ],

    "Health": [
        "Vitamins",
        "Supplements",
        "Medical Devices",
        "Personal Care",
        "Health Drinks"
    ],

    "Jewellery": [
        "Gold",
        "Silver",
        "Diamond",
        "Fashion Jewellery",
        "Accessories"
    ],

    "Pet Supplies": [
        "Dog Food",
        "Cat Food",
        "Pet Toys",
        "Pet Grooming",
        "Pet Accessories"
    ],

    "Office Supplies": [
        "Stationery",
        "Printers",
        "Office Furniture",
        "Calculators",
        "Files & Folders"
    ],

    "Garden & Outdoor": [
        "Plants",
        "Seeds",
        "Gardening Tools",
        "Outdoor Furniture",
        "Watering Equipment"
    ]
}

# =========================================================
# Generate Categories
# =========================================================

def generate_categories():

    category_rows = []
    subcategory_rows = []

    category_id = 1
    subcategory_id = 1

    for category_name, subcategories in CATEGORY_DATA.items():

        category_rows.append({

            "CategoryID": category_id,
            "CategoryName": category_name,
            "Description": f"{category_name} Products",
            "IsActive": 1

        })

        for subcategory in subcategories:

            subcategory_rows.append({

                "SubCategoryID": subcategory_id,
                "CategoryID": category_id,
                "SubCategoryName": subcategory,
                "Description": f"{subcategory} under {category_name}",
                "IsActive": 1

            })

            subcategory_id += 1

        category_id += 1

    categories_df = pd.DataFrame(category_rows)

    subcategories_df = pd.DataFrame(subcategory_rows)

    categories_path = REFERENCE_DATA / "categories.csv"

    subcategories_path = REFERENCE_DATA / "subcategories.csv"

    categories_df.to_csv(categories_path, index=False)

    subcategories_df.to_csv(subcategories_path, index=False)

    print("=" * 60)
    print("Categories Generated Successfully")
    print("=" * 60)
    print(f"Categories    : {len(categories_df)}")
    print(f"SubCategories : {len(subcategories_df)}")
    print(f"Output        : {categories_path}")
    print(f"Output        : {subcategories_path}")
    print("=" * 60)

    return categories_df, subcategories_df


# =========================================================
# Main
# =========================================================

if __name__ == "__main__":
    generate_categories()