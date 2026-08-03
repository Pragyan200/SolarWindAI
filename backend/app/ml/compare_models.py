import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Dataset path
data_path = "datasets/ml/training_data.csv"

# Model save path
model_path = "backend/app/ml/best_energy_model.pkl"


print("Loading dataset...")

df = pd.read_csv(data_path)


# Features and target
X = df.drop("energy_output", axis=1)
y = df["energy_output"]


# Split dataset:
# 70% Training, 15% Validation, 15% Testing

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


print("Dataset split completed")
print("Training:", X_train.shape)
print("Validation:", X_val.shape)
print("Testing:", X_test.shape)


# Models

models = {
    "Decision Tree": DecisionTreeRegressor(
        random_state=42
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )
}


results = {}
trained_models = {}


# Training and validation

for name, model in models.items():

    print("\nTraining:", name)

    model.fit(
        X_train,
        y_train
    )

    y_pred = model.predict(
        X_val
    )


    mae = mean_absolute_error(
        y_val,
        y_pred
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_val,
            y_pred
        )
    )

    r2 = r2_score(
        y_val,
        y_pred
    )


    results[name] = {
        "MAE": mae,
        "RMSE": rmse,
        "R2 Score": r2
    }

    trained_models[name] = model


# Comparison table

comparison = pd.DataFrame(results).T

print("\nModel Comparison:")
print(comparison)


# Select best model using R2 score

best_model_name = comparison["R2 Score"].idxmax()

best_model = trained_models[best_model_name]


print("\nBest Model:", best_model_name)


# Test performance

test_prediction = best_model.predict(X_test)

test_r2 = r2_score(
    y_test,
    test_prediction
)

print("Test R2 Score:", test_r2)


# Save best model

os.makedirs(
    "backend/app/ml",
    exist_ok=True
)

joblib.dump(
    best_model,
    model_path
)


print("\nBest model saved successfully!")
print("Saved at:", model_path)