"""
=========================================================
ShopSphere Analytics
load_reference.py

Loads all reference tables into SQL Server

Author : Prasanta Kumar Deb
=========================================================
"""

from pathlib import Path
import math
import pandas as pd
import pyodbc

from config.config import (
    CSV_OUTPUT,
    SQL_SERVER,
    DATABASE_NAME,
    ODBC_DRIVER
)

from src.etl.logger import (
    log_info,
    log_success,
    log_error
)

from src.etl.validation import (
    validate_csv
)

from src.etl.schema_reader import (
    get_table_schema
)
from config.config import REFERENCE_DATA
# ==========================================================
# SQL Server Connection
# ==========================================================

def get_connection():

    connection = pyodbc.connect(

        f"DRIVER={{{ODBC_DRIVER}}};"

        f"SERVER={SQL_SERVER};"

        f"DATABASE={DATABASE_NAME};"

        "Trusted_Connection=yes;"

        "TrustServerCertificate=yes;"

    )

    return connection

# ==========================================================
# Load Order (Parent → Child)
# ==========================================================

LOAD_ORDER = [

    "States",

    "Cities",

    "Categories",

    "SubCategories",

    "Brands",

    "Suppliers",

    "Warehouses",

    "PaymentMethods",

    "Couriers",

    "ReturnReasons",

    "SupportIssues",

    "FestivalCalendar",

    "Calendar"

]

# ==========================================================
# Delete Order (Child → Parent)
# ==========================================================

DELETE_ORDER = [

    "Calendar",

    "FestivalCalendar",

    "SupportIssues",

    "ReturnReasons",

    "Couriers",

    "PaymentMethods",

    "Warehouses",

    "Suppliers",

    "Brands",

    "SubCategories",

    "Categories",

    "Cities",

    "States"

]

# ==========================================================
# CSV File Path
# ==========================================================

REFERENCE_FILES = {

    "States": "states.csv",
    "Cities": "cities.csv",
    "Categories": "categories.csv",
    "SubCategories": "subcategories.csv",
    "Brands": "brands.csv",
    "Suppliers": "suppliers.csv",
    "Warehouses": "warehouses.csv",
    "PaymentMethods": "payment_methods.csv",
    "Couriers": "couriers.csv",
    "ReturnReasons": "return_reasons.csv",
    "SupportIssues": "support_issues.csv",
    "FestivalCalendar": "festival_calendar.csv",
    "Calendar": "calendar.csv"

}

def get_csv_path(table_name):

    return REFERENCE_DATA / REFERENCE_FILES[table_name]

# ==========================================================
# Clear Table
# ==========================================================

def clear_table(cursor, table_name):

    log_info(f"Clearing {table_name}")

    cursor.execute(

        f"DELETE FROM {table_name}"

    )

    log_success(f"{table_name} cleared")
    
# ==========================================================
# Build Insert Query
# ==========================================================

def build_insert_query(table_name, columns):

    column_string = ", ".join(columns)

    placeholders = ", ".join(

        "?"

        for _ in columns

    )

    query = (

        f"INSERT INTO {table_name}"

        f" ({column_string}) "

        f"VALUES ({placeholders})"

    )

    return query

# ==========================================================
# Prepare Records
# ==========================================================

def prepare_records(df):

    df = df.astype(object)

    df = df.where(pd.notnull(df), None)

    return list(
        df.itertuples(
            index=False,
            name=None
        )
    )

# ==========================================================
# Insert Data
# ==========================================================

def insert_data(
    cursor,
    table_name,
    df,
    columns,
    schema,
):

    log_info(f"Inserting {table_name}")

    query = build_insert_query(
        table_name,
        columns
    )

    records = prepare_records(df)

    cursor.fast_executemany = False

    # --------------------------------------------
    # Enable IDENTITY_INSERT if required
    # --------------------------------------------

    has_identity = len(schema["identity_columns"]) > 0

    if has_identity:

        cursor.execute(
            f"SET IDENTITY_INSERT {table_name} ON"
        )

    for i, record in enumerate(records, start=1):

        try:

            cursor.execute(
                query,
                record
            )

        except Exception as ex:

            print("\n" + "=" * 70)
            print(f"FAILED TABLE : {table_name}")
            print(f"FAILED ROW   : {i}")
            print(record)
            print("=" * 70)

            raise

    if has_identity:

        cursor.execute(
            f"SET IDENTITY_INSERT {table_name} OFF"
        )

    log_success(
        f"{len(records):,} rows inserted into {table_name}"
    )
    
# ==========================================================
# Clear Reference Tables
# ==========================================================

def clear_reference_tables(connection):

    log_info("=" * 60)
    log_info("Clearing Reference Tables")
    log_info("=" * 60)

    cursor = connection.cursor()

    for table in DELETE_ORDER:

        log_info(f"Clearing {table}")

        cursor.execute(

            f"DELETE FROM {table}"

        )

        log_success(f"{table} cleared")

    cursor.close()
# ==========================================================
# Load Single Table
# ==========================================================

def load_table(connection, table_name):

    log_info("=" * 60)
    log_info(f"Loading {table_name}")
    log_info("=" * 60)

    csv_path = get_csv_path(table_name)

    # ----------------------------------------------

    df = validate_csv(

        file_path=csv_path,

        table_name=table_name

    )

    # ----------------------------------------------

    schema = get_table_schema(

        table_name

    )

    columns = schema["load_columns"]

    df = df[columns]

    # ----------------------------------------------

    cursor = connection.cursor()

    insert_data(

    cursor,

    table_name,

    df,

    columns,

    schema

)

    cursor.close()

    log_success(

        f"{table_name} Loaded Successfully"

    )
# ==========================================================
# Load Reference Data
# ==========================================================

def load_reference_data():

    connection = None

    try:

        log_info("=" * 70)
        log_info("REFERENCE DATA ETL STARTED")
        log_info("=" * 70)

        connection = get_connection()

        # --------------------------------------------------
        # Clear all reference tables (Child → Parent)
        # --------------------------------------------------

        clear_reference_tables(connection)

        connection.commit()

        log_success("All Reference Tables Cleared")

        # --------------------------------------------------
        # Load all reference tables (Parent → Child)
        # --------------------------------------------------

        for table in LOAD_ORDER:

            try:

                load_table(

                    connection,

                    table

                )

                connection.commit()

                log_success(

                    f"{table} committed."

                )

            except Exception as ex:

                connection.rollback()

                log_error(

                    f"{table} failed."

                )

                log_error(

                    str(ex)

                )

                raise

        log_success("=" * 70)
        log_success("REFERENCE DATA IMPORT COMPLETED")
        log_success("=" * 70)

    finally:

        if connection:

            connection.close()

            log_info(

                "Database Connection Closed"

            )
# ==========================================================
# Main
# ==========================================================

def main():

    load_reference_data()


if __name__ == "__main__":

    main()
    
