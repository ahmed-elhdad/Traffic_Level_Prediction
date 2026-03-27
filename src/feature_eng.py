import pandas as pd

data = pd.read_csv("../data/cleaned_traffic_data.csv")


def feature_eng():
    data["hour"] = pd.to_datetime(data["DateTime"]).dt.hour
    data["day"] = pd.to_datetime(data["DateTime"]).dt.day
    data["month"] = pd.to_datetime(data["DateTime"]).dt.month
    data["dayofweek"] = pd.to_datetime(data["DateTime"]).dt.dayofweek
    finish_and_go_work_times = [10, 12, 14, 16, 17]
    data["is_weekend"] = data["dayofweek"].apply(lambda x: 1 if x in [5, 6] else 0)
    data["rush_hour"] = data["hour"].apply(
        lambda x: 1 if x in finish_and_go_work_times else 0
    )
    holidays = {(1, 1), (3, 31), (7, 4), (11, 11), (12, 25)}

    data["is_holiday"] = list(zip(data["month"], data["day"]))
    data["is_holiday"] = data["is_holiday"].apply(lambda x: 1 if x in holidays else 0)
    data.to_csv("../data/cleaned_traffic_data.csv", index=False)
