import os
import joblib
import pandas as pd


# ---------------------------------------------------------
# Model path
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "random_forest_energy_model.pkl"
)


# ---------------------------------------------------------
# Load trained model
# ---------------------------------------------------------

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model file not found: {MODEL_PATH}"
    )

model = joblib.load(MODEL_PATH)


# ---------------------------------------------------------
# Features must exactly match training
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


def predict_energy(features: dict) -> dict:
    """
    Predict energy output using the trained model.
    """

    # -----------------------------------------------------
    # Check for missing features
    # -----------------------------------------------------

    missing_features = [
        feature
        for feature in REQUIRED_FEATURES
        if feature not in features
    ]

    if missing_features:
        raise ValueError(
            f"Missing required features: {missing_features}"
        )

    # -----------------------------------------------------
    # Arrange features in training order
    # -----------------------------------------------------

    input_data = pd.DataFrame(
        [[features[feature] for feature in REQUIRED_FEATURES]],
        columns=REQUIRED_FEATURES
    )

    # -----------------------------------------------------
    # Generate prediction
    # -----------------------------------------------------

    prediction = model.predict(input_data)

    # -----------------------------------------------------
    # Get feature importance directly from trained model
    # -----------------------------------------------------

    if hasattr(model, "feature_importances_"):

        importance = dict(
            zip(
                REQUIRED_FEATURES,
                model.feature_importances_
            )
        )

        top_features = sorted(
            importance.items(),
            key=lambda x: x[1],
            reverse=True
        )[:3]

        top_feature_names = [
            feature
            for feature, _ in top_features
        ]

    else:
        top_feature_names = []

    # -----------------------------------------------------
    # Return prediction
    # -----------------------------------------------------

    return {
        "energy_prediction": float(prediction[0]),
        "explanation": {
            "top_features": top_feature_names,
            "message": (
                "Prediction is based on location-specific "
                "solar, wind, elevation, and infrastructure data."
            )
        }
    }