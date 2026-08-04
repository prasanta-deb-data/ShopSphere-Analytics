"""
=========================================================
ShopSphere Analytics

customer_address_generator.py

Generates:
    output/csv/customer_addresses.csv

Author : Prasanta Kumar Deb
=========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import random

from pathlib import Path

import pandas as pd

from config.config import (

    CSV_OUTPUT,

    REFERENCE_DATA,

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

PROGRESS_INTERVAL = 10000

MIN_ADDRESSES_PER_CUSTOMER = 1

MAX_ADDRESSES_PER_CUSTOMER = 4

# ==========================================================
# Load Master Data
# ==========================================================

def load_master_data():

    data = {

        "Customers": pd.read_csv(

            CSV_OUTPUT /

            "customers.csv"

        ),

        "Cities": pd.read_csv(

            REFERENCE_DATA /

            "cities.csv"

        )

    }

    return data

# ==========================================================
# Load Once
# ==========================================================

MASTER = load_master_data()

CUSTOMERS = MASTER["Customers"]

CITIES = MASTER["Cities"]

# ==========================================================
# Fast Lookups
# ==========================================================

CITY_LOOKUP = (

    CITIES

    .set_index(

        "CityID"

    )

    .to_dict(

        "index"

    )

)

# ==========================================================
# Validate Master Data
# ==========================================================

def validate_master_data():

    print("=" * 60)

    print(

        "Customer Address Generator Configuration"

    )

    print("=" * 60)

    if CUSTOMERS.empty:

        raise ValueError(

            "customers.csv is empty."

        )

    if CITIES.empty:

        raise ValueError(

            "cities.csv is empty."

        )

    print(

        f"Customers              : {len(CUSTOMERS):,}"

    )

    print(

        f"Cities                 : {len(CITIES):,}"

    )

    print(

        f"Min Addresses/Customer : {MIN_ADDRESSES_PER_CUSTOMER}"

    )

    print(

        f"Max Addresses/Customer : {MAX_ADDRESSES_PER_CUSTOMER}"

    )

    print("=" * 60)
# ==========================================================
# Address Count Distribution
# ==========================================================

ADDRESS_COUNT_DISTRIBUTION = {

    1: 60,

    2: 30,

    3: 8,

    4: 2

}

# ==========================================================
# Address Type Distribution
# ==========================================================

ADDRESS_TYPE_DISTRIBUTION = {

    "Home": 70,

    "Office": 20,

    "Other": 10

}

# ==========================================================
# House Number Prefixes
# ==========================================================

HOUSE_PREFIXES = [

    "House No.",

    "Flat",

    "Apartment",

    "Villa",

    "Plot No.",

    "Block",

    "Floor"

]

# ==========================================================
# Apartment / Building Names
# ==========================================================

BUILDING_NAMES = [

    "Green Residency",

    "Sunshine Heights",

    "Royal Enclave",

    "Silver Oak",

    "Lake View Residency",

    "Palm Residency",

    "Skyline Towers",

    "Harmony Apartments",

    "Orchid Residency",

    "Shanti Vihar",

    "Emerald Heights",

    "Golden Plaza",

    "Hill View",

    "Park Residency",

    "Crystal Tower",

    "Urban Nest",

    "Elite Residency",

    "Blue Pearl",

    "Galaxy Residency",

    "Maple Heights"

]

# ==========================================================
# Landmark List
# ==========================================================

LANDMARKS = [

    "Near Railway Station",

    "Near Bus Stand",

    "Near Metro Station",

    "Near Airport",

    "Near Market",

    "Near City Mall",

    "Opp City Hospital",

    "Opp Police Station",

    "Near Government School",

    "Near College",

    "Near Temple",

    "Near Mosque",

    "Near Church",

    "Near Petrol Pump",

    "Near Park",

    "Near Lake",

    "Near Stadium",

    "Behind Shopping Complex",

    "Near Post Office",

    "Near Bank"

]

# ==========================================================
# Street Names
# ==========================================================

STREET_NAMES = [

    "MG Road",

    "Station Road",

    "Main Road",

    "Park Street",

    "Lake Road",

    "College Road",

    "Temple Road",

    "Church Road",

    "Airport Road",

    "Market Road",

    "VIP Road",

    "Hill Road",

    "Forest Road",

    "Ring Road",

    "Central Avenue",

    "Gandhi Road",

    "Netaji Road",

    "Azad Road",

    "Nehru Road",

    "Shivaji Road"

]

# ==========================================================
# Country
# ==========================================================

COUNTRY = "India"

# ==========================================================
# Default Address Rule
# ==========================================================

EXACTLY_ONE_DEFAULT_ADDRESS = True
# ==========================================================
# Number of Addresses
# ==========================================================

def get_address_count():

    return random.choices(

        population=list(

            ADDRESS_COUNT_DISTRIBUTION.keys()

        ),

        weights=list(

            ADDRESS_COUNT_DISTRIBUTION.values()

        ),

        k=1

    )[0]


# ==========================================================
# Address Type
# ==========================================================

def get_address_type():

    return random.choices(

        population=list(

            ADDRESS_TYPE_DISTRIBUTION.keys()

        ),

        weights=list(

            ADDRESS_TYPE_DISTRIBUTION.values()

        ),

        k=1

    )[0]


# ==========================================================
# Address Line 1
# ==========================================================

def generate_address_line1():

    prefix = random.choice(

        HOUSE_PREFIXES

    )

    if prefix == "Flat":

        number = f"{random.randint(1,30)}{random.randint(1,20):02d}"

    elif prefix == "Apartment":

        number = f"{random.randint(1,20)}-{random.randint(1,15)}"

    elif prefix == "Floor":

        number = f"{random.randint(1,15)}"

    else:

        number = random.randint(

            1,

            999

        )

    return f"{prefix} {number}"


# ==========================================================
# Address Line 2
# ==========================================================

def generate_address_line2():

    building = random.choice(

        BUILDING_NAMES

    )

    street = random.choice(

        STREET_NAMES

    )

    return f"{building}, {street}"


# ==========================================================
# Landmark
# ==========================================================

def generate_landmark():

    return random.choice(

        LANDMARKS

    )


# ==========================================================
# City
# ==========================================================

def select_city():

    return random.choice(

        CITIES["CityID"].tolist()

    )


# ==========================================================
# Country
# ==========================================================

def get_country():

    return COUNTRY


# ==========================================================
# Default Address
# ==========================================================

def get_default_index(

    total_addresses

):

    return random.randint(

        0,

        total_addresses - 1

    )


# ==========================================================
# Progress Logger
# ==========================================================

def log_progress(

    customer_number,

    total_customers

):

    if customer_number % PROGRESS_INTERVAL == 0:

        print(

            f"{customer_number:,} / {total_customers:,} Customers Processed..."

        )
# ==========================================================
# Generate Customer Addresses
# ==========================================================

def generate_customer_addresses():

    print("=" * 60)
    print("Generating Customer Addresses")
    print("=" * 60)

    validate_master_data()

    rows = []

    address_id = 1

    total_customers = len(

        CUSTOMERS

    )

    # ------------------------------------------------------
    # Generate
    # ------------------------------------------------------

    for customer_number, customer in enumerate(

        CUSTOMERS.itertuples(index=False),

        start=1

    ):

        address_count = get_address_count()

        default_index = get_default_index(

            address_count

        )

        for index in range(

            address_count

        ):

            rows.append(

                {

                    "AddressID": address_id,

                    "CustomerID": int(

                        customer.CustomerID

                    ),

                    "AddressType": get_address_type(),

                    "AddressLine1": generate_address_line1(),

                    "AddressLine2": generate_address_line2(),

                    "Landmark": generate_landmark(),

                    "CityID": select_city(),

                    "Country": get_country(),

                    "IsDefault": 1 if index == default_index else 0

                }

            )

            address_id += 1

        log_progress(

            customer_number,

            total_customers

        )

    # ------------------------------------------------------
    # DataFrame
    # ------------------------------------------------------

    addresses = pd.DataFrame(

        rows,

        columns=[

            "AddressID",

            "CustomerID",

            "AddressType",

            "AddressLine1",

            "AddressLine2",

            "Landmark",

            "CityID",

            "Country",

            "IsDefault"

        ]

    )

    print()

    print("=" * 60)
    print("Customer Address Generation Completed")
    print("=" * 60)

    print(

        f"Customers : {total_customers:,}"

    )

    print(

        f"Addresses : {len(addresses):,}"

    )

    print("=" * 60)

    return addresses
# ==========================================================
# Validate Customer Addresses
# ==========================================================

def validate_customer_addresses(

    addresses

):

    print("=" * 60)

    print(

        "Validating Customer Addresses"

    )

    print("=" * 60)

    # ------------------------------------------------------
    # Dataset
    # ------------------------------------------------------

    if addresses.empty:

        raise ValueError(

            "Customer address dataset is empty."

        )

    print(

        "✓ Dataset Validation Passed"

    )

    # ------------------------------------------------------
    # AddressID
    # ------------------------------------------------------

    if addresses["AddressID"].duplicated().any():

        raise ValueError(

            "Duplicate AddressID found."

        )

    print(

        "✓ AddressID Validation Passed"

    )

    # ------------------------------------------------------
    # CustomerID
    # ------------------------------------------------------

    valid_customers = set(

        CUSTOMERS["CustomerID"]

    )

    invalid_customer = addresses.loc[

        ~addresses["CustomerID"].isin(

            valid_customers

        )

    ]

    if not invalid_customer.empty:

        raise ValueError(

            "Invalid CustomerID found."

        )

    print(

        "✓ Customer Validation Passed"

    )

    # ------------------------------------------------------
    # CityID
    # ------------------------------------------------------

    valid_cities = set(

        CITIES["CityID"]

    )

    invalid_city = addresses.loc[

        ~addresses["CityID"].isin(

            valid_cities

        )

    ]

    if not invalid_city.empty:

        raise ValueError(

            "Invalid CityID found."

        )

    print(

        "✓ City Validation Passed"

    )

    # ------------------------------------------------------
    # Address Type
    # ------------------------------------------------------

    valid_types = set(

        ADDRESS_TYPE_DISTRIBUTION.keys()

    )

    invalid_type = addresses.loc[

        ~addresses["AddressType"].isin(

            valid_types

        )

    ]

    if not invalid_type.empty:

        raise ValueError(

            "Invalid AddressType found."

        )

    print(

        "✓ Address Type Validation Passed"

    )

    # ------------------------------------------------------
    # Country
    # ------------------------------------------------------

    invalid_country = addresses.loc[

        addresses["Country"] != COUNTRY

    ]

    if not invalid_country.empty:

        raise ValueError(

            "Invalid Country found."

        )

    print(

        "✓ Country Validation Passed"

    )

    # ------------------------------------------------------
    # Default Address
    # ------------------------------------------------------

    default_count = (

        addresses

        .groupby(

            "CustomerID"

        )["IsDefault"]

        .sum()

    )

    invalid_default = default_count[

        default_count != 1

    ]

    if not invalid_default.empty:

        raise ValueError(

            "Each customer must have exactly one default address."

        )

    print(

        "✓ Default Address Validation Passed"

    )

    # ------------------------------------------------------
    # Mandatory Columns
    # ------------------------------------------------------

    required_columns = [

        "CustomerID",

        "AddressType",

        "AddressLine1",

        "CityID",

        "Country",

        "IsDefault"

    ]

    for column in required_columns:

        if addresses[

            column

        ].isnull().any():

            raise ValueError(

                f"{column} contains NULL values."

            )

    print(

        "✓ Required Column Validation Passed"

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

        f"Customers : {addresses['CustomerID'].nunique():,}"

    )

    print(

        f"Addresses : {len(addresses):,}"

    )

    print(

        f"Default Addresses : {addresses['IsDefault'].sum():,}"

    )

    print("=" * 60)

    return True
# ==========================================================
# Export CSV
# ==========================================================

def export_customer_addresses(

    addresses

):

    print("=" * 60)

    print(

        "Exporting Customer Addresses"

    )

    print("=" * 60)

    output_path = (

        CSV_OUTPUT /

        "customer_addresses.csv"

    )

    addresses.to_csv(

        output_path,

        index=False

    )

    print(

        f"✓ File Saved : {output_path}"

    )

    print(

        f"✓ Rows Exported : {len(addresses):,}"

    )

    print("=" * 60)

    return output_path


# ==========================================================
# Main
# ==========================================================

def main():

    print()

    print("=" * 60)
    print("SHOPSPHERE CUSTOMER ADDRESS GENERATOR")
    print("=" * 60)

    start_time = pd.Timestamp.now()

    # ------------------------------------------------------
    # Generate
    # ------------------------------------------------------

    addresses = generate_customer_addresses()

    # ------------------------------------------------------
    # Validate
    # ------------------------------------------------------

    validate_customer_addresses(

        addresses

    )

    # ------------------------------------------------------
    # Export
    # ------------------------------------------------------

    output_file = export_customer_addresses(

        addresses

    )

    # ------------------------------------------------------
    # Execution Summary
    # ------------------------------------------------------

    end_time = pd.Timestamp.now()

    print()

    print("=" * 60)
    print("CUSTOMER ADDRESS GENERATION COMPLETED")
    print("=" * 60)

    print(

        f"Customers Processed : {CUSTOMERS['CustomerID'].nunique():,}"

    )

    print(

        f"Addresses Generated : {len(addresses):,}"

    )

    print(

        f"Output File         : {output_file}"

    )

    print(

        f"Started At          : {start_time.strftime('%Y-%m-%d %H:%M:%S')}"

    )

    print(

        f"Completed At        : {end_time.strftime('%Y-%m-%d %H:%M:%S')}"

    )

    print(

        f"Duration            : {end_time - start_time}"

    )

    print("=" * 60)


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    main()