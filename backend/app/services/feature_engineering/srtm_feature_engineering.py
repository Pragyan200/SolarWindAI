import os
import csv
import rasterio
import numpy as np

# Project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))

# Input file
INPUT_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "srtm",
    "india_dem_cleaned.tif"
)

# Output file
OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "srtm",
    "srtm_features.csv"
)

print("Loading cleaned SRTM dataset...")

with rasterio.open(INPUT_PATH) as src:
    elevation = src.read(1)

print("Dataset loaded successfully!")

# Keep only valid elevations
valid = elevation[(elevation >= 0) & (elevation <= 9000)]

print("\nSRTM Feature Statistics")
print("Minimum Elevation:", float(np.min(valid)))
print("Maximum Elevation:", float(np.max(valid)))
print("Mean Elevation:", float(np.mean(valid)))

# Save summary features
with open(OUTPUT_PATH, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["min_elevation", "max_elevation", "mean_elevation"])
    writer.writerow([
        float(np.min(valid)),
        float(np.max(valid)),
        float(np.mean(valid))
    ])

print("\nFeature extraction completed!")
print("Saved to:", OUTPUT_PATH)