"""
=========================================================
ShopSphere Analytics
brands_generator.py

Generates:
    reference_data/brands.csv
=========================================================
"""

import random
import pandas as pd

from config.config import REFERENCE_DATA

# ---------------------------------------------------------
# Brand Data
# ---------------------------------------------------------

BRANDS = {

    "Electronics": [

        "Samsung",
        "Apple",
        "Sony",
        "LG",
        "OnePlus",
        "Xiaomi",
        "Realme",
        "Lenovo",
        "Dell",
        "HP",
        "ASUS",
        "Boat",
        "JBL",
        "Canon",
        "Nikon",
        "Panasonic",
        "Acer",
        "Nothing",
        "Intel",
        "AMD"

    ],

    "Fashion":[

        "Nike",
        "Adidas",
        "Puma",
        "Levi's",
        "Allen Solly",
        "Van Heusen",
        "Louis Philippe",
        "Peter England",
        "U.S. Polo",
        "Roadster",
        "HRX",
        "Campus",
        "Bata",
        "Woodland",
        "Sparx"

    ],

    "Beauty":[

        "Lakme",
        "Maybelline",
        "L'Oreal",
        "Mamaearth",
        "Nivea",
        "Dove",
        "Ponds",
        "Biotique",
        "Minimalist",
        "Himalaya"

    ],

    "Home":[

        "Prestige",
        "Pigeon",
        "Milton",
        "Cello",
        "Wonderchef",
        "Hawkins",
        "Philips"

    ],

    "Sports":[

        "SG",
        "MRF",
        "Yonex",
        "Cosco",
        "Nivia",
        "Decathlon"

    ],

    "Books":[

        "Penguin",
        "HarperCollins",
        "McGraw Hill",
        "Oxford",
        "Pearson"

    ],

    "Automotive":[

        "Bosch",
        "Castrol",
        "Michelin",
        "MRF Tyres",
        "Exide"

    ]

}

# ---------------------------------------------------------
# Generic Brands
# ---------------------------------------------------------

for i in range(1,201):

    BRANDS.setdefault(
        "Generic",
        []
    ).append(

        f"ShopSphere Brand {i}"

    )

# ---------------------------------------------------------
# Generate CSV
# ---------------------------------------------------------

def generate_brands():

    rows=[]

    brand_id=1

    for category,brand_list in BRANDS.items():

        for brand in brand_list:

            rows.append({

                "BrandID":brand_id,

                "BrandName":brand,

                "Country":random.choice([

                    "India",

                    "USA",

                    "Japan",

                    "South Korea",

                    "China",

                    "Germany"

                ]),

                "Website":None,

                "IsActive":1

            })

            brand_id+=1

    df=pd.DataFrame(rows)

    output=REFERENCE_DATA/"brands.csv"

    df.to_csv(output,index=False)

    print("="*60)
    print("Brands Generated")
    print("="*60)
    print(df.shape)
    print(output)

    return df

if __name__=="__main__":

    generate_brands()