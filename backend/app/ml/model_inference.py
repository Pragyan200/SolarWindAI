import os
import joblib
import pandas as pd


# Model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(
    BASE_DIR,
    "best_energy_model.pkl"
)


# Load model once when this module is imported
model = joblib.load(MODEL_PATH)


# Feature order must match training data
REQUIRED_FEATURES = [
    "ALLSKY_SFC_SW_DWN",
    "T2M",
    "RH2M",
    "WS50M",
    "wind_speed",
    "power_density",
    "mean_elevation",
    "total_roads",
    "average_pixel_value"
]


def predict_energy(features: dict) -> float:
    """
    Predict energy output using trained Random Forest model.
    """

    # Check missing features
    missing_features = [
        feature
        for feature in REQUIRED_FEATURES
        if feature not in features
    ]

    if missing_features:
        raise ValueError(
            f"Missing required features: {missing_features}"
        )


    # Arrange input in the same order as training
    input_data = pd.DataFrame(
        [[features[feature] for feature in REQUIRED_FEATURES]],
        columns=REQUIRED_FEATURES
    )


    # Generate prediction
    prediction = model.predict(input_data)


    return float(prediction[0])