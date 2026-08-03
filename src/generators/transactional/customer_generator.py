"""
=========================================================
ShopSphere Analytics
customer_generator.py

Generates:
    output/csv/customers.csv

Author : Prasanta Kumar Deb
=========================================================
"""

import random
from pathlib import Path
from datetime import datetime, timedelta

import pandas as pd

from config.config import (
    REFERENCE_DATA,
    CSV_OUTPUT,
    NUM_CUSTOMERS,
    RANDOM_SEED
)

random.seed(RANDOM_SEED)

# ==========================================================
# Business Constants
# ==========================================================

GENDER_DISTRIBUTION = {

    "Male": 0.52,
    "Female": 0.48

}

REGISTRATION_SOURCE = {

    "Android App": 0.45,
    "Website": 0.30,
    "iOS App": 0.15,
    "Referral": 0.05,
    "Customer Support": 0.05

}

CUSTOMER_SEGMENT = {

    "Regular": 0.60,
    "Silver": 0.20,
    "Gold": 0.15,
    "Platinum": 0.05

}

ACTIVE_RATE = 0.97

START_DATE = datetime(2023,1,1)

END_DATE = datetime(2025,12,31)

# ==========================================================
# Load Reference CSVs
# ==========================================================

def load_reference_data():

    male_names = pd.read_csv(
        REFERENCE_DATA / "first_names_male.csv"
    )

    female_names = pd.read_csv(
        REFERENCE_DATA / "first_names_female.csv"
    )

    last_names = pd.read_csv(
        REFERENCE_DATA / "last_names.csv"
    )

    email_domains = pd.read_csv(
        REFERENCE_DATA / "email_domains.csv"
    )

    cities = pd.read_csv(
        REFERENCE_DATA / "cities.csv"
    )

    states = pd.read_csv(
        REFERENCE_DATA / "states.csv"
    )

    return (
        male_names,
        female_names,
        last_names,
        email_domains,
        cities,
        states
    )
    
    # ==========================================================
# Weighted Choice
# ==========================================================

def weighted_choice(mapping):

    values = list(mapping.keys())

    weights = list(mapping.values())

    return random.choices(

        values,

        weights=weights,

        k=1

    )[0]
    
# ==========================================================
# Random Date
# ==========================================================

def random_registration_date():

    days = (END_DATE - START_DATE).days

    return START_DATE + timedelta(

        days=random.randint(0, days)

    )


def random_last_login(registration_date):

    days = (END_DATE - registration_date).days

    if days <= 0:

        return registration_date

    return registration_date + timedelta(

        days=random.randint(0, days)

    )


def random_dob():

    today = datetime.today()

    age = random.randint(18,70)

    return today - timedelta(days=age*365)

# ==========================================================
# Email Generator
# ==========================================================

used_emails = set()

def generate_email(

    first,

    last,

    domains,

    customer_id

):

    while True:

        email = (

            f"{first.lower()}."

            f"{last.lower()}"

            f"{customer_id}"

            "@"

            f"{random.choice(domains)}"

        )

        if email not in used_emails:

            used_emails.add(email)

            return email
        
# ==========================================================
# Phone Generator
# ==========================================================

used_phones = set()

def generate_phone():

    while True:

        phone = "9" + "".join(

            random.choices(

                "0123456789",

                k=9

            )

        )

        if phone not in used_phones:

            used_phones.add(phone)

            return phone
# ==========================================================
# Loyalty Points
# ==========================================================

def loyalty_points(segment):

    if segment=="Regular":

        return random.randint(0,1000)

    if segment=="Silver":

        return random.randint(1001,5000)

    if segment=="Gold":

        return random.randint(5001,12000)

    return random.randint(12001,50000)

# ==========================================================
# Generate Customers
# ==========================================================

