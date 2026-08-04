"""
=========================================================
ShopSphere Analytics
cities_generator.py

Generates:
    reference_data/cities.csv

Author : Prasanta Kumar Deb
=========================================================
"""


import random
import pandas as pd

from config.config import (
    REFERENCE_DATA,
    RANDOM_SEED
)

random.seed(RANDOM_SEED)
# ==========================================================
# State PIN Code Range
# ==========================================================

STATE_PINCODE_RANGE = {

    "Andhra Pradesh": (515001, 535999),

    "Arunachal Pradesh": (790001, 792999),

    "Assam": (781001, 788999),

    "Bihar": (800001, 855999),

    "Chhattisgarh": (490001, 497999),

    "Goa": (403001, 403999),

    "Gujarat": (360001, 396999),

    "Haryana": (121001, 136999),

    "Himachal Pradesh": (171001, 177999),

    "Jharkhand": (814001, 835999),

    "Karnataka": (560001, 591999),

    "Kerala": (670001, 695999),

    "Madhya Pradesh": (450001, 488999),

    "Maharashtra": (400001, 444999),

    "Manipur": (795001, 795999),

    "Meghalaya": (793001, 794999),

    "Mizoram": (796001, 796999),

    "Nagaland": (797001, 798999),

    "Odisha": (751001, 770999),

    "Punjab": (140001, 160999),

    "Rajasthan": (301001, 345999),

    "Sikkim": (737001, 737999),

    "Tamil Nadu": (600001, 643999),

    "Telangana": (500001, 509999),

    "Tripura": (799001, 799999),

    "Uttar Pradesh": (201001, 285999),

    "Uttarakhand": (244001, 263999),

    "West Bengal": (700001, 743999),

    "Delhi": (110001, 110099),

    "Jammu and Kashmir": (180001, 194999),

    "Ladakh": (194101, 194999),

    "Chandigarh": (160001, 160999),

    "Puducherry": (605001, 609999),

    "Andaman and Nicobar Islands": (744101, 744999),

    "Dadra and Nagar Haveli and Daman and Diu": (396210, 396299),

    "Lakshadweep": (682551, 682559)

}

# ==========================================================
# Metro Cities
# ==========================================================

METRO_CITIES = {

    "Mumbai",

    "Delhi",

    "Bengaluru",

    "Kolkata",

    "Chennai",

    "Hyderabad",

    "Pune",

    "Ahmedabad"

}
# ---------------------------------------------------------
# State Name -> Major Cities
# (Expand this list over time)
# ---------------------------------------------------------

STATE_CITIES = {

    "Assam": [
        "Guwahati",
        "Silchar",
        "Dibrugarh",
        "Jorhat",
        "Tezpur",
        "Nagaon",
        "Tinsukia",
        "Bongaigaon",
        "Sivasagar",
        "Dhubri"
    ],

    "West Bengal": [
        "Kolkata",
        "Howrah",
        "Siliguri",
        "Asansol",
        "Durgapur",
        "Kharagpur",
        "Malda",
        "Haldia",
        "Bardhaman",
        "Darjeeling"
    ],

    "Maharashtra": [
        "Mumbai",
        "Pune",
        "Nagpur",
        "Nashik",
        "Aurangabad",
        "Kolhapur",
        "Solapur",
        "Thane",
        "Amravati",
        "Jalgaon"
    ],

    "Karnataka": [
        "Bengaluru",
        "Mysuru",
        "Hubli",
        "Belagavi",
        "Mangalore",
        "Shivamogga",
        "Tumakuru",
        "Ballari"
    ],

    "Tamil Nadu": [
        "Chennai",
        "Coimbatore",
        "Madurai",
        "Salem",
        "Tiruchirappalli",
        "Vellore",
        "Erode",
        "Thoothukudi"
    ],

    "Delhi": [
        "New Delhi"
    ]
}

# ==========================================================
# Load States
# ==========================================================

def load_states():

    states = pd.read_csv(

        REFERENCE_DATA / "states.csv"

    )

    return states
# ==========================================================
# Generate Pincode
# ==========================================================

def generate_pincode(state_name):

    start, end = STATE_PINCODE_RANGE.get(

        state_name,

        (100001, 999999)

    )

    return str(

        random.randint(

            start,

            end

        )

    )
    
# ==========================================================
# Generate Tier
# ==========================================================

def generate_tier(city):

    if city in METRO_CITIES:

        return "Tier 1"

    return random.choices(

        population=[

            "Tier 2",

            "Tier 3"

        ],

        weights=[

            0.55,

            0.45

        ],

        k=1

    )[0]
    
# ==========================================================
# Generate Cities
# ==========================================================

def generate_cities():

    print("=" * 60)
    print("Generating Cities...")
    print("=" * 60)

    states = load_states()

    rows = []

    city_id = 1

    for _, state in states.iterrows():

        state_id = state["StateID"]

        state_name = state["StateName"]

        cities = STATE_CITIES.get(

            state_name,

            []

        )

        for city in cities:

            rows.append({

                "CityID": city_id,

                "StateID": state_id,

                "CityName": city,

                "Pincode": generate_pincode(

                    state_name

                ),

                "Tier": generate_tier(

                    city

                ),

                "IsMetro": int(

                    city in METRO_CITIES

                ),

                "IsActive": 1

            })

            city_id += 1

    df = pd.DataFrame(rows)

    return df
# ==========================================================
# Validate Cities
# ==========================================================

def validate_cities(df):

    print("\n" + "=" * 60)
    print("Validating Cities")
    print("=" * 60)

    # ------------------------------------------------------

    assert df["CityID"].is_unique

    print("✔ CityID Unique")

    # ------------------------------------------------------

    if df.isnull().sum().sum() > 0:

        raise ValueError(
            "Null values found."
        )

    print("✔ No Null Values")

    # ------------------------------------------------------

    if len(df[df["Pincode"].str.len() != 6]):

        raise ValueError(
            "Invalid Pincode."
        )

    print("✔ Pincode Validation Passed")

    # ------------------------------------------------------

    if len(df[df["IsMetro"].isin([0, 1]) == False]):

        raise ValueError(
            "Invalid IsMetro value."
        )

    print("✔ Metro Validation Passed")

    # ------------------------------------------------------

    if len(df[df["IsActive"].isin([0, 1]) == False]):

        raise ValueError(
            "Invalid IsActive value."
        )

    print("✔ Active Flag Validation Passed")

    print("=" * 60)
# ==========================================================
# Export
# ==========================================================

def export_cities(df):

    output = REFERENCE_DATA / "cities.csv"

    df.to_csv(

        output,

        index=False

    )

    print("\n" + "=" * 60)
    print("Cities Exported Successfully")
    print("=" * 60)
    print(f"Rows   : {len(df):,}")
    print(f"Output : {output}")
# ==========================================================
# Summary
# ==========================================================

def print_summary(df):

    print("\n" + "=" * 60)
    print("Cities Summary")
    print("=" * 60)

    print(f"Total Cities : {len(df):,}")

    print()

    print("Metro Cities")

    print(

        df["IsMetro"].value_counts()

    )

    print()

    print("City Tier")

    print(

        df["Tier"].value_counts()

    )

    print("=" * 60)


# ==========================================================
# Main
# ==========================================================

def main():

    print("\n")
    print("=" * 70)
    print("ShopSphere Analytics")
    print("Cities Generator")
    print("=" * 70)

    cities = generate_cities()

    validate_cities(

        cities

    )

    export_cities(

        cities

    )

    print_summary(

        cities

    )

    print("\nCompleted Successfully.")


if __name__ == "__main__":

    main()