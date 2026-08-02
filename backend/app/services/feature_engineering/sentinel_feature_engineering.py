import os
import csv
from PIL import Image
import numpy as np

# Project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))

# Folder containing cleaned Sentinel images
INPUT_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "sentinel",
    "SEN-2 LULC",
    "train_images",
    "train_cleaned"
)

# Output CSV
OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "sentinel",
    "sentinel_features.csv"
)

print("Loading Sentinel dataset...")

files = [f for f in os.listdir(INPUT_PATH) if f.endswith(".png")]

total_images = len(files)

# Calculate statistics using only the first 100 images
sample_size = min(100, total_images)

pixel_means = []

for file in files[:sample_size]:
    image_path = os.path.join(INPUT_PATH, file)

    img = Image.open(image_path).convert("RGB")
    arr = np.array(img, dtype=np.float32)

    pixel_means.append(arr.mean())

overall_mean = float(np.mean(pixel_means))

print("Dataset loaded successfully!")

print("\nSentinel Feature Statistics")
print("Total Images:", total_images)
print("Sample Images Used:", sample_size)
print("Average Pixel Value:", overall_mean)

with open(OUTPUT_PATH, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["total_images", "sample_images", "average_pixel_value"])
    writer.writerow([total_images, sample_size, overall_mean])

print("\nFeature extraction completed!")
print("Saved to:", OUTPUT_PATH)