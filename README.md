# Traffic Level Prediction

## Project Overview

This project aims to predict traffic levels based on historical data using a machine learning model. It utilizes a Logistic Regression model trained on traffic data to classify whether there will be heavy traffic or not on a given date and junction. The prediction is made through a user-friendly Streamlit web application.

The model considers features such as hour, day, month, day of the week, whether it's a weekend, rush hour, and holidays to make accurate predictions.

## Folder Structure

```
Traffic_Level_Prediction/
├── requirements.txt          # Python dependencies
├── data/
│   ├── traffic_data.csv      # Raw traffic data
│   └── cleaned_traffic_data.csv  # Processed data after cleaning and feature engineering
└── src/
    ├── clean_data.py         # Script to clean and preprocess the data
    ├── feature_eng.py        # Feature engineering functions
    ├── Logistic_Regression_model.py  # Model training script
    ├── main.py               # Streamlit app for predictions
    ├── __pycache__/          # Python cache files
    └── models/
        └── Logistic_Regression_model.pkl  # Trained model file
```

## Libraries Used

The project relies on the following key Python libraries:

- ![Pandas](https://pandas.pydata.org/static/img/pandas.svg) **Pandas**: For data manipulation and analysis.
- ![Scikit-learn](https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png) **Scikit-learn**: For machine learning algorithms, specifically Logistic Regression.
- ![Streamlit](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png) **Streamlit**: For building the interactive web application.
- ![Joblib](https://joblib.readthedocs.io/en/latest/_images/joblib_logo.svg) **Joblib**: For saving and loading the trained model.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Traffic_Level_Prediction.git
   cd Traffic_Level_Prediction
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the data cleaning and feature engineering:
   ```
   python src/clean_data.py
   ```

2. Train the model:
   ```
   python src/Logistic_Regression_model.py
   ```

3. Launch the Streamlit app:
   ```
   streamlit run src/main.py
   ```

4. Open your browser and go to the provided URL to use the prediction app.

## How It Works

- The app takes a date input and junction selection.
- It extracts features like hour, day, month, day of week from the date.
- The trained Logistic Regression model predicts if there will be heavy traffic (more than 20 vehicles) or not.
- The result is displayed to the user.</content>
<parameter name="filePath">d:\work\GitHub\Traffic_Level_Prediction\README.md