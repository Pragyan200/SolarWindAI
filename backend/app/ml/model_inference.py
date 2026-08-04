import os
import joblib
import pandas as pd


# Model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(
    BASE_DIR,
    "random_forest_energy_model.pkl"
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

FEATURE_IMPORTANCE = {
    "ALLSKY_SFC_SW_DWN": 0.482404,
    "wind_speed": 0.270685,
    "power_density": 0.217603,
    "RH2M": 0.013276,
    "WS50M": 0.010694,
    "T2M": 0.005337,
    "mean_elevation": 0.000000,
    "total_roads": 0.000000,
    "average_pixel_value": 0.000000
}


def predict_energy(features: dict) -> dict:
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


    top_features = sorted(
    FEATURE_IMPORTANCE.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]

    return {
    "energy_prediction": float(prediction[0]),
    "explanation": {
        "top_features": [feature for feature, _ in top_features],
        "message": (
            "The prediction is primarily influenced by "
            "Solar Irradiance, Wind Speed, and Power Density."
        )
    }
}