def generate_customers():

    (
        male_names,
        female_names,
        last_names,
        email_domains,
        cities,
        states
    ) = load_reference_data()

    male_list = male_names.iloc[:, 0].tolist()
    female_list = female_names.iloc[:, 0].tolist()
    last_list = last_names.iloc[:, 0].tolist()
    domain_list = email_domains.iloc[:, 0].tolist()

    customers = []

    print("=" * 60)
    print("Generating Customers...")
    print("=" * 60)

    for customer_id in range(1, NUM_CUSTOMERS + 1):

        # -----------------------------
        # Gender
        # -----------------------------

        gender = weighted_choice(
            GENDER_DISTRIBUTION
        )

        if gender == "Male":

            first_name = random.choice(
                male_list
            )

        else:

            first_name = random.choice(
                female_list
            )

        last_name = random.choice(
            last_list
        )

        # -----------------------------
        # Dates
        # -----------------------------

        dob = random_dob()

        registration_date = random_registration_date()

        last_login = random_last_login(
            registration_date
        )

        # -----------------------------
        # Segment
        # -----------------------------

        segment = weighted_choice(
            CUSTOMER_SEGMENT
        )

        # -----------------------------
        # Source
        # -----------------------------

        registration_source = weighted_choice(
            REGISTRATION_SOURCE
        )

        # -----------------------------
        # Email
        # -----------------------------

        email = generate_email(

            first_name,

            last_name,

            domain_list,

            customer_id

        )

        # -----------------------------
        # Phone
        # -----------------------------

        phone = generate_phone()

        # -----------------------------
        # Active
        # -----------------------------

        is_active = int(

            random.random() <= ACTIVE_RATE

        )

        # -----------------------------
        # Loyalty
        # -----------------------------

        points = loyalty_points(
            segment
        )

        # -----------------------------
        # Created
        # -----------------------------

        created_at = registration_date

        updated_at = last_login

        # -----------------------------
        # Record
        # -----------------------------

        customers.append({

            "CustomerID": customer_id,

            "FirstName": first_name,

            "LastName": last_name,

            "Gender": gender,

            "DateOfBirth": dob.date(),

            "Email": email,

            "Phone": phone,

            "RegistrationDate": registration_date,

            "RegistrationSource": registration_source,

            "CustomerSegment": segment,

            "LoyaltyPoints": points,

            "LastLoginDate": last_login,

            "IsActive": is_active,

            "CreatedAt": created_at,

            "UpdatedAt": updated_at

        })

        # -----------------------------
        # Progress
        # -----------------------------

        if customer_id % 10000 == 0:

            print(

                f"{customer_id:,} customers generated..."

            )

    print("=" * 60)

    df = pd.DataFrame(customers)

    return df
# ==========================================================
# Validate Customer Data
# ==========================================================

def validate_customers(df):

    print("\n" + "=" * 60)
    print("Validating Customer Data")
    print("=" * 60)

    # ------------------------------------------------------
    # Duplicate CustomerID
    # ------------------------------------------------------

    assert df["CustomerID"].is_unique, \
        "Duplicate CustomerID found."

    # ------------------------------------------------------
    # Duplicate Email
    # ------------------------------------------------------

    assert df["Email"].is_unique, \
        "Duplicate Email found."

    # ------------------------------------------------------
    # Duplicate Phone
    # ------------------------------------------------------

    assert df["Phone"].is_unique, \
        "Duplicate Phone found."

    # ------------------------------------------------------
    # Null Values
    # ------------------------------------------------------

    if df.isnull().sum().sum() > 0:

        raise ValueError(
            "Null values detected."
        )

    # ------------------------------------------------------
    # Last Login >= Registration
    # ------------------------------------------------------

    invalid_dates = (

        df["LastLoginDate"]

        <

        df["RegistrationDate"]

    ).sum()

    if invalid_dates > 0:

        raise ValueError(

            "Last Login before Registration Date."

        )

    print("✔ CustomerID Unique")
    print("✔ Email Unique")
    print("✔ Phone Unique")
    print("✔ No Null Values")
    print("✔ Date Validation Passed")

    print("=" * 60)
    
# ==========================================================
# Export CSV
# ==========================================================

def export_customers(df):

    output_file = CSV_OUTPUT / "customers.csv"

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
    print("Customer CSV Exported Successfully")
    print("=" * 60)
    print(f"Rows   : {len(df):,}")
    print(f"Output : {output_file}")
    print("=" * 60)
    
# ==========================================================
# Summary
# ==========================================================

def print_summary(df):

    print("\n" + "=" * 60)
    print("Customer Summary")
    print("=" * 60)

    print(f"Customers : {len(df):,}")

    print()

    print("Gender")

    print(df["Gender"].value_counts())

    print()

    print("Customer Segment")

    print(df["CustomerSegment"].value_counts())

    print()

    print("Registration Source")

    print(df["RegistrationSource"].value_counts())

    print()

    print("Active Customers")

    print(df["IsActive"].value_counts())

    print("=" * 60)
    
# ==========================================================
# Main
# ==========================================================

def main():

    print("\n")
    print("=" * 70)
    print("ShopSphere Analytics")
    print("Customer Generator")
    print("=" * 70)

    customers = generate_customers()

    validate_customers(customers)

    export_customers(customers)

    print_summary(customers)

    print("\nCompleted Successfully.")

# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":

    main()
    
