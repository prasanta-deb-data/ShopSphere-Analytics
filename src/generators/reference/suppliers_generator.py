"""
=========================================================
ShopSphere Analytics
suppliers_generator.py

Generates:
    reference_data/suppliers.csv
=========================================================
"""

import random
import string
import pandas as pd
from faker import Faker

from config.config import REFERENCE_DATA

fake = Faker("en_IN")

# --------------------------------------------------------
# Company Prefix
# --------------------------------------------------------

PREFIXES = [

    "Tech",
    "Global",
    "Prime",
    "National",
    "Metro",
    "Star",
    "Elite",
    "Royal",
    "Future",
    "United",
    "Modern",
    "Shree",
    "Sai",
    "Om",
    "Apex"

]

# --------------------------------------------------------
# Company Suffix
# --------------------------------------------------------

SUFFIXES = [

    "Distributors",

    "Wholesalers",

    "Trading",

    "Enterprises",

    "Private Limited",

    "Industries",

    "Suppliers",

    "Corporation",

    "Retail Supply",

    "Solutions"

]

# --------------------------------------------------------
# Load Cities
# --------------------------------------------------------

cities = pd.read_csv(

    REFERENCE_DATA / "cities.csv"

)

# --------------------------------------------------------
# GST Number
# --------------------------------------------------------

def generate_gst():

    state_code = random.randint(10,99)

    pan = ''.join(

        random.choices(

            string.ascii_uppercase,

            k=5

        )

    )

    pan += ''.join(

        random.choices(

            string.digits,

            k=4

        )

    )

    pan += random.choice(

        string.ascii_uppercase

    )

    return f"{state_code}{pan}1Z5"

# --------------------------------------------------------
# Generate Suppliers
# --------------------------------------------------------

def generate_suppliers(

        total=250

):

    rows=[]

    for supplier_id in range(

        1,

        total+1

    ):

        city = cities.sample(1).iloc[0]

        company = (

            random.choice(PREFIXES)

            + " "

            + fake.last_name()

            + " "

            + random.choice(SUFFIXES)

        )

        contact = fake.name()

        email = (

            company.lower()

            .replace(" ","")

            .replace(".","")

            + "@gmail.com"

        )

        rows.append({

            "SupplierID":supplier_id,

            "SupplierName":company,

            "ContactPerson":contact,

            "Email":email,

            "Phone":fake.phone_number(),

            "CityID":city.CityID,

            "GSTNumber":generate_gst(),

            "IsActive":1

        })

    df=pd.DataFrame(rows)

    output=REFERENCE_DATA/"suppliers.csv"

    df.to_csv(

        output,

        index=False

    )

    print("="*60)
    print("Suppliers Generated")
    print("="*60)
    print(df.shape)
    print(output)

    return df

# --------------------------------------------------------
# Main
# --------------------------------------------------------

if __name__=="__main__":

    generate_suppliers()