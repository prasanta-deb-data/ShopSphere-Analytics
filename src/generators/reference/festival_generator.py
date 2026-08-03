"""
=========================================================
ShopSphere Analytics
festival_generator.py

Generates:
    reference_data/festival_calendar.csv

Author : Prasanta Kumar Deb
=========================================================
"""

import pandas as pd

from config.config import REFERENCE_DATA

# =========================================================
# Festival Data (2023–2025)
# =========================================================

FESTIVALS = [

    # =====================================================
    # 2023
    # =====================================================

    {
        "FestivalName": "New Year",
        "FestivalDate": "2023-01-01",
        "FestivalType": "National",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Republic Day",
        "FestivalDate": "2023-01-26",
        "FestivalType": "National",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Holi",
        "FestivalDate": "2023-03-08",
        "FestivalType": "Religious",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Independence Day",
        "FestivalDate": "2023-08-15",
        "FestivalType": "National",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Raksha Bandhan",
        "FestivalDate": "2023-08-30",
        "FestivalType": "Cultural",
        "IsNationalHoliday": 0,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Ganesh Chaturthi",
        "FestivalDate": "2023-09-19",
        "FestivalType": "Religious",
        "IsNationalHoliday": 0,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Navratri",
        "FestivalDate": "2023-10-15",
        "FestivalType": "Religious",
        "IsNationalHoliday": 0,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Dussehra",
        "FestivalDate": "2023-10-24",
        "FestivalType": "Religious",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Diwali",
        "FestivalDate": "2023-11-12",
        "FestivalType": "Religious",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 1
    },

    {
        "FestivalName": "Christmas",
        "FestivalDate": "2023-12-25",
        "FestivalType": "Religious",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    # =====================================================
    # 2024
    # =====================================================

    {
        "FestivalName": "New Year",
        "FestivalDate": "2024-01-01",
        "FestivalType": "National",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Republic Day",
        "FestivalDate": "2024-01-26",
        "FestivalType": "National",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Holi",
        "FestivalDate": "2024-03-25",
        "FestivalType": "Religious",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Independence Day",
        "FestivalDate": "2024-08-15",
        "FestivalType": "National",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Raksha Bandhan",
        "FestivalDate": "2024-08-19",
        "FestivalType": "Cultural",
        "IsNationalHoliday": 0,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Ganesh Chaturthi",
        "FestivalDate": "2024-09-07",
        "FestivalType": "Religious",
        "IsNationalHoliday": 0,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Navratri",
        "FestivalDate": "2024-10-03",
        "FestivalType": "Religious",
        "IsNationalHoliday": 0,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Dussehra",
        "FestivalDate": "2024-10-12",
        "FestivalType": "Religious",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Diwali",
        "FestivalDate": "2024-11-01",
        "FestivalType": "Religious",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 1
    },

    {
        "FestivalName": "Christmas",
        "FestivalDate": "2024-12-25",
        "FestivalType": "Religious",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    # =====================================================
    # 2025
    # =====================================================

    {
        "FestivalName": "New Year",
        "FestivalDate": "2025-01-01",
        "FestivalType": "National",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Republic Day",
        "FestivalDate": "2025-01-26",
        "FestivalType": "National",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Holi",
        "FestivalDate": "2025-03-14",
        "FestivalType": "Religious",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Independence Day",
        "FestivalDate": "2025-08-15",
        "FestivalType": "National",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Raksha Bandhan",
        "FestivalDate": "2025-08-09",
        "FestivalType": "Cultural",
        "IsNationalHoliday": 0,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Ganesh Chaturthi",
        "FestivalDate": "2025-08-27",
        "FestivalType": "Religious",
        "IsNationalHoliday": 0,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Navratri",
        "FestivalDate": "2025-09-22",
        "FestivalType": "Religious",
        "IsNationalHoliday": 0,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Dussehra",
        "FestivalDate": "2025-10-02",
        "FestivalType": "Religious",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    {
        "FestivalName": "Diwali",
        "FestivalDate": "2025-10-20",
        "FestivalType": "Religious",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 1
    },

    {
        "FestivalName": "Christmas",
        "FestivalDate": "2025-12-25",
        "FestivalType": "Religious",
        "IsNationalHoliday": 1,
        "IsShoppingEvent": 0
    },

    # Shopping Events
    {
        "FestivalName": "Big Billion Days",
        "FestivalDate": "2025-09-25",
        "FestivalType": "Shopping",
        "IsNationalHoliday": 0,
        "IsShoppingEvent": 1
    },

    {
        "FestivalName": "Great Indian Festival",
        "FestivalDate": "2025-10-01",
        "FestivalType": "Shopping",
        "IsNationalHoliday": 0,
        "IsShoppingEvent": 1
    }

]

# =========================================================
# Generate CSV
# =========================================================

def generate_festivals():

    df = pd.DataFrame(FESTIVALS)

    df.insert(0, "FestivalID", range(1, len(df) + 1))

    output = REFERENCE_DATA / "festival_calendar.csv"

    output.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output, index=False)

    print("=" * 60)
    print("Festival Calendar Generated Successfully")
    print("=" * 60)
    print(f"Rows   : {len(df)}")
    print(f"Output : {output}")
    print("=" * 60)

    return df


if __name__ == "__main__":
    generate_festivals()