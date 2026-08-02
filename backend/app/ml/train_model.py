import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("Loading training dataset...")

# Load dataset
df = pd.read_csv("datasets/ml/training_data.csv")

# Remove missing values
df = df.dropna()

print("Dataset loaded successfully!")

# Features
X = df[["T2M", "RH2M"]]

# Target
y = df["ALLSKY_SFC_SW_DWN"]

# -----------------------------
# Dataset Split
# 70% Train
# 15% Validation
# 15% Test
# -----------------------------

X_train, X_temp, y_train, y_temp = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp,
    y_temp,
    test_size=0.50,
    random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Validation samples: {len(X_val)}")
print(f"Testing samples: {len(X_test)}")

# -----------------------------
# Train Decision Tree
# -----------------------------

print("\nTraining Decision Tree...")

dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train, y_train)

print("Decision Tree trained successfully!")

# -----------------------------
# Train Random Forest
# -----------------------------

print("\nTraining Random Forest...")

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

print("Random Forest trained successfully!")

# -----------------------------
# Training Performance
# -----------------------------

dt_train_pred = dt_model.predict(X_train)
rf_train_pred = rf_model.predict(X_train)

dt_train_r2 = r2_score(y_train, dt_train_pred)
rf_train_r2 = r2_score(y_train, rf_train_pred)

# -----------------------------
# Validation Performance
# -----------------------------

dt_val_pred = dt_model.predict(X_val)
rf_val_pred = rf_model.predict(X_val)

dt_mae = mean_absolute_error(y_val, dt_val_pred)
dt_rmse = mean_squared_error(y_val, dt_val_pred) ** 0.5
dt_r2 = r2_score(y_val, dt_val_pred)

rf_mae = mean_absolute_error(y_val, rf_val_pred)
rf_rmse = mean_squared_error(y_val, rf_val_pred) ** 0.5
rf_r2 = r2_score(y_val, rf_val_pred)

# -----------------------------
# Results
# -----------------------------

print("\n========== TRAINING RESULTS ==========")
print("Decision Tree Training R2 :", dt_train_r2)
print("Random Forest Training R2:", rf_train_r2)

print("\n========== VALIDATION RESULTS ==========")

print("\nDecision Tree")
print("MAE :", dt_mae)
print("RMSE:", dt_rmse)
print("R2  :", dt_r2)

print("\nRandom Forest")
print("MAE :", rf_mae)
print("RMSE:", rf_rmse)
print("R2  :", rf_r2)

# -----------------------------
# Save Best Model
# -----------------------------

joblib.dump(rf_model, "backend/app/ml/random_forest_model.pkl")

print("\nBest model (Random Forest) saved successfully!")