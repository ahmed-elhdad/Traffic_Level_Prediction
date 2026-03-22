from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
import pandas as pd

data = pd.read_csv("../data/cleaned_traffic_data.csv")

X = data[["hour", "day", "month", "dayofweek", "is_weekend", "rush_hour", "is_holiday"]]
y = data["Traffic"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

numeric = ["hour", "day", "month", "dayofweek"]

transformer = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric),
    ],
    remainder="drop",
)

pipeline = Pipeline(
    [
        ("prep", transformer),
        ("clf", LogisticRegression(class_weight="balanced", random_state=42)),
    ]
)

param_grid = {
    "clf__C": [
        0.001,
    ],
}

grid_model = GridSearchCV(pipeline, param_grid, cv=2, n_jobs=-1, scoring="f1_weighted")
grid_model.fit(X_train, y_train)

y_pred = grid_model.predict(X_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(grid_model.score(X_test, y_test) * 100)
