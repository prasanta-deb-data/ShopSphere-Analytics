"""
=========================================================
ShopSphere Analytics
states_generator.py

Generates:
    reference_data/states.csv

Author : Prasanta Kumar Deb
=========================================================
"""

from pathlib import Path
import pandas as pd

from config.config import REFERENCE_DATA

# --------------------------------------------------------
# Indian States & Union Territories
# --------------------------------------------------------

STATES = [

    # ---------------- North ----------------
    ("JK", "Jammu and Kashmir", "North", "State"),
    ("HP", "Himachal Pradesh", "North", "State"),
    ("PB", "Punjab", "North", "State"),
    ("HR", "Haryana", "North", "State"),
    ("UK", "Uttarakhand", "North", "State"),
    ("UP", "Uttar Pradesh", "North", "State"),
    ("DL", "Delhi", "North", "Union Territory"),
    ("CH", "Chandigarh", "North", "Union Territory"),

    # ---------------- West ----------------
    ("RJ", "Rajasthan", "West", "State"),
    ("GJ", "Gujarat", "West", "State"),
    ("MH", "Maharashtra", "West", "State"),
    ("GA", "Goa", "West", "State"),
    ("DN", "Dadra and Nagar Haveli and Daman and Diu", "West", "Union Territory"),

    # ---------------- South ----------------
    ("KA", "Karnataka", "South", "State"),
    ("KL", "Kerala", "South", "State"),
    ("TN", "Tamil Nadu", "South", "State"),
    ("AP", "Andhra Pradesh", "South", "State"),
    ("TS", "Telangana", "South", "State"),
    ("PY", "Puducherry", "South", "Union Territory"),
    ("LD", "Lakshadweep", "South", "Union Territory"),

    # ---------------- East ----------------
    ("WB", "West Bengal", "East", "State"),
    ("BR", "Bihar", "East", "State"),
    ("JH", "Jharkhand", "East", "State"),
    ("OD", "Odisha", "East", "State"),

    # ---------------- Central ----------------
    ("MP", "Madhya Pradesh", "Central", "State"),
    ("CG", "Chhattisgarh", "Central", "State"),

    # ---------------- North-East ----------------
    ("AS", "Assam", "North-East", "State"),
    ("AR", "Arunachal Pradesh", "North-East", "State"),
    ("ML", "Meghalaya", "North-East", "State"),
    ("MN", "Manipur", "North-East", "State"),
    ("MZ", "Mizoram", "North-East", "State"),
    ("NL", "Nagaland", "North-East", "State"),
    ("TR", "Tripura", "North-East", "State"),
    ("SK", "Sikkim", "North-East", "State"),

    # ---------------- Islands ----------------
    ("AN", "Andaman and Nicobar Islands", "Islands", "Union Territory"),
    ("LA", "Ladakh", "North", "Union Territory")
]

# --------------------------------------------------------
# Generate DataFrame
# --------------------------------------------------------

def generate_states():

    records = []

    for idx, (code, name, region, state_type) in enumerate(STATES, start=1):

        records.append({

            "StateID": idx,

            "StateCode": code,

            "StateName": name,

            "Region": region,

            "StateType": state_type,

            "IsActive": 1

        })

    df = pd.DataFrame(records)

    output_path = REFERENCE_DATA / "states.csv"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print("=" * 60)
    print("States Generated Successfully")
    print("=" * 60)
    print(f"Rows     : {len(df)}")
    print(f"Output   : {output_path}")
    print("=" * 60)

    return df


# --------------------------------------------------------
# Main
# --------------------------------------------------------

if __name__ == "__main__":
    generate_states()