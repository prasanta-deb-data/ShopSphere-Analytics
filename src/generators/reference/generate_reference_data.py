"""
=========================================================
ShopSphere Analytics
Generate All Reference Data
=========================================================
"""

from .states_generator import generate_states
from .cities_generator import generate_cities
from .categories_generator import generate_categories
from .brands_generator import generate_brands
from .suppliers_generator import generate_suppliers
from .warehouses_generator import generate_warehouses
from .lookup_generator import generate_lookup_tables
from .festival_generator import generate_festivals
from .calendar_generator import generate_calendar
from .names_generator import generate_names


def main():

    print("=" * 70)
    print("Generating ShopSphere Reference Data")
    print("=" * 70)

    generate_states()
    generate_cities()
    generate_categories()
    generate_brands()
    generate_suppliers()
    generate_warehouses()
    generate_lookup_tables()
    generate_festivals()
    generate_calendar()
    generate_names()

    print("\n" + "=" * 70)
    print("Reference Data Generation Completed Successfully")
    print("=" * 70)


if __name__ == "__main__":
    main()