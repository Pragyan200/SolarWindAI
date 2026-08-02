import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.abspath(
    os.path.join(
        BASE_DIR,
        "..",
        "..",
        "..",
        "..",
        "datasets",
        "nasa_power",
        "Nasa Power.csv",
    )
)

OUTPUT_PATH = os.path.abspath(
    os.path.join(
        BASE_DIR,
        "..",
        "..",
        "..",
        "..",
        "datasets",
        "nasa_power",
        "Nasa Power_cleaned.csv",
    )
)

print("Loading dataset...")
df = pd.read_csv(DATA_PATH)

print("Cleaning dataset...")

# Replace NASA missing values
df = df.replace(-999, pd.NA)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values with median
df = df.fillna(df.median(numeric_only=True))

# Save cleaned dataset
df.to_csv(OUTPUT_PATH, index=False)

print("Cleaning completed successfully!")
print("Cleaned dataset saved at:")
print(OUTPUT_PATH)