import pandas as pd
import os

print("Loading dataset...")

INPUT_PATH = "datasets/nasa_power/solar_features.csv"
OUTPUT_PATH = "datasets/ml/training_data.csv"

os.makedirs("datasets/ml", exist_ok=True)

df = pd.read_csv(INPUT_PATH)

print("Dataset loaded successfully!")

print("Available columns:")
print(df.columns.tolist())

features = [
    "ALLSKY_SFC_SW_DWN",
    "T2M",
    "RH2M"
]

training_df = df[features]

training_df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("Training dataset prepared successfully!")
print("Saved at:", OUTPUT_PATH)

print(training_df.head())