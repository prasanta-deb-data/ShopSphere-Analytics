"""
=========================================================
ShopSphere Analytics
calendar_generator.py

Generates:
    reference_data/calendar.csv

Author : Prasanta Kumar Deb
=========================================================
"""

from datetime import date
import pandas as pd

from config.config import REFERENCE_DATA

# =========================================================
# Date Range
# =========================================================

START_DATE = date(2023, 1, 1)
END_DATE = date(2025, 12, 31)

# =========================================================
# Load Festival Calendar
# =========================================================

festival_df = pd.read_csv(
    REFERENCE_DATA / "festival_calendar.csv"
)

festival_df["FestivalDate"] = pd.to_datetime(
    festival_df["FestivalDate"]
)

festival_lookup = {

    row["FestivalDate"].date():
    row["FestivalID"]

    for _, row in festival_df.iterrows()

}

# =========================================================
# Generate Calendar
# =========================================================

def generate_calendar():

    rows = []

    current = START_DATE

    while current <= END_DATE:

        festival_id = festival_lookup.get(current)

        rows.append({

            "DateID":
            int(current.strftime("%Y%m%d")),

            "CalendarDate":
            current,

            "DayNumber":
            current.day,

            "DayName":
            current.strftime("%A"),

            "DayOfWeek":
            current.isoweekday(),

            "WeekNumber":
            current.isocalendar().week,

            "MonthNumber":
            current.month,

            "MonthName":
            current.strftime("%B"),

            "QuarterNumber":
            ((current.month - 1) // 3) + 1,

            "QuarterName":
            f"Q{((current.month - 1)//3)+1}",

            "YearNumber":
            current.year,

            "FiscalYear":
            f"FY{current.year}-{str(current.year+1)[-2:]}"
            if current.month >= 4
            else f"FY{current.year-1}-{str(current.year)[-2:]}",

            "FiscalQuarter":

            (
                "Q1" if current.month in [4,5,6]
                else
                "Q2" if current.month in [7,8,9]
                else
                "Q3" if current.month in [10,11,12]
                else
                "Q4"
            ),

            "IsWeekend":

            int(current.weekday() >= 5),

            "IsHoliday":

            int(festival_id is not None),

            "FestivalID":

            festival_id,

            

        })

        current += pd.Timedelta(days=1)

    df = pd.DataFrame(rows)

    output = REFERENCE_DATA / "calendar.csv"

    df.to_csv(

        output,

        index=False

    )

    print("=" * 60)
    print("Calendar Generated Successfully")
    print("=" * 60)
    print(f"Rows   : {len(df)}")
    print(f"Output : {output}")
    print("=" * 60)

    return df


# =========================================================
# Main
# =========================================================

if __name__ == "__main__":

    generate_calendar()