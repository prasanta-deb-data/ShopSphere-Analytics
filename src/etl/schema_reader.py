"""
=========================================================
ShopSphere Analytics
schema_reader.py

Reads SQL Server schema metadata for ETL

Author : Prasanta Kumar Deb
=========================================================
"""

from sqlalchemy import text

from src.etl.database import get_engine
from src.etl.logger import (
    log_info,
    log_success
)

# ==========================================================
# Audit Columns
# ==========================================================

AUDIT_COLUMNS = {

    "CreatedAt",
    "UpdatedAt"

}

# ==========================================================
# Get Complete Schema
# ==========================================================

def get_table_schema(table_name):

    log_info(f"Reading schema : {table_name}")

    engine = get_engine()

    query = text("""

    SELECT

        c.COLUMN_NAME,

        c.DATA_TYPE,

        c.IS_NULLABLE,

        COLUMNPROPERTY(
            OBJECT_ID(c.TABLE_SCHEMA + '.' + c.TABLE_NAME),
            c.COLUMN_NAME,
            'IsIdentity'
        ) AS IsIdentity,

        COLUMNPROPERTY(
            OBJECT_ID(c.TABLE_SCHEMA + '.' + c.TABLE_NAME),
            c.COLUMN_NAME,
            'IsComputed'
        ) AS IsComputed

    FROM INFORMATION_SCHEMA.COLUMNS c

    WHERE c.TABLE_NAME = :table_name

    ORDER BY c.ORDINAL_POSITION

    """)

    pk_query = text("""

    SELECT

        KU.COLUMN_NAME

    FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS TC

    INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE KU

        ON TC.CONSTRAINT_NAME = KU.CONSTRAINT_NAME

    WHERE

        TC.TABLE_NAME = :table_name

        AND TC.CONSTRAINT_TYPE='PRIMARY KEY'

    """)

    with engine.connect() as conn:

        rows = conn.execute(

            query,

            {

                "table_name": table_name

            }

        ).fetchall()

        pk = conn.execute(

            pk_query,

            {

                "table_name": table_name

            }

        ).fetchone()

    columns = []

    datatypes = {}

    nullable = {}

    identity_columns = []

    computed_columns = []

    load_columns = []

    for row in rows:

        column = row.COLUMN_NAME

        columns.append(column)

        datatypes[column] = row.DATA_TYPE

        nullable[column] = (

            row.IS_NULLABLE == "YES"

        )

        if row.IsIdentity == 1:

            identity_columns.append(column)

        if row.IsComputed == 1:

            computed_columns.append(column)

        # --------------------------------------

        if (

    column not in AUDIT_COLUMNS

    and

    row.IsComputed != 1



):

         load_columns.append(column)

    schema = {

        "table_name": table_name,

        "columns": columns,

        "load_columns": load_columns,

        "primary_key":

            pk.COLUMN_NAME

            if pk

            else None,

        "datatypes": datatypes,

        "nullable": nullable,

        "identity_columns": identity_columns,

        "computed_columns": computed_columns

    }

    log_success(

        f"{table_name} schema loaded"

    )

    return schema

# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    schema = get_table_schema(

        "States"

    )

    print("=" * 60)

    print("TABLE")

    print(schema["table_name"])

    print()

    print("ALL COLUMNS")

    print(schema["columns"])

    print()

    print("LOAD COLUMNS")

    print(schema["load_columns"])

    print()

    print("PRIMARY KEY")

    print(schema["primary_key"])

    print()

    print("IDENTITY")

    print(schema["identity_columns"])

    print()

    print("COMPUTED")

    print(schema["computed_columns"])

    print()

    print("DATATYPES")

    for k, v in schema["datatypes"].items():

        print(f"{k:<25}{v}")

    print()

    print("NULLABLE")

    for k, v in schema["nullable"].items():

        print(f"{k:<25}{v}")

    print("=" * 60)