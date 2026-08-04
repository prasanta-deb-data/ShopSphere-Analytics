"""
=========================================================
ShopSphere Analytics

lookup_generator.py

Generates

    payment_methods.csv
    couriers.csv
    return_reasons.csv
    support_issues.csv

Author : Prasanta Kumar Deb
=========================================================
"""

from pathlib import Path

import pandas as pd

from config.config import REFERENCE_DATA

# =========================================================
# Payment Methods
# =========================================================

PAYMENT_METHODS = [

    {
        "PaymentMethodName": "Credit Card",
        "Description": "Visa, MasterCard, RuPay and other credit cards"
    },

    {
        "PaymentMethodName": "Debit Card",
        "Description": "Visa, MasterCard and RuPay debit cards"
    },

    {
        "PaymentMethodName": "UPI",
        "Description": "Unified Payments Interface"
    },

    {
        "PaymentMethodName": "Net Banking",
        "Description": "Internet banking payment"
    },

    {
        "PaymentMethodName": "Wallet",
        "Description": "Digital wallet payment"
    },

    {
        "PaymentMethodName": "Cash on Delivery",
        "Description": "Payment collected during delivery"
    },

    {
        "PaymentMethodName": "EMI",
        "Description": "Equated Monthly Installment"
    },

    {
        "PaymentMethodName": "Gift Card",
        "Description": "Gift voucher or prepaid balance"
    }

]

# =========================================================
# Couriers
# =========================================================

COURIERS = [

    {
        "CourierName": "Blue Dart",
        "ContactNumber": "1860-233-1234",
        "Website": "https://www.bluedart.com"
    },

    {
        "CourierName": "Delhivery",
        "ContactNumber": "1800-103-6354",
        "Website": "https://www.delhivery.com"
    },

    {
        "CourierName": "DTDC",
        "ContactNumber": "7305770577",
        "Website": "https://www.dtdc.in"
    },

    {
        "CourierName": "Ecom Express",
        "ContactNumber": "",
        "Website": "https://www.ecomexpress.in"
    },

    {
        "CourierName": "Ekart",
        "ContactNumber": "",
        "Website": "https://www.ekartlogistics.com"
    },

    {
        "CourierName": "India Post",
        "ContactNumber": "1800-266-6868",
        "Website": "https://www.indiapost.gov.in"
    },

    {
        "CourierName": "Shadowfax",
        "ContactNumber": "",
        "Website": "https://www.shadowfax.in"
    },

    {
        "CourierName": "XpressBees",
        "ContactNumber": "",
        "Website": "https://www.xpressbees.com"
    },

    {
        "CourierName": "FedEx",
        "ContactNumber": "1800-209-6161",
        "Website": "https://www.fedex.com"
    },

    {
        "CourierName": "DHL",
        "ContactNumber": "1800-111-345",
        "Website": "https://www.dhl.com"
    },

    {
        "CourierName": "Aramex",
        "ContactNumber": "",
        "Website": "https://www.aramex.com"
    },

    {
        "CourierName": "Amazon Transportation",
        "ContactNumber": "",
        "Website": "https://www.amazon.in"
    },

    {
        "CourierName": "Borzo",
        "ContactNumber": "",
        "Website": "https://borzodelivery.com"
    },

    {
        "CourierName": "Gati",
        "ContactNumber": "1860-123-4284",
        "Website": "https://www.gati.com"
    },

    {
        "CourierName": "Trackon",
        "ContactNumber": "",
        "Website": "https://www.trackon.in"
    }

]

# =========================================================
# Return Reasons
# =========================================================

RETURN_REASONS = [

    {
        "ReturnReasonName": "Wrong Product",
        "Description": "Customer received a different product."
    },

    {
        "ReturnReasonName": "Damaged Product",
        "Description": "Product arrived damaged."
    },

    {
        "ReturnReasonName": "Defective Product",
        "Description": "Product is not functioning properly."
    },

    {
        "ReturnReasonName": "Size Too Small",
        "Description": "Ordered size is smaller than expected."
    },

    {
        "ReturnReasonName": "Size Too Large",
        "Description": "Ordered size is larger than expected."
    },

    {
        "ReturnReasonName": "Quality Not As Expected",
        "Description": "Customer not satisfied with product quality."
    },

    {
        "ReturnReasonName": "Changed Mind",
        "Description": "Customer no longer wants the product."
    },

    {
        "ReturnReasonName": "Duplicate Order",
        "Description": "Multiple orders placed accidentally."
    },

    {
        "ReturnReasonName": "Item Missing",
        "Description": "Some items were missing from the shipment."
    },

    {
        "ReturnReasonName": "Late Delivery",
        "Description": "Order delivered later than expected."
    },

    {
        "ReturnReasonName": "Wrong Color",
        "Description": "Received a different color."
    },

    {
        "ReturnReasonName": "Better Price Available",
        "Description": "Customer found a better price elsewhere."
    }

]

# =========================================================
# Support Issues
# =========================================================

