"""
=========================================================
ShopSphere Analytics
validation.py

CSV Validation Utility

Author : Prasanta Kumar Deb
=========================================================
"""

from pathlib import Path

import pandas as pd

from src.etl.logger import (
    log_info,
    log_success,
    log_error
)

from src.etl.schema_reader import (
    get_table_schema
)


# ==========================================================
# File Validation
# ==========================================================

def validate_file(file_path):

    file_path = Path(file_path)

    if not file_path.exists():

        log_error(f"{file_path.name} not found.")

        raise FileNotFoundError(file_path)

    log_success(f"{file_path.name} found.")


# ==========================================================
# Read CSV
# ==========================================================

def read_csv(file_path):

    validate_file(file_path)

    return pd.read_csv(file_path)


# ==========================================================
# Column Validation
# ==========================================================

def validate_columns(df, table_name):

    schema = get_table_schema(table_name)

    expected = schema["load_columns"]

    csv_columns = list(df.columns)

    missing = [

        c

        for c in expected

        if c not in csv_columns

    ]

    extra = [

        c

        for c in csv_columns

        if c not in expected

    ]

    if missing:

        raise ValueError(

            f"Missing Columns : {missing}"

        )

    if extra:

        raise ValueError(

            f"Unexpected Columns : {extra}"

        )

    log_success("Column Validation Passed")
    
# ==========================================================
# Primary Key Validation
# ==========================================================
def validate_primary_key(df, table_name):

    schema = get_table_schema(table_name)

    pk = schema["primary_key"]

    if pk is None:

        return

    if df[pk].duplicated().any():

        raise ValueError(

            f"Duplicate Primary Key : {pk}"

        )

    log_success("Primary Key Validation Passed")

# ==========================================================
# Null Validation
# ==========================================================

def validate_nulls(df, table_name):

    schema = get_table_schema(table_name)

    nullable = schema["nullable"]

    for column in df.columns:

        if (

            nullable.get(column) is False

            and

            df[column].isnull().any()

        ):

            raise ValueError(

                f"Null values in {column}"

            )

    log_success("Null Validation Passed")


# ==========================================================
# Data Type Validation
# ==========================================================

SQL_TO_PANDAS = {

    "int": "Int64",

    "bigint": "Int64",

    "bit": "Int64",

    "decimal": "float64",

    "numeric": "float64",

    "float": "float64",

    "nvarchar": "object",

    "varchar": "object",

    "char": "object",

    "date": "datetime64[ns]",

    "datetime": "datetime64[ns]",

    "datetime2": "datetime64[ns]"
}
# ==========================================================
# python
# ==========================================================

def validate_datatypes(df, table_name):

    schema = get_table_schema(table_name)

    datatypes = schema["datatypes"]

    for column in df.columns:

        sql_type = datatypes[column]

        if sql_type in [

            "date",

            "datetime",

            "datetime2"

        ]:

            try:

                pd.to_datetime(

                    df[column]

                )

            except Exception:

                raise ValueError(

                    f"{column} invalid datetime"

                )

    log_success("Datatype Validation Passed")
# ==========================================================
# Complete Validation
# ==========================================================

def validate_csv(file_path, table_name):

    log_info(f"Validating {table_name}")

    df = read_csv(file_path)

    validate_columns(

        df,

        table_name

    )

    validate_primary_key(

        df,

        table_name

    )

    validate_nulls(

        df,

        table_name

    )

    validate_datatypes(

        df,

        table_name

    )

    log_success(

        f"{table_name} validation completed"

    )

    return df