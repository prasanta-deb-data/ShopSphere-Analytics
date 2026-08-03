"""
CSV Loaders
"""

import pandas as pd
from config.config import REFERENCE_DATA


def load_csv(file_name):
    path = REFERENCE_DATA / file_name
    return pd.read_csv(path)


def load_categories():
    return load_csv("categories.csv")


def load_subcategories():
    return load_csv("subcategories.csv")


def load_brands():
    return load_csv("brands.csv")


def load_suppliers():
    return load_csv("suppliers.csv")


def load_states():
    return load_csv("states.csv")


def load_cities():
    return load_csv("cities.csv")


def load_payment_methods():
    return load_csv("payment_methods.csv")


def load_couriers():
    return load_csv("couriers.csv")


def load_return_reasons():
    return load_csv("return_reasons.csv")


def load_support_issues():
    return load_csv("support_issues.csv")