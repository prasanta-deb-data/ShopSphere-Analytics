"""
=========================================================
ShopSphere Analytics

customer_generator.py

Generates:
    output/csv/customers.csv

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

NUM_CUSTOMERS = 100000

REGISTRATION_START = datetime(

    2022,

    1,

    1

)

REGISTRATION_END = datetime(

    2025,

    12,

    31

)

MIN_AGE = 18

MAX_AGE = 70

# ==========================================================
# Customer Configuration
# ==========================================================

REGISTRATION_SOURCES = [

    "Website",

    "Android App",

    "iOS App",

    "Referral",

    "Campaign"

]

CUSTOMER_SEGMENTS = [

    "New",

    "Regular",

    "Premium",

    "VIP"

]

EMAIL_DOMAINS = [

    "gmail.com",

    "outlook.com",

    "yahoo.com",

    "hotmail.com",

    "icloud.com"

]

# ==========================================================
# Gender Distribution
# ==========================================================

GENDER_DISTRIBUTION = {

    "Male": 52,

    "Female": 47,

    "Other": 1

}

# ==========================================================
# Progress Configuration
# ==========================================================

PROGRESS_INTERVAL = 10000

# ==========================================================
# Validation
# ==========================================================

def validate_configuration():

    print("=" * 60)

    print("Customer Generator Configuration")

    print("=" * 60)

    print(f"Customers            : {NUM_CUSTOMERS:,}")

    print(f"Registration Start   : {REGISTRATION_START.date()}")

    print(f"Registration End     : {REGISTRATION_END.date()}")

    print(f"Minimum Age          : {MIN_AGE}")

    print(f"Maximum Age          : {MAX_AGE}")

    print(f"Email Domains        : {len(EMAIL_DOMAINS)}")

    print(f"Customer Segments    : {len(CUSTOMER_SEGMENTS)}")

    print(f"Registration Sources : {len(REGISTRATION_SOURCES)}")

    print("=" * 60)
# ==========================================================
# Indian First Names
# ==========================================================

MALE_FIRST_NAMES = [

    "Aarav","Vivaan","Aditya","Arjun","Krishna",
    "Rahul","Rohit","Amit","Akash","Sourav",
    "Abhishek","Ankit","Ayush","Deepak","Karan",
    "Manish","Nikhil","Pankaj","Rajesh","Rakesh",
    "Sandeep","Shubham","Vikas","Vivek","Yash",
    "Prasanta","Rohan","Harsh","Mohit","Varun",
    "Nitin","Ashish","Sumit","Tarun","Anurag",
    "Gaurav","Sachin","Lokesh","Naveen","Ritesh"

]

FEMALE_FIRST_NAMES = [

    "Aadhya","Ananya","Diya","Ishita","Kiara",
    "Priya","Neha","Pooja","Sneha","Riya",
    "Anjali","Aarti","Kavya","Nisha","Payal",
    "Swati","Megha","Shreya","Komal","Nandini",
    "Rashmi","Ritika","Sakshi","Simran","Tanvi",
    "Vaishnavi","Muskan","Divya","Ankita","Preeti",
    "Jyoti","Shruti","Khushi","Rupal","Sonali",
    "Monika","Pallavi","Renu","Seema","Ayesha"

]

# ==========================================================
# Indian Last Names
# ==========================================================

LAST_NAMES = [

    "Sharma","Verma","Singh","Das","Deb",
    "Patel","Gupta","Yadav","Kumar","Roy",
    "Saha","Paul","Dutta","Choudhury","Ghosh",
    "Banerjee","Mukherjee","Chakraborty","Reddy",
    "Nair","Pillai","Joshi","Kulkarni","Bose",
    "Bhattacharya","Sarkar","Mishra","Tripathi",
    "Pandey","Agarwal","Jain","Malhotra",
    "Kapoor","Mehta","Thakur","Barman",
    "Saikia","Baruah","Hazarika","Bora"

]

# ==========================================================
# Registration Source Distribution
# ==========================================================

REGISTRATION_SOURCE_WEIGHTS = {

    "Website": 25,

    "Android App": 45,

    "iOS App": 15,

    "Referral": 10,

    "Campaign": 5

}

# ==========================================================
# Customer Segment Distribution
# ==========================================================

CUSTOMER_SEGMENT_WEIGHTS = {

    "New": 35,

    "Regular": 40,

    "Premium": 20,

    "VIP": 5

}

# ==========================================================
# Loyalty Points
# ==========================================================

LOYALTY_POINTS = {

    "New": (0, 500),

    "Regular": (500, 3000),

    "Premium": (3000, 15000),

    "VIP": (15000, 100000)

}

# ==========================================================
# Indian Mobile Prefixes
# ==========================================================

PHONE_PREFIXES = [

    "98","99","97","96","95",

    "94","93","92","91","90",

    "89","88","87","86","85",

    "84","83","82","81","80",

    "79","78","77","76","75",

    "74","73","72","71","70"

]

# ==========================================================
# Email Username Patterns
# ==========================================================

EMAIL_PATTERNS = [

    "{first}.{last}",

    "{first}{last}",

    "{first}_{last}",

    "{first}{number}",

    "{first}.{number}",

    "{first}{last}{number}"

]

# ==========================================================
# Active Customer Distribution
# ==========================================================

ACTIVE_WEIGHTS = {

    1: 96,

    0: 4

}
# ==========================================================
# Generate Gender
# ==========================================================

def generate_gender():

    return random.choices(

        population=list(GENDER_DISTRIBUTION.keys()),

        weights=list(GENDER_DISTRIBUTION.values()),

        k=1

    )[0]


# ==========================================================
# Generate Name
# ==========================================================

def generate_name(gender):

    if gender == "Male":

        first_name = random.choice(

            MALE_FIRST_NAMES

        )

    elif gender == "Female":

        first_name = random.choice(

            FEMALE_FIRST_NAMES

        )

    else:

        first_name = random.choice(

            MALE_FIRST_NAMES + FEMALE_FIRST_NAMES

        )

    last_name = random.choice(

        LAST_NAMES

    )

    return first_name, last_name


# ==========================================================
# Generate Date of Birth
# ==========================================================

def generate_dob():

    today = pd.Timestamp.today().normalize()

    youngest = today - pd.DateOffset(years=MIN_AGE)

    oldest = today - pd.DateOffset(years=MAX_AGE)

    days = (youngest - oldest).days

    dob = oldest + pd.Timedelta(

        days=random.randint(

            0,

            days

        )

    )

    return dob.date()


# ==========================================================
# Generate Email
# ==========================================================

def generate_email(

    first_name,

    last_name,

    customer_id

):

    pattern = random.choice(

        EMAIL_PATTERNS

    )

    username = pattern.format(

        first=first_name.lower(),

        last=last_name.lower(),

        number=customer_id

    )

    domain = random.choice(

        EMAIL_DOMAINS

    )

    return f"{username}@{domain}"


# ==========================================================
# Generate Phone Number
# ==========================================================

def generate_phone():

    prefix = random.choice(

        PHONE_PREFIXES

    )

    number = "".join(

        random.choices(

            "0123456789",

            k=8

        )

    )

    return prefix + number


# ==========================================================
# Registration Date
# ==========================================================

def generate_registration_date():

    days = (

        REGISTRATION_END -

        REGISTRATION_START

    ).days

    return (

        REGISTRATION_START +

        pd.Timedelta(

            days=random.randint(

                0,

                days

            )

        )

    ).date()


# ==========================================================
# Registration Source
# ==========================================================

def generate_registration_source():

    return random.choices(

        population=list(

            REGISTRATION_SOURCE_WEIGHTS.keys()

        ),

        weights=list(

            REGISTRATION_SOURCE_WEIGHTS.values()

        ),

        k=1

    )[0]


# ==========================================================
# Customer Segment
# ==========================================================

def generate_customer_segment():

    return random.choices(

        population=list(

            CUSTOMER_SEGMENT_WEIGHTS.keys()

        ),

        weights=list(

            CUSTOMER_SEGMENT_WEIGHTS.values()

        ),

        k=1

    )[0]


# ==========================================================
# Loyalty Points
# ==========================================================

def generate_loyalty_points(

    segment

):

    minimum, maximum = LOYALTY_POINTS[

        segment

    ]

    return random.randint(

        minimum,

        maximum

    )


# ==========================================================
# Last Login Date
# ==========================================================

def generate_last_login(

    registration_date

):

    today = datetime.today().date()

    days = (

        today -

        registration_date

    ).days

    if days <= 0:

        return registration_date

    return (

        registration_date +

        pd.Timedelta(

            days=random.randint(

                0,

                days

            )

        )

    )


# ==========================================================
# Active Status
# ==========================================================

def generate_is_active():

    return random.choices(

        population=list(

            ACTIVE_WEIGHTS.keys()

        ),

        weights=list(

            ACTIVE_WEIGHTS.values()

        ),

        k=1

    )[0]
# ==========================================================
# Generate Customers
# ==========================================================

def generate_customers():

    print("=" * 60)
    print("Generating Customers")
    print("=" * 60)

    validate_configuration()

    rows = []

    # ------------------------------------------------------
    # Track Unique Values
    # ------------------------------------------------------

    used_emails = set()

    used_phones = set()

    # ------------------------------------------------------
    # Generate Records
    # ------------------------------------------------------

    for customer_id in range(1, NUM_CUSTOMERS + 1):

        # ----------------------------------------------
        # Gender
        # ----------------------------------------------

        gender = generate_gender()

        # ----------------------------------------------
        # Name
        # ----------------------------------------------

        first_name, last_name = generate_name(

            gender

        )

        # ----------------------------------------------
        # DOB
        # ----------------------------------------------

        dob = generate_dob()

        # ----------------------------------------------
        # Email (Guaranteed Unique)
        # ----------------------------------------------

        while True:

            email = generate_email(

                first_name,

                last_name,

                customer_id

            )

            if email not in used_emails:

                used_emails.add(email)

                break

        # ----------------------------------------------
        # Phone (Guaranteed Unique)
        # ----------------------------------------------

        while True:

            phone = generate_phone()

            if phone not in used_phones:

                used_phones.add(phone)

                break

        # ----------------------------------------------
        # Registration
        # ----------------------------------------------

        registration_date = generate_registration_date()

        registration_source = generate_registration_source()

        # ----------------------------------------------
        # Customer Segment
        # ----------------------------------------------

        segment = generate_customer_segment()

        # ----------------------------------------------
        # Loyalty Points
        # ----------------------------------------------

        loyalty_points = generate_loyalty_points(

            segment

        )

        # ----------------------------------------------
        # Last Login
        # ----------------------------------------------

        last_login = generate_last_login(

            registration_date

        )

        # ----------------------------------------------
        # Active Status
        # ----------------------------------------------

        is_active = generate_is_active()

        # ----------------------------------------------
        # Store Row
        # ----------------------------------------------

        rows.append({

            "CustomerID": customer_id,

            "FirstName": first_name,

            "LastName": last_name,

            "Gender": gender,

            "DateOfBirth": dob,

            "Email": email,

            "Phone": phone,

            "RegistrationDate": registration_date,

            "RegistrationSource": registration_source,

            "CustomerSegment": segment,

            "LoyaltyPoints": loyalty_points,

            "LastLoginDate": last_login,

            "IsActive": is_active

        })

        # ----------------------------------------------
        # Progress
        # ----------------------------------------------

        if customer_id % PROGRESS_INTERVAL == 0:

            print(

                f"{customer_id:,} Customers Generated..."

            )

    customers = pd.DataFrame(rows)

    print("=" * 60)
    print("Customer Generation Completed")
    print("=" * 60)

    print(f"Rows : {len(customers):,}")

    return customers
# ==========================================================
# Validate Customers
# ==========================================================

def validate_customers(customers):

    print("=" * 60)
    print("Validating Customers")
    print("=" * 60)

    # ------------------------------------------------------
    # Empty Dataset
    # ------------------------------------------------------

    if customers.empty:
        raise ValueError("Customer dataset is empty.")

    print("✓ Dataset Validation Passed")

    # ------------------------------------------------------
    # Convert Date Columns Once
    # ------------------------------------------------------

    customers = customers.copy()

    customers["DateOfBirth"] = pd.to_datetime(
        customers["DateOfBirth"]
    )

    customers["RegistrationDate"] = pd.to_datetime(
        customers["RegistrationDate"]
    )

    customers["LastLoginDate"] = pd.to_datetime(
        customers["LastLoginDate"]
    )

    today = pd.Timestamp.today().normalize()

    # ------------------------------------------------------
    # CustomerID
    # ------------------------------------------------------

    if customers["CustomerID"].duplicated().any():
        raise ValueError("Duplicate CustomerID found.")

    print("✓ CustomerID Validation Passed")

    # ------------------------------------------------------
    # Email
    # ------------------------------------------------------

    if customers["Email"].duplicated().any():
        raise ValueError("Duplicate Email found.")

    print("✓ Email Validation Passed")

    # ------------------------------------------------------
    # Phone
    # ------------------------------------------------------

    if customers["Phone"].duplicated().any():
        raise ValueError("Duplicate Phone found.")

    print("✓ Phone Validation Passed")

    # ------------------------------------------------------
    # Required Columns
    # ------------------------------------------------------

    required_columns = [

        "FirstName",
        "LastName",
        "Email",
        "Phone",
        "RegistrationDate",
        "CustomerSegment"

    ]

    for column in required_columns:

        if customers[column].isnull().any():

            raise ValueError(

                f"Null values found in {column}"

            )

    print("✓ Required Column Validation Passed")

    # ------------------------------------------------------
    # Age Validation
    # ------------------------------------------------------

    age = (

        (today - customers["DateOfBirth"])

        .dt.days // 365

    )

    if (age < MIN_AGE).any():

        raise ValueError(

            "Customers below minimum age found."

        )

    if (age > MAX_AGE).any():

        raise ValueError(

            "Customers above maximum age found."

        )

    print("✓ Date Of Birth Validation Passed")

    # ------------------------------------------------------
    # Registration Date
    # ------------------------------------------------------

    if (customers["RegistrationDate"] > today).any():

        raise ValueError(

            "Future RegistrationDate found."

        )

    print("✓ Registration Date Validation Passed")

    # ------------------------------------------------------
    # Last Login
    # ------------------------------------------------------

    if (

        customers["LastLoginDate"] <

        customers["RegistrationDate"]

    ).any():

        raise ValueError(

            "LastLoginDate cannot be earlier than RegistrationDate."

        )

    if (

        customers["LastLoginDate"] > today

    ).any():

        raise ValueError(

            "Future LastLoginDate found."

        )

    print("✓ Last Login Validation Passed")

    # ------------------------------------------------------
    # Loyalty Points
    # ------------------------------------------------------

    if (

        customers["LoyaltyPoints"] < 0

    ).any():

        raise ValueError(

            "Negative LoyaltyPoints found."

        )

    print("✓ Loyalty Points Validation Passed")

    # ------------------------------------------------------
    # IsActive
    # ------------------------------------------------------

    if (

        ~customers["IsActive"].isin([0, 1])

    ).any():

        raise ValueError(

            "Invalid IsActive values."

        )

    print("✓ IsActive Validation Passed")

    # ------------------------------------------------------
    # Summary
    # ------------------------------------------------------

    print("=" * 60)
    print("ALL CUSTOMER VALIDATIONS PASSED")
    print("=" * 60)

    print(f"Customers          : {len(customers):,}")

    print(f"Male               : {(customers['Gender'] == 'Male').sum():,}")

    print(f"Female             : {(customers['Gender'] == 'Female').sum():,}")

    print(f"Other              : {(customers['Gender'] == 'Other').sum():,}")

    print()

    print("Customer Segments")

    print(customers["CustomerSegment"].value_counts())

    print()

    print(f"Active Customers   : {(customers['IsActive'] == 1).sum():,}")

    print(f"Inactive Customers : {(customers['IsActive'] == 0).sum():,}")

    print("=" * 60)

    return True
# ==========================================================
# Export Customers
# ==========================================================

def export_customers(customers):

    print("=" * 60)
    print("Exporting Customers")
    print("=" * 60)

    CSV_OUTPUT.mkdir(

        parents=True,

        exist_ok=True

    )

    output_file = (

        CSV_OUTPUT /

        "customers.csv"

    )

    customers.to_csv(

        output_file,

        index=False

    )

    print(f"SUCCESS : {len(customers):,} customers exported.")

    print(f"Location : {output_file}")

    return output_file


# ==========================================================
# Customer Summary
# ==========================================================

def print_summary(customers):

    print("\n" + "=" * 60)
    print("CUSTOMER GENERATION SUMMARY")
    print("=" * 60)

    print(f"Total Customers      : {len(customers):,}")

    print(f"Male Customers       : {(customers['Gender'] == 'Male').sum():,}")

    print(f"Female Customers     : {(customers['Gender'] == 'Female').sum():,}")

    print(f"Other Customers      : {(customers['Gender'] == 'Other').sum():,}")

    print()

    print("Customer Segments")

    print(

        customers["CustomerSegment"]

        .value_counts()

    )

    print()

    print("Registration Sources")

    print(

        customers["RegistrationSource"]

        .value_counts()

    )

    print()

    print(f"Average Loyalty Points : {customers['LoyaltyPoints'].mean():,.0f}")

    print(f"Maximum Loyalty Points : {customers['LoyaltyPoints'].max():,}")

    print(f"Minimum Loyalty Points : {customers['LoyaltyPoints'].min():,}")

    print()

    print(f"Active Customers       : {(customers['IsActive'] == 1).sum():,}")

    print(f"Inactive Customers     : {(customers['IsActive'] == 0).sum():,}")

    print("=" * 60)


# ==========================================================
# Main
# ==========================================================

def main():

    print("\n")
    print("=" * 60)
    print("SHOPSPHERE CUSTOMER GENERATOR")
    print("=" * 60)

    customers = generate_customers()

    validate_customers(customers)

    export_customers(customers)

    print_summary(customers)

    print("\nSUCCESS : Customer generation completed successfully.")

    print("=" * 60)


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    main()