"""
=========================================================
ShopSphere Analytics
lookup_generator.py

Generates:

    payment_methods.csv
    couriers.csv
    return_reasons.csv
    support_issues.csv

Author : Prasanta Kumar Deb
=========================================================
"""

import pandas as pd

from config.config import REFERENCE_DATA

# =========================================================
# Payment Methods
# =========================================================

PAYMENT_METHODS = [

    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking",
    "Wallet",
    "Cash on Delivery",
    "EMI",
    "Gift Card"

]

# =========================================================
# Couriers
# =========================================================

COURIERS = [

    "Blue Dart",
    "Delhivery",
    "DTDC",
    "Ecom Express",
    "Ekart",
    "India Post",
    "Shadowfax",
    "XpressBees",
    "FedEx",
    "DHL",
    "Aramex",
    "Amazon Transportation",
    "Borzo",
    "Gati",
    "Trackon"

]

# =========================================================
# Return Reasons
# =========================================================

RETURN_REASONS = [

    "Wrong Product",

    "Damaged Product",

    "Defective Product",

    "Size Too Small",

    "Size Too Large",

    "Quality Not As Expected",

    "Changed Mind",

    "Duplicate Order",

    "Item Missing",

    "Late Delivery",

    "Wrong Color",

    "Better Price Available"

]

# =========================================================
# Support Issues
# =========================================================

SUPPORT_ISSUES = [

    "Payment Failed",

    "Refund Request",

    "Order Cancellation",

    "Delivery Delay",

    "Order Not Received",

    "Damaged Product",

    "Account Issue",

    "Coupon Issue",

    "Product Inquiry",

    "Return Request",

    "Replacement Request",

    "Invoice Request",

    "Warranty Claim",

    "App Issue",

    "Website Issue"

]

# =========================================================
# Generic CSV Writer
# =========================================================

def save_lookup(data, filename, id_column, name_column):

    rows = []

    for idx, value in enumerate(data, start=1):

        rows.append({

            id_column: idx,

            name_column: value,

            "Description": value,

            "IsActive": 1

        })

    df = pd.DataFrame(rows)

    output = REFERENCE_DATA / filename

    output.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output, index=False)

    print(f"✔ {filename:<25} {len(df)} rows")

    return df

# =========================================================
# Generate All Lookups
# =========================================================

def generate_lookup_tables():

    print("=" * 60)
    print("Generating Lookup Tables")
    print("=" * 60)

    save_lookup(

        PAYMENT_METHODS,

        "payment_methods.csv",

        "PaymentMethodID",

        "PaymentMethodName"

    )

    save_lookup(

        COURIERS,

        "couriers.csv",

        "CourierID",

        "CourierName"

    )

    save_lookup(

        RETURN_REASONS,

        "return_reasons.csv",

        "ReturnReasonID",

        "ReturnReasonName"

    )

    save_lookup(

        SUPPORT_ISSUES,

        "support_issues.csv",

        "SupportIssueID",

        "SupportIssueName"

    )

    print("=" * 60)
    print("Lookup Tables Generated Successfully")
    print("=" * 60)

# =========================================================
# Main
# =========================================================

if __name__ == "__main__":

    generate_lookup_tables()