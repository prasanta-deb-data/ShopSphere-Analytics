"""
Date Utilities
"""

import random
from datetime import datetime, timedelta

from config.config import START_DATE, END_DATE

start_date = datetime.strptime(START_DATE, "%Y-%m-%d")
end_date = datetime.strptime(END_DATE, "%Y-%m-%d")


def random_date():
    delta = end_date - start_date
    return start_date + timedelta(days=random.randint(0, delta.days))


def random_datetime():
    d = random_date()

    return d.replace(
        hour=random.randint(0, 23),
        minute=random.randint(0, 59),
        second=random.randint(0, 59)
    )


def random_birth_date(min_age=18, max_age=70):
    today = datetime.today()

    age = random.randint(min_age, max_age)

    return today - timedelta(days=age * 365)