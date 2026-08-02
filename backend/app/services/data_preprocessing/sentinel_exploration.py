import os
from PIL import Image
import numpy as np

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))

DATA_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "sentinel",
    "SEN-2 LULC",
    "train_images",
    "train"
)

print("----- SENTINEL DATASET -----")
print("Dataset Path:", DATA_PATH)

# Get first image
files = os.listdir(DATA_PATH)

image_file = files[0]
image_path = os.path.join(DATA_PATH, image_file)

print("\nFirst Image:", image_file)

# Load image
img = Image.open(image_path)

print("\n----- IMAGE DETAILS -----")
print("Size:", img.size)
print("Mode:", img.mode)

# Convert to array
img_array = np.array(img)

print("\n----- PIXEL STATISTICS -----")
print("Shape:", img_array.shape)
print("Minimum:", img_array.min())
print("Maximum:", img_array.max())
print("Mean:", img_array.mean())
print("Data Type:", img_array.dtype)