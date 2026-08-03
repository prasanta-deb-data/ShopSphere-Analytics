"""
Common Helper Functions
"""

import random
import uuid
from config.config import RANDOM_SEED

random.seed(RANDOM_SEED)


def random_choice(values):
    """Return a random item from a list."""
    return random.choice(values)


def random_boolean(true_probability=0.5):
    """Return True/False based on probability."""
    return random.random() < true_probability


def random_percentage(min_value=0, max_value=100):
    """Random percentage."""
    return round(random.uniform(min_value, max_value), 2)


def generate_uuid():
    """Generate UUID string."""
    return str(uuid.uuid4())


def chunk_list(data, chunk_size):
    """Yield data in chunks."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]