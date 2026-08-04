"""
=========================================================
ShopSphere Analytics
address_generator.py

Generates:
    output/csv/customer_addresses.csv
=========================================================
"""

import random
from datetime import timedelta

import pandas as pd

from config.config import (
    CSV_OUTPUT,
    REFERENCE_DATA,
    RANDOM_SEED
)

random.seed(RANDOM_SEED)

# ==========================================================
# Load Files
# ==========================================================

def load_data():

    customers = pd.read_csv(

        CSV_OUTPUT / "customers.csv"

    )

    cities = pd.read_csv(

        REFERENCE_DATA / "cities.csv"

    )

    return customers, cities

# ==========================================================
# Address Types
# ==========================================================

ADDRESS_TYPES = {

    "Home":0.70,

    "Office":0.20,

    "Other":0.10

}

# ==========================================================
# Address Count
# ==========================================================

ADDRESS_COUNT = {

    1:0.70,

    2:0.25,

    3:0.05

}

# ==========================================================
# Indian Street Names
# ==========================================================
STREETS = [

    "MG Road",

    "Station Road",

    "VIP Road",

    "GS Road",

    "Church Road",

    "College Road",

    "Main Road",

    "Lake View Road",

    "Park Street",

    "Hill Road",

    "Circular Road",

    "Airport Road",

    "Ring Road",

    "Market Road",

    "Temple Road"

]
# ==========================================================
# Localities
# ==========================================================
LOCALITIES = [

    "Green Residency",

    "Sunshine Apartment",

    "Shanti Nagar",

    "Lake View",

    "City Center",

    "New Colony",

    "Model Town",

    "Civil Lines",

    "Gandhi Nagar",

    "Ashok Nagar",

    "Housing Colony",

    "North Extension"

]

# ==========================================================
# Landmarks
# ==========================================================

LANDMARKS = [

    "Near Railway Station",

    "Near Bus Stand",

    "Near Hospital",

    "Near School",

    "Near Mall",

    "Near Airport",

    "Opposite Police Station",

    "Behind Market",

    "Near Petrol Pump",

    "Near Temple"

]

# ==========================================================
# Helper
# ==========================================================
def weighted_choice(mapping):

    return random.choices(

        list(mapping.keys()),

        weights=list(mapping.values()),

        k=1

    )[0]
    
# ==========================================================
# Generate Customer Addresses
# ==========================================================

def generate_addresses():

    customers, cities = load_data()

    addresses = []

    address_id = 1

    print("=" * 60)
    print("Generating Customer Addresses...")
    print("=" * 60)

    for _, customer in customers.iterrows():

        customer_id = customer["CustomerID"]

        registration_date = pd.to_datetime(
            customer["RegistrationDate"]
        )

        # ---------------------------------------------
        # Number of addresses
        # ---------------------------------------------

        address_count = weighted_choice(
            ADDRESS_COUNT
        )

        default_index = random.randint(
            1,
            address_count
        )

        for i in range(1, address_count + 1):

            city = cities.sample(1).iloc[0]

            created_at = registration_date

            updated_at = created_at + timedelta(

                days=random.randint(0, 365)

            )

            addresses.append({

                "AddressID": address_id,

                "CustomerID": customer_id,

                "AddressType": weighted_choice(
                    ADDRESS_TYPES
                ),

                "AddressLine1":

                    f"House No. {random.randint(1,999)}, "

                    f"{random.choice(STREETS)}",

                "AddressLine2":

                    random.choice(LOCALITIES),

                "Landmark":

                    random.choice(LANDMARKS),

                "CityID":

                    int(city["CityID"]),
                    
                "Country": "India",

                

                "IsDefault":

                    1 if i == default_index else 0,

               

                "CreatedAt":

                    created_at,

                "UpdatedAt":

                    updated_at

            })

            address_id += 1

        if customer_id % 10000 == 0:

            print(

                f"{customer_id:,} customers processed..."

            )

    print("=" * 60)

    df = pd.DataFrame(addresses)

    return df
# ==========================================================
# Validate Address Data
# ==========================================================

def validate_addresses(df):

    print("\n" + "=" * 60)
    print("Validating Address Data")
    print("=" * 60)

    # ------------------------------------------------------
    # AddressID Unique
    # ------------------------------------------------------

    assert df["AddressID"].is_unique, \
        "Duplicate AddressID found."

    # ------------------------------------------------------
    # No Null Values
    # ------------------------------------------------------

    if df.isnull().sum().sum() > 0:
        raise ValueError("Null values detected.")

    # ------------------------------------------------------
    # Exactly One Default Address Per Customer
    # ------------------------------------------------------

    default_counts = (
        df.groupby("CustomerID")["IsDefault"]
          .sum()
    )

    invalid = default_counts[default_counts != 1]

    if not invalid.empty:
        raise ValueError(
            "Some customers do not have exactly one default address."
        )

    print("✔ AddressID Unique")
    print("✔ No Null Values")
    print("✔ One Default Address Per Customer")
    print("=" * 60)
    
# ==========================================================
# Export CSV
# ==========================================================

def export_addresses(df):

    output_file = CSV_OUTPUT / "customer_addresses.csv"

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8"
    )

    print("\n" + "=" * 60)
    print("Customer Addresses Exported Successfully")
    print("=" * 60)
    print(f"Rows   : {len(df):,}")
    print(f"Output : {output_file}")
    print("=" * 60)
    
# ==========================================================
# Summary
# ==========================================================

def print_summary(df):

    print("\n" + "=" * 60)
    print("Customer Address Summary")
    print("=" * 60)

    print(f"Total Addresses : {len(df):,}")
    print()

    print("Address Types")
    print(df["AddressType"].value_counts())
    print()

    print("Default Addresses")
    print(df["IsDefault"].value_counts())
    print()

    addresses_per_customer = (
        df.groupby("CustomerID")
          .size()
    )

    print("Addresses Per Customer")
    print(addresses_per_customer.value_counts().sort_index())

    print("=" * 60)
# ==========================================================
# Main
# ==========================================================

def main():

    print("\n")
    print("=" * 70)
    print("ShopSphere Analytics")
    print("Customer Address Generator")
    print("=" * 70)

    addresses = generate_addresses()

    validate_addresses(addresses)

    export_addresses(addresses)

    print_summary(addresses)

    print("\nCompleted Successfully.")


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":

    main()
    


