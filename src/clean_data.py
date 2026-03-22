import pandas as pd

df = pd.read_csv("../data/traffic_data.csv")
df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df.drop(["ID"], inplace=True, axis=1)
df["hour"] = pd.to_datetime(df["DateTime"]).dt.hour
df["day"] = pd.to_datetime(df["DateTime"]).dt.day
df["month"] = pd.to_datetime(df["DateTime"]).dt.month
df["dayofweek"] = pd.to_datetime(df["DateTime"]).dt.dayofweek
df.to_csv("../data/cleaned_traffic_data.csv", index=False)
print("Cleaned Successfully")
