import os
import rasterio
import numpy as np
import pandas as pd

# Project root directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))

# Cleaned datasets
WIND_SPEED_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "global_wind_atlas",
    "IND_wind-speed_100m_cleaned.tif"
)

POWER_DENSITY_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "global_wind_atlas",
    "IND_power-density_100m_cleaned.tif"
)

print("Loading cleaned Global Wind Atlas datasets...")

# Read raster files
with rasterio.open(WIND_SPEED_PATH) as src:
    wind_speed = src.read(1)

with rasterio.open(POWER_DENSITY_PATH) as src:
    power_density = src.read(1)

print("Datasets loaded successfully!")

# Flatten arrays
wind_speed = wind_speed.flatten()
power_density = power_density.flatten()

# Create feature table
features = pd.DataFrame({
    "wind_speed": wind_speed,
    "power_density": power_density
})

# Remove invalid values
features = features.replace([np.inf, -np.inf], np.nan)
features = features.dropna()

print("\nFirst 5 rows:")
print(features.head())

# Save features
OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "global_wind_atlas",
    "wind_features.csv"
)

features.to_csv(OUTPUT_PATH, index=False)

print("\nFeature extraction completed!")
print("Saved to:", OUTPUT_PATH)