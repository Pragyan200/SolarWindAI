import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor


# Dataset path
data_path = "datasets/ml/training_data.csv"

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

# -----------------------------
# Random Forest Regressor
# -----------------------------
print("\nTraining Random Forest Regressor...")

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_pred)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
rf_r2 = r2_score(y_test, rf_pred)

# -----------------------------
# XGBoost Regressor
# -----------------------------
print("Training XGBoost Regressor...")

xgb_model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)

xgb_model.fit(X_train, y_train)

xgb_pred = xgb_model.predict(X_test)

xgb_mae = mean_absolute_error(y_test, xgb_pred)
xgb_rmse = np.sqrt(mean_squared_error(y_test, xgb_pred))
xgb_r2 = r2_score(y_test, xgb_pred)

# -----------------------------
# Comparison Table
# -----------------------------
print("\nModel Comparison")
print("-" * 65)
print(f"{'Model':<25}{'MAE':<12}{'RMSE':<12}{'R2 Score'}")
print("-" * 65)
print(f"{'Random Forest':<25}{rf_mae:<12.4f}{rf_rmse:<12.4f}{rf_r2:.4f}")
print(f"{'XGBoost':<25}{xgb_mae:<12.4f}{xgb_rmse:<12.4f}{xgb_r2:.4f}")
print("-" * 65)



# Create folder if it doesn't exist
os.makedirs("backend/app/ml", exist_ok=True)

# Save the selected model
model_path = "backend/app/ml/random_forest_energy_model.pkl"

joblib.dump(rf_model, model_path)

print("\nSelected model saved successfully!")
print("Saved location:", model_path)