import pandas as pd
import os
import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Dataset path
data_path = "datasets/ml/training_data.csv"

# Model save path
model_path = "backend/app/ml/random_forest_energy_model.pkl"


print("Loading training dataset...")

# Load dataset
df = pd.read_csv(data_path)


# Separate features and target
X = df.drop("energy_output", axis=1)
y = df["energy_output"]


print("Features used:")
print(X.columns.tolist())


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("Training Random Forest model...")


# Create Random Forest Regression model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)


# Train model
model.fit(
    X_train,
    y_train
)


print("Model training completed!")


# Make predictions
y_pred = model.predict(X_test)


# Evaluation metrics
mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        y_pred
    )
)

r2 = r2_score(
    y_test,
    y_pred
)


print("\nModel Performance:")
print("-------------------")
print("MAE:", mae)
print("RMSE:", rmse)
print("R² Score:", r2)


# Create folder if not available
os.makedirs(
    "backend/app/ml",
    exist_ok=True
)


# Save trained model
joblib.dump(
    model,
    model_path
)


print("\nModel saved successfully!")
print("Saved location:", model_path)