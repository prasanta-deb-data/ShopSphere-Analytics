"""
=========================================================
ShopSphere Analytics
load_reference.py

Loads all reference tables into SQL Server

Author : Prasanta Kumar Deb
=========================================================
"""

from pathlib import Path

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
# Reference Tables
# ==========================================================

REFERENCE_TABLES = [

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

    records = [

        tuple(row)

        for row in df.itertuples(

            index=False,

            name=None

        )

    ]

    return records

# ==========================================================
# Insert Data
# ==========================================================

def insert_data(

    cursor,

    table_name,

    df,

    columns

):

    log_info(

        f"Inserting {table_name}"

    )

    query = build_insert_query(

        table_name,

        columns

    )

    records = prepare_records(df)

    cursor.fast_executemany = True

    cursor.executemany(

        query,

        records

    )

    log_success(

        f"{len(records):,} rows inserted into {table_name}"

    )
    
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

    clear_table(

        cursor,

        table_name

    )

    insert_data(

        cursor,

        table_name,

        df,

        columns

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

        for table in REFERENCE_TABLES:

            load_table(

                connection,

                table

            )

        connection.commit()

        log_success("=" * 70)
        log_success("REFERENCE DATA IMPORT COMPLETED")
        log_success("=" * 70)

    except Exception as ex:

        if connection:

            connection.rollback()

        log_error(str(ex))

        raise

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
    
