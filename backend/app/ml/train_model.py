import os
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from xgboost import XGBRegressor


# ---------------------------------------------------------
# Project paths
# ---------------------------------------------------------

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../..")
)

DATA_PATH = os.path.join(
    PROJECT_ROOT,
    "datasets",
    "ml",
    "training_data.csv"
)

MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "backend",
    "app",
    "ml",
    "random_forest_energy_model.pkl"
)


# ---------------------------------------------------------
# Model features
# ---------------------------------------------------------

REQUIRED_FEATURES = [
    "ALLSKY_SFC_SW_DWN",
    "T2M",
    "RH2M",
    "WS50M",
    "wind_speed",
    "power_density",
    "mean_elevation",
    "total_roads",
]

TARGET = "energy_output"


# ---------------------------------------------------------
# Load training dataset
# ---------------------------------------------------------

print("Loading training dataset...")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(
        f"Training dataset not found: {DATA_PATH}"
    )

df = pd.read_csv(DATA_PATH)

print("Dataset shape:", df.shape)


# ---------------------------------------------------------
# Validate columns
# ---------------------------------------------------------

missing_features = [
    feature
    for feature in REQUIRED_FEATURES
    if feature not in df.columns
]

if missing_features:
    raise ValueError(
        f"Missing required features: {missing_features}"
    )

if TARGET not in df.columns:
    raise ValueError(
        f"Target column '{TARGET}' not found."
    )


# ---------------------------------------------------------
# Select features and target
# ---------------------------------------------------------

X = df[REQUIRED_FEATURES].copy()
y = df[TARGET].copy()

print("\nFeatures used:")
print(X.columns.tolist())

print("\nTarget:")
print(TARGET)


# ---------------------------------------------------------
# Clean invalid values
# ---------------------------------------------------------

X = X.replace(
    [np.inf, -np.inf],
    np.nan
)

valid_rows = (
    X.notna().all(axis=1)
    & y.notna()
)

X = X.loc[valid_rows]
y = y.loc[valid_rows]

print("\nValid training rows:", len(X))


# ---------------------------------------------------------
# Train/Test split
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================================================
# Random Forest
# =========================================================

print("\nTraining Random Forest Regressor...")

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(
    X_train,
    y_train
)

rf_pred = rf_model.predict(X_test)

rf_mae = mean_absolute_error(
    y_test,
    rf_pred
)

rf_rmse = np.sqrt(
    mean_squared_error(
        y_test,
        rf_pred
    )
)

rf_r2 = r2_score(
    y_test,
    rf_pred
)


# ---------------------------------------------------------
# Feature importance
# ---------------------------------------------------------

importance_df = pd.DataFrame({
    "Feature": X_train.columns,
    "Importance": rf_model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nRandom Forest Feature Importance:")
print(importance_df)


# =========================================================
# XGBoost
# =========================================================

print("\nTraining XGBoost Regressor...")

xgb_model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)

xgb_model.fit(
    X_train,
    y_train
)

xgb_pred = xgb_model.predict(X_test)

xgb_mae = mean_absolute_error(
    y_test,
    xgb_pred
)

xgb_rmse = np.sqrt(
    mean_squared_error(
        y_test,
        xgb_pred
    )
)

xgb_r2 = r2_score(
    y_test,
    xgb_pred
)


# =========================================================
# Model comparison
# =========================================================

print("\nModel Comparison")
print("-" * 65)
print(
    f"{'Model':<25}"
    f"{'MAE':<12}"
    f"{'RMSE':<12}"
    f"{'R2 Score'}"
)
print("-" * 65)

print(
    f"{'Random Forest':<25}"
    f"{rf_mae:<12.4f}"
    f"{rf_rmse:<12.4f}"
    f"{rf_r2:.4f}"
)

print(
    f"{'XGBoost':<25}"
    f"{xgb_mae:<12.4f}"
    f"{xgb_rmse:<12.4f}"
    f"{xgb_r2:.4f}"
)

print("-" * 65)


# =========================================================
# Select and save model
# =========================================================

selected_model = rf_model

os.makedirs(
    os.path.dirname(MODEL_PATH),
    exist_ok=True
)

joblib.dump(
    selected_model,
    MODEL_PATH
)

print("\nSelected model saved successfully!")
print("Saved location:", MODEL_PATH)

print("\nFinal model features:")
print(REQUIRED_FEATURES)