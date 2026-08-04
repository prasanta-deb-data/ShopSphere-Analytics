"""
=========================================================
ShopSphere Analytics
database.py

Creates SQL Server connection using SQLAlchemy

Author : Prasanta Kumar Deb
=========================================================
"""

from sqlalchemy import create_engine
from urllib.parse import quote_plus

from config.config import (
    SQL_SERVER,
    DATABASE_NAME,
    ODBC_DRIVER,
    TRUSTED_CONNECTION
)


def get_connection_string():

    connection_string = (

        f"DRIVER={{{ODBC_DRIVER}}};"

        f"SERVER={SQL_SERVER};"

        f"DATABASE={DATABASE_NAME};"

        f"Trusted_Connection={TRUSTED_CONNECTION};"

        "TrustServerCertificate=yes;"

    )

    return connection_string


def get_engine():

    params = quote_plus(

        get_connection_string()

    )

    engine = create_engine(

        f"mssql+pyodbc:///?odbc_connect={params}",

        fast_executemany=True,

        future=True

    )

    return engine


if __name__ == "__main__":

    try:

        engine = get_engine()

        with engine.connect() as conn:

            print("=" * 60)
            print("Connected Successfully")
            print("=" * 60)

    except Exception as e:

        print("=" * 60)
        print("Connection Failed")
        print("=" * 60)
        print(e)