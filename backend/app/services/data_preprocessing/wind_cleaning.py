import os
import rasterio
import numpy as np

# Project root directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))

# Input file
INPUT_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "global_wind_atlas",
    "IND_power-density_100m.tif"
)

# Output file
OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "global_wind_atlas",
    "IND_power-density_100m_cleaned.tif"
)

print("Loading Global Wind Atlas Power Density dataset...")

with rasterio.open(INPUT_PATH) as src:
    data = src.read(1)
    profile = src.profile

print("Replacing NaN values with 0...")
data = np.nan_to_num(data, nan=0)

with rasterio.open(OUTPUT_PATH, "w", **profile) as dst:
    dst.write(data, 1)

print("Dataset cleaned successfully!")
print("Saved to:", OUTPUT_PATH)