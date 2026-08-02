import os
import rasterio
import numpy as np

# Project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))

# Input and output paths
INPUT_PATH = os.path.join(BASE_DIR, "datasets", "srtm", "india_dem.tif")
OUTPUT_PATH = os.path.join(BASE_DIR, "datasets", "srtm", "india_dem_cleaned.tif")

print("Loading SRTM dataset...")

with rasterio.open(INPUT_PATH) as src:
    data = src.read(1)
    profile = src.profile

print("Replacing NoData (-32768) with 0...")
data[data == -32768] = 0

with rasterio.open(OUTPUT_PATH, "w", **profile) as dst:
    dst.write(data, 1)

print("Dataset cleaned successfully!")
print("Saved to:", OUTPUT_PATH)