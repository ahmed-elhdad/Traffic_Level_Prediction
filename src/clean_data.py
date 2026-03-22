import pandas as pd


df = pd.read_csv("../data/traffic_data.csv")
holidays_dates = [
    {"month": 1, "day": 1},
    {"month": 3, "day": 31},
    {"month": 7, "day": 4},
    {"month": 11, "day": 11},
    {"month": 12, "day": 25},
]


def check_public_holidays(day, month):
    for date in holidays_dates:
        if date["month"] == month and date["day"] == day:
            return 1
    return 0


finish_and_go_work_times = [10, 12, 14, 16, 17]


def clean_data():

    df.columns = df.columns.str.strip()
    # Feature Engineering
    df["hour"] = pd.to_datetime(df["DateTime"]).dt.hour
    df["day"] = pd.to_datetime(df["DateTime"]).dt.day
    df["month"] = pd.to_datetime(df["DateTime"]).dt.month
    df["dayofweek"] = pd.to_datetime(df["DateTime"]).dt.dayofweek
    df["cars_count"] = df["Vehicles"]
    df["Traffic"] = df["cars_count"].apply(lambda x: 1 if x > 20 else 0)
    df["is_weekend"] = df["dayofweek"].apply(lambda x: 1 if x == 1 | 7 else 0)
    df["rush_hour"] = df["hour"].apply(
        lambda x: 1 if x in finish_and_go_work_times else 0
    )
    holidays = {(1, 1), (3, 31), (7, 4), (11, 11), (12, 25)}

    df["is_holiday"] = list(zip(df["month"], df["day"]))
    df["is_holiday"] = df["is_holiday"].apply(lambda x: 1 if x in holidays else 0)
    # Drop
    df.drop(["ID"], inplace=True, axis=1)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df.drop("DateTime", axis=1, inplace=True)
    df.drop("Vehicles", axis=1, inplace=True)

    df.to_csv("../data/cleaned_traffic_data.csv", index=False)

    print("Cleaned Successfully")


clean_data()
