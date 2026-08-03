"""
Pricing Utilities
"""

import random

from config.config import (
    MIN_MARGIN,
    MAX_MARGIN,
    GST_RATE
)


def calculate_selling_price(cost_price):
    margin = random.uniform(MIN_MARGIN, MAX_MARGIN)
    return round(cost_price * (1 + margin), 2)


def calculate_mrp(selling_price):
    return round(selling_price * 1.08, 2)


def calculate_tax(amount):
    return round(amount * GST_RATE, 2)


def calculate_discount(mrp, selling_price):
    return round(mrp - selling_price, 2)