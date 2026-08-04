"""
=========================================================
ShopSphere Analytics

orders_generator.py

Generates:
    output/csv/orders.csv

Stage Generator
(Financial columns are updated later by
update_orders_financials.py)

Author : Prasanta Kumar Deb
=========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import random

from datetime import (

    datetime,

    timedelta

)

from pathlib import Path

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

NUM_ORDERS = 1_000_000

ORDER_ID_START = 1_000_001

ORDER_START_DATE = datetime(

    2023,

    1,

    1

)

ORDER_END_DATE = datetime(

    2025,

    12,

    31

)

PROGRESS_INTERVAL = 10_000

# ==========================================================
# Load Master Data
# ==========================================================

def load_master_data():

    return {

        "Customers": pd.read_csv(

            CSV_OUTPUT /

            "customers.csv"

        ),

        "CustomerAddresses": pd.read_csv(

            CSV_OUTPUT /

            "customer_addresses.csv"

        )

    }

# ==========================================================
# Load Once
# ==========================================================

MASTER = load_master_data()

CUSTOMERS = MASTER["Customers"]

CUSTOMER_ADDRESSES = MASTER["CustomerAddresses"]

# ==========================================================
# Fast Lookups
# ==========================================================

CUSTOMER_IDS = (

    CUSTOMERS["CustomerID"]

    .tolist()

)

ADDRESS_LOOKUP = (

    CUSTOMER_ADDRESSES

    .groupby(

        "CustomerID"

    )

)

# ==========================================================
# Validate Master Data
# ==========================================================

def validate_master_data():

    print("=" * 60)

    print(

        "Orders Generator Configuration"

    )

    print("=" * 60)

    if CUSTOMERS.empty:

        raise ValueError(

            "customers.csv is empty."

        )

    if CUSTOMER_ADDRESSES.empty:

        raise ValueError(

            "customer_addresses.csv is empty."

        )

    if ORDER_START_DATE >= ORDER_END_DATE:

        raise ValueError(

            "Invalid order date range."

        )

    print(

        f"Orders             : {NUM_ORDERS:,}"

    )

    print(

        f"Customers          : {len(CUSTOMERS):,}"

    )

    print(

        f"Customer Addresses : {len(CUSTOMER_ADDRESSES):,}"

    )

    print(

        f"Order Start Date   : {ORDER_START_DATE.date()}"

    )

    print(

        f"Order End Date     : {ORDER_END_DATE.date()}"

    )

    print("=" * 60)
# ==========================================================
# Order Status Distribution
# ==========================================================

ORDER_STATUS_DISTRIBUTION = {

    "Delivered": 70,

    "Shipped": 12,

    "Processing": 8,

    "Pending": 5,

    "Cancelled": 3,

    "Returned": 2

}

# ==========================================================
# Order Channels
# ==========================================================

ORDER_CHANNEL_DISTRIBUTION = {

    "Website": 58,

    "Mobile App": 32,

    "Marketplace": 5,

    "Customer Support": 5

}

# ==========================================================
# Payment Status Mapping
# ==========================================================

PAYMENT_STATUS_MAPPING = {

    "Delivered": "Paid",

    "Shipped": "Paid",

    "Processing": "Paid",

    "Pending": "Pending",

    "Cancelled": "Refunded",

    "Returned": "Refunded"

}

# ==========================================================
# Customer Selection Weights
# ==========================================================

SEGMENT_WEIGHTS = {

    "Premium": 8,

    "Gold": 5,

    "Silver": 3,

    "Standard": 1

}

# ==========================================================
# Loyalty Bonus Weights
# ==========================================================

LOYALTY_WEIGHT_RULES = [

    (5000, 4),

    (2500, 2),

    (1000, 1)

]

# ==========================================================
# Order Time
# ==========================================================

ORDER_START_HOUR = 7

ORDER_END_HOUR = 23

# ==========================================================
# Delivery SLA
# ==========================================================

MIN_DELIVERY_DAYS = 2

MAX_DELIVERY_DAYS = 10

# ==========================================================
# Delivered Order Variance
# ==========================================================

EARLY_DELIVERY_DAYS = 2

LATE_DELIVERY_DAYS = 2

# ==========================================================
# Weekend Ordering
# ==========================================================

WEEKEND_ORDER_MULTIPLIER = 1.10

# ==========================================================
# Festival Ordering
# ==========================================================

FESTIVAL_ORDER_MULTIPLIER = 1.30
# ==========================================================
# Build Customer Pool
# ==========================================================

def build_customer_pool():

    customer_pool = []

    for customer in CUSTOMERS.itertuples(index=False):

        weight = SEGMENT_WEIGHTS.get(

            customer.CustomerSegment,

            1

        )

        for threshold, bonus in LOYALTY_WEIGHT_RULES:

            if customer.LoyaltyPoints >= threshold:

                weight += bonus

                break

        customer_pool.extend(

            [customer.CustomerID] * weight

        )

    return customer_pool


# ==========================================================
# Build Once
# ==========================================================

CUSTOMER_POOL = build_customer_pool()


# ==========================================================
# Generate Order ID
# ==========================================================

def generate_order_id(sequence):

    return ORDER_ID_START + sequence


# ==========================================================
# Select Customer
# ==========================================================

def select_customer():

    return random.choice(

        CUSTOMER_POOL

    )


# ==========================================================
# Generate Order Date
# ==========================================================

def generate_order_date():

    total_days = (

        ORDER_END_DATE -

        ORDER_START_DATE

    ).days

    return (

        ORDER_START_DATE +

        timedelta(

            days=random.randint(

                0,

                total_days

            ),

            hours=random.randint(

                ORDER_START_HOUR,

                ORDER_END_HOUR

            ),

            minutes=random.randint(

                0,

                59

            ),

            seconds=random.randint(

                0,

                59

            )

        )

    )


# ==========================================================
# Generate Order Status
# ==========================================================

def generate_order_status():

    return random.choices(

        population=list(

            ORDER_STATUS_DISTRIBUTION.keys()

        ),

        weights=list(

            ORDER_STATUS_DISTRIBUTION.values()

        ),

        k=1

    )[0]


# ==========================================================
# Generate Order Channel
# ==========================================================

def generate_order_channel():

    return random.choices(

        population=list(

            ORDER_CHANNEL_DISTRIBUTION.keys()

        ),

        weights=list(

            ORDER_CHANNEL_DISTRIBUTION.values()

        ),

        k=1

    )[0]


# ==========================================================
# Generate Payment Status
# ==========================================================

def generate_payment_status(

    order_status

):

    return PAYMENT_STATUS_MAPPING[

        order_status

    ]


# ==========================================================
# Generate Delivery Dates
# ==========================================================

def generate_delivery_dates(

    order_date,

    order_status

):

    expected_delivery = (

        order_date +

        timedelta(

            days=random.randint(

                MIN_DELIVERY_DAYS,

                MAX_DELIVERY_DAYS

            )

        )

    ).date()

    delivered_date = None

    if order_status in (

        "Delivered",

        "Returned"

    ):

        variance = random.randint(

            -EARLY_DELIVERY_DAYS,

            LATE_DELIVERY_DAYS

        )

        delivered_date = (

            expected_delivery +

            timedelta(

                days=variance

            )

        )

        if delivered_date < order_date.date():

            delivered_date = order_date.date()

    return (

        expected_delivery,

        delivered_date

    )


# ==========================================================
# Progress Logger
# ==========================================================

def log_progress(

    current_order

):

    if current_order % PROGRESS_INTERVAL == 0:

        print(

            f"{current_order:,} Orders Generated..."

        )
# ==========================================================
# Generate Orders
# ==========================================================

def generate_orders():

    print("=" * 60)

    print(

        "Generating Orders"

    )

    print("=" * 60)

    validate_master_data()

    rows = []

    # ------------------------------------------------------
    # Generate Orders
    # ------------------------------------------------------

    for sequence in range(NUM_ORDERS):

        order_id = generate_order_id(

            sequence

        )

        customer_id = select_customer()

        order_date = generate_order_date()

        order_status = generate_order_status()

        order_channel = generate_order_channel()

        payment_status = generate_payment_status(

            order_status

        )

        expected_delivery_date, delivered_date = (

            generate_delivery_dates(

                order_date,

                order_status

            )

        )

        rows.append(

            {

                "OrderID": order_id,

                "CustomerID": customer_id,

                "OrderDate": order_date,

                "OrderStatus": order_status,

                "OrderChannel": order_channel,

                "TotalAmount": 0.00,

                "DiscountAmount": 0.00,

                "ShippingCharge": 0.00,

                "TaxAmount": 0.00,

                "FinalAmount": 0.00,

                "PaymentStatus": payment_status,

                "ExpectedDeliveryDate": expected_delivery_date,

                "DeliveredDate": delivered_date

            }

        )

        log_progress(

            sequence + 1

        )

    # ------------------------------------------------------
    # Create DataFrame
    # ------------------------------------------------------

    orders = pd.DataFrame(

        rows,

        columns=[

            "OrderID",

            "CustomerID",

            "OrderDate",

            "OrderStatus",

            "OrderChannel",

            "TotalAmount",

            "DiscountAmount",

            "ShippingCharge",

            "TaxAmount",

            "FinalAmount",

            "PaymentStatus",

            "ExpectedDeliveryDate",

            "DeliveredDate"

        ]

    )

    # ------------------------------------------------------
    # Data Types
    # ------------------------------------------------------

    orders["OrderDate"] = pd.to_datetime(

        orders["OrderDate"]

    )

    orders["ExpectedDeliveryDate"] = pd.to_datetime(

        orders["ExpectedDeliveryDate"]

    ).dt.date

    orders["DeliveredDate"] = pd.to_datetime(

        orders["DeliveredDate"]

    ).dt.date

    # ------------------------------------------------------
    # Generation Summary
    # ------------------------------------------------------

    print()

    print("=" * 60)

    print(

        "Order Generation Completed"

    )

    print("=" * 60)

    print(

        f"Orders Generated : {len(orders):,}"

    )

    print()

    print(

        "Order Status Distribution"

    )

    print(

        orders["OrderStatus"]

        .value_counts()

        .sort_index()

    )

    print()

    print(

        "Order Channel Distribution"

    )

    print(

        orders["OrderChannel"]

        .value_counts()

        .sort_index()

    )

    print()

    print(

        "Payment Status Distribution"

    )

    print(

        orders["PaymentStatus"]

        .value_counts()

        .sort_index()

    )

    print("=" * 60)

    return orders
# ==========================================================
# Validate Orders
# ==========================================================

def validate_orders(

    orders

):

    print("=" * 60)

    print(

        "Validating Orders"

    )

    print("=" * 60)

    # ------------------------------------------------------
    # Dataset Validation
    # ------------------------------------------------------

    if orders.empty:

        raise ValueError(

            "Orders dataset is empty."

        )

    print(

        "✓ Dataset Validation Passed"

    )

    # ------------------------------------------------------
    # OrderID
    # ------------------------------------------------------

    if orders["OrderID"].duplicated().any():

        raise ValueError(

            "Duplicate OrderID found."

        )

    print(

        "✓ OrderID Validation Passed"

    )

    # ------------------------------------------------------
    # CustomerID
    # ------------------------------------------------------

    valid_customers = set(

        CUSTOMER_IDS

    )

    invalid_customer = orders.loc[

        ~orders["CustomerID"].isin(

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
    # Order Status
    # ------------------------------------------------------

    valid_status = set(

        ORDER_STATUS_DISTRIBUTION.keys()

    )

    invalid_status = orders.loc[

        ~orders["OrderStatus"].isin(

            valid_status

        )

    ]

    if not invalid_status.empty:

        raise ValueError(

            "Invalid OrderStatus found."

        )

    print(

        "✓ Order Status Validation Passed"

    )

    # ------------------------------------------------------
    # Order Channel
    # ------------------------------------------------------

    valid_channels = set(

        ORDER_CHANNEL_DISTRIBUTION.keys()

    )

    invalid_channel = orders.loc[

        ~orders["OrderChannel"].isin(

            valid_channels

        )

    ]

    if not invalid_channel.empty:

        raise ValueError(

            "Invalid OrderChannel found."

        )

    print(

        "✓ Order Channel Validation Passed"

    )

    # ------------------------------------------------------
    # Payment Status Mapping
    # ------------------------------------------------------

    for row in orders.itertuples(index=False):

        expected_status = PAYMENT_STATUS_MAPPING[

            row.OrderStatus

        ]

        if row.PaymentStatus != expected_status:

            raise ValueError(

                f"PaymentStatus mismatch for OrderID {row.OrderID}"

            )

    print(

        "✓ Payment Status Validation Passed"

    )

    # ------------------------------------------------------
    # Delivery Dates
    # ------------------------------------------------------

    invalid_expected = orders.loc[

        orders["ExpectedDeliveryDate"] <

        orders["OrderDate"].dt.date

    ]

    if not invalid_expected.empty:

        raise ValueError(

            "ExpectedDeliveryDate earlier than OrderDate."

        )

    delivered = orders.dropna(

        subset=["DeliveredDate"]

    )

    invalid_delivered = delivered.loc[

        delivered["DeliveredDate"] <

        delivered["OrderDate"].dt.date

    ]

    if not invalid_delivered.empty:

        raise ValueError(

            "DeliveredDate earlier than OrderDate."

        )

    print(

        "✓ Delivery Date Validation Passed"

    )

    # ------------------------------------------------------
    # Delivered Orders
    # ------------------------------------------------------

    delivered_orders = orders.loc[

        orders["OrderStatus"] == "Delivered"

    ]

    if delivered_orders["DeliveredDate"].isna().any():

        raise ValueError(

            "Delivered orders must contain DeliveredDate."

        )

    print(

        "✓ Delivered Orders Validation Passed"

    )

    # ------------------------------------------------------
    # Pending Orders
    # ------------------------------------------------------

    pending = orders.loc[

        orders["OrderStatus"].isin(

            [

                "Pending",

                "Processing"

            ]

        )

    ]

    if pending["DeliveredDate"].notna().any():

        raise ValueError(

            "Pending/Processing orders cannot have DeliveredDate."

        )

    print(

        "✓ Pending Orders Validation Passed"

    )

    # ------------------------------------------------------
    # Financial Columns
    # ------------------------------------------------------

    financial_columns = [

        "TotalAmount",

        "DiscountAmount",

        "ShippingCharge",

        "TaxAmount",

        "FinalAmount"

    ]

    for column in financial_columns:

        if (orders[column] != 0).any():

            raise ValueError(

                f"{column} must remain 0.00 in Stage Orders."

            )

    print(

        "✓ Stage Financial Validation Passed"

    )

    # ------------------------------------------------------
    # Required Columns
    # ------------------------------------------------------

    required_columns = [

        "OrderID",

        "CustomerID",

        "OrderDate",

        "OrderStatus",

        "OrderChannel",

        "PaymentStatus"

    ]

    for column in required_columns:

        if orders[column].isnull().any():

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

        f"Orders             : {len(orders):,}"

    )

    print(

        f"Customers          : {orders['CustomerID'].nunique():,}"

    )

    print(

        f"Delivered          : {(orders['OrderStatus']=='Delivered').sum():,}"

    )

    print(

        f"Shipped            : {(orders['OrderStatus']=='Shipped').sum():,}"

    )

    print(

        f"Processing         : {(orders['OrderStatus']=='Processing').sum():,}"

    )

    print(

        f"Pending            : {(orders['OrderStatus']=='Pending').sum():,}"

    )

    print(

        f"Cancelled          : {(orders['OrderStatus']=='Cancelled').sum():,}"

    )

    print(

        f"Returned           : {(orders['OrderStatus']=='Returned').sum():,}"

    )

    print("=" * 60)

    return True
# ==========================================================
# Export Orders
# ==========================================================

def export_orders(

    orders

):

    print("=" * 60)

    print(

        "Exporting Orders"

    )

    print("=" * 60)

    output_file = (

        CSV_OUTPUT /

        "orders.csv"

    )

    output_file.parent.mkdir(

        parents=True,

        exist_ok=True

    )

    orders.to_csv(

        output_file,

        index=False

    )

    print(

        f"✓ File Saved : {output_file}"

    )

    print(

        f"✓ Rows Exported : {len(orders):,}"

    )

    print("=" * 60)

    return output_file


# ==========================================================
# Main
# ==========================================================

def main():

    print()

    print("=" * 70)

    print("SHOPSPHERE ANALYTICS")

    print("ORDERS GENERATOR (STAGE)")

    print("=" * 70)

    start_time = datetime.now()

    # ------------------------------------------------------
    # Generate
    # ------------------------------------------------------

    orders = generate_orders()

    # ------------------------------------------------------
    # Validate
    # ------------------------------------------------------

    validate_orders(

        orders

    )

    # ------------------------------------------------------
    # Export
    # ------------------------------------------------------

    output_file = export_orders(

        orders

    )

    # ------------------------------------------------------
    # Execution Summary
    # ------------------------------------------------------

    end_time = datetime.now()

    duration = end_time - start_time

    print()

    print("=" * 70)

    print(

        "ORDERS STAGE GENERATION COMPLETED"

    )

    print("=" * 70)

    print(

        f"Orders Generated      : {len(orders):,}"

    )

    print(

        f"Unique Customers      : {orders['CustomerID'].nunique():,}"

    )

    print()

    print("Order Status")

    print(

        orders["OrderStatus"]

        .value_counts()

        .sort_index()

    )

    print()

    print("Order Channel")

    print(

        orders["OrderChannel"]

        .value_counts()

        .sort_index()

    )

    print()

    print("Payment Status")

    print(

        orders["PaymentStatus"]

        .value_counts()

        .sort_index()

    )

    print()

    print(

        f"Output File           : {output_file}"

    )

    print(

        f"Started At            : {start_time.strftime('%Y-%m-%d %H:%M:%S')}"

    )

    print(

        f"Completed At          : {end_time.strftime('%Y-%m-%d %H:%M:%S')}"

    )

    print(

        f"Execution Time        : {duration}"

    )

    print("=" * 70)

    print()

    print(

        "Orders Stage Generator Finished Successfully."

    )


# ==========================================================
# Run Generator
# ==========================================================

if __name__ == "__main__":

    main()
    