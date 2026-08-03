"""
=========================================================
ShopSphere Analytics
cities_generator.py

Generates:
    reference_data/cities.csv

Author : Prasanta Kumar Deb
=========================================================
"""

import random
import pandas as pd

from config.config import REFERENCE_DATA

# ---------------------------------------------------------
# State Name -> Major Cities
# (Expand this list over time)
# ---------------------------------------------------------

STATE_CITIES = {

    "Assam": [
        "Guwahati",
        "Silchar",
        "Dibrugarh",
        "Jorhat",
        "Tezpur",
        "Nagaon",
        "Tinsukia",
        "Bongaigaon",
        "Sivasagar",
        "Dhubri"
    ],

    "West Bengal": [
        "Kolkata",
        "Howrah",
        "Siliguri",
        "Asansol",
        "Durgapur",
        "Kharagpur",
        "Malda",
        "Haldia",
        "Bardhaman",
        "Darjeeling"
    ],

    "Maharashtra": [
        "Mumbai",
        "Pune",
        "Nagpur",
        "Nashik",
        "Aurangabad",
        "Kolhapur",
        "Solapur",
        "Thane",
        "Amravati",
        "Jalgaon"
    ],

    "Karnataka": [
        "Bengaluru",
        "Mysuru",
        "Hubli",
        "Belagavi",
        "Mangalore",
        "Shivamogga",
        "Tumakuru",
        "Ballari"
    ],

    "Tamil Nadu": [
        "Chennai",
        "Coimbatore",
        "Madurai",
        "Salem",
        "Tiruchirappalli",
        "Vellore",
        "Erode",
        "Thoothukudi"
    ],

    "Delhi": [
        "New Delhi"
    ]
}

# --------------------------------------------------------
# Load States
# --------------------------------------------------------
def load_states():

    return pd.read_csv(
        REFERENCE_DATA / "states.csv"
    )
    
# --------------------------------------------------------
# Generate Cities
# --------------------------------------------------------
def generate_cities():

    states = load_states()

    rows = []

    city_id = 1

    for _, state in states.iterrows():

        state_name = state["StateName"]

        state_id = state["StateID"]

        cities = STATE_CITIES.get(state_name, [])

        for city in cities:

            rows.append({

                "CityID": city_id,

                "StateID": state_id,

                "CityName": city,

                "Tier": random.choice([
                    "Tier 1",
                    "Tier 2",
                    "Tier 3"
                ]),

                "IsMetro": int(city in [
                    "Mumbai",
                    "Delhi",
                    "Bengaluru",
                    "Kolkata",
                    "Chennai",
                    "Hyderabad",
                    "Pune"
                ]),

                "IsActive": 1

            })

            city_id += 1

    df = pd.DataFrame(rows)

    output = REFERENCE_DATA / "cities.csv"

    df.to_csv(output, index=False)

    print("=" * 60)
    print("Cities Generated Successfully")
    print("=" * 60)
    print("Rows :", len(df))
    print("Output :", output)

    return df
# --------------------------------------------------------
# Main
# --------------------------------------------------------

if __name__ == "__main__":
    generate_cities()