import os
import pandas as pd

# Project root directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))

# Cleaned NASA POWER dataset
DATA_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "nasa_power",
    "Nasa Power_cleaned.csv"
)

print("Loading cleaned NASA POWER dataset...")

# Load dataset
df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")

# Select useful features
features = [
    "ALLSKY_SFC_SW_DWN",
    "T2M",
    "RH2M"
]

available_features = [col for col in features if col in df.columns]

feature_df = df[available_features]

print("\nSelected Features:")
print(feature_df.head())

# Save extracted features
OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "nasa_power",
    "solar_features.csv"
)

feature_df.to_csv(OUTPUT_PATH, index=False)

print("\nFeature extraction completed!")
print("Saved to:", OUTPUT_PATH)