SUPPORT_ISSUES = [

    {
        "SupportIssueName": "Payment Failed",
        "Description": "Customer unable to complete payment."
    },

    {
        "SupportIssueName": "Refund Request",
        "Description": "Customer requested a refund."
    },

    {
        "SupportIssueName": "Order Cancellation",
        "Description": "Customer wants to cancel an order."
    },

    {
        "SupportIssueName": "Delivery Delay",
        "Description": "Shipment delayed beyond expected date."
    },

    {
        "SupportIssueName": "Order Not Received",
        "Description": "Customer has not received the order."
    },

    {
        "SupportIssueName": "Damaged Product",
        "Description": "Product damaged during delivery."
    },

    {
        "SupportIssueName": "Account Issue",
        "Description": "Customer account access problem."
    },

    {
        "SupportIssueName": "Coupon Issue",
        "Description": "Coupon not applied correctly."
    },

    {
        "SupportIssueName": "Product Inquiry",
        "Description": "Customer requested product information."
    },

    {
        "SupportIssueName": "Return Request",
        "Description": "Customer initiated a return."
    },

    {
        "SupportIssueName": "Replacement Request",
        "Description": "Customer requested a replacement."
    },

    {
        "SupportIssueName": "Invoice Request",
        "Description": "Customer requested a copy of the invoice."
    },

    {
        "SupportIssueName": "Warranty Claim",
        "Description": "Customer raised a warranty claim."
    },

    {
        "SupportIssueName": "App Issue",
        "Description": "Problem using the mobile application."
    },

    {
        "SupportIssueName": "Website Issue",
        "Description": "Problem using the website."
    }

]

# =========================================================
# Generate Payment Methods
# =========================================================

def generate_payment_methods():

    rows = []

    for idx, payment in enumerate(

        PAYMENT_METHODS,

        start=1

    ):

        rows.append({

            "PaymentMethodID": idx,

            "PaymentMethodName": payment["PaymentMethodName"],

            "Description": payment["Description"],

            "IsActive": 1

        })

    df = pd.DataFrame(rows)

    output = REFERENCE_DATA / "payment_methods.csv"

    output.parent.mkdir(

        parents=True,

        exist_ok=True

    )

    df.to_csv(

        output,

        index=False

    )

    print("=" * 60)
    print("Payment Methods Generated")
    print("=" * 60)
    print(f"Rows   : {len(df)}")
    print(f"Output : {output}")

    return df
# =========================================================
# Generate Couriers
# =========================================================

def generate_couriers():

    rows = []

    for idx, courier in enumerate(

        COURIERS,

        start=1

    ):

        rows.append({

            "CourierID": idx,

            "CourierName": courier["CourierName"],

            "ContactNumber": courier["ContactNumber"],

            "Website": courier["Website"],

            "IsActive": 1

        })

    df = pd.DataFrame(rows)

    output = REFERENCE_DATA / "couriers.csv"

    output.parent.mkdir(

        parents=True,

        exist_ok=True

    )

    df.to_csv(

        output,

        index=False

    )

    print("=" * 60)
    print("Couriers Generated")
    print("=" * 60)
    print(f"Rows   : {len(df)}")
    print(f"Output : {output}")

    return df
# =========================================================
# Generate Return Reasons
# =========================================================

def generate_return_reasons():

    rows = []

    for idx, reason in enumerate(

        RETURN_REASONS,

        start=1

    ):

        rows.append({

            "ReturnReasonID": idx,

            "ReturnReasonName": reason["ReturnReasonName"],

            "Description": reason["Description"],

            "IsActive": 1

        })

    df = pd.DataFrame(rows)

    output = REFERENCE_DATA / "return_reasons.csv"

    output.parent.mkdir(

        parents=True,

        exist_ok=True

    )

    df.to_csv(

        output,

        index=False

    )

    print("=" * 60)
    print("Return Reasons Generated")
    print("=" * 60)
    print(f"Rows   : {len(df)}")
    print(f"Output : {output}")

    return df


# =========================================================
# Generate Support Issues
# =========================================================

def generate_support_issues():

    rows = []

    for idx, issue in enumerate(

        SUPPORT_ISSUES,

        start=1

    ):

        rows.append({

            "SupportIssueID": idx,

            "SupportIssueName": issue["SupportIssueName"],

            "Description": issue["Description"],

            "IsActive": 1

        })

    df = pd.DataFrame(rows)

    output = REFERENCE_DATA / "support_issues.csv"

    output.parent.mkdir(

        parents=True,

        exist_ok=True

    )

    df.to_csv(

        output,

        index=False

    )

    print("=" * 60)
    print("Support Issues Generated")
    print("=" * 60)
    print(f"Rows   : {len(df)}")
    print(f"Output : {output}")

    return df
# =========================================================
# Generate All Lookup Tables
# =========================================================

def generate_lookup_tables():

    print("=" * 60)
    print("Generating Lookup Tables")
    print("=" * 60)

    generate_payment_methods()

    generate_couriers()

    generate_return_reasons()

    generate_support_issues()

    print("=" * 60)
    print("Lookup Tables Generated Successfully")
    print("=" * 60)


# =========================================================
# Main
# =========================================================

def main():

    generate_lookup_tables()


if __name__ == "__main__":

    main()