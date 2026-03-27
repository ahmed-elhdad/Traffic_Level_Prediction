import joblib
import pandas as pd
import streamlit as st

st.title("🚦Traffic Prediction App")
model_path = "models/Logistic_Regression_model.pkl"
model = joblib.load(model_path)
st.subheader("Junction")
junction_button = st.checkbox("Yes")
st.markdown("Don't click if no")
if junction_button:
    junction = 1
else:
    junction = 0
date_input = st.datetime_input("📅 Date")

if st.button("Predict"):
    datetime = pd.DataFrame([{"DateTime": date_input}])
    hour = pd.to_datetime(datetime["DateTime"]).dt.hour
    day = pd.to_datetime(datetime["DateTime"]).dt.day
    month = pd.to_datetime(datetime["DateTime"]).dt.month
    dayofweek = pd.to_datetime(datetime["DateTime"]).dt.dayofweek
    data = pd.DataFrame(
        [
            {
                "Junction": junction,
                "hour": hour,
                "day": day,
                "month": month,
                "dayofweek": dayofweek,
            }
        ]
    )
    prediction_result = model.predict(data)
    if prediction_result == 0:
        result = "No Heavy Traffic Now"
    else:
        result = "Heavy Traffic Now"

    st.success(result)
