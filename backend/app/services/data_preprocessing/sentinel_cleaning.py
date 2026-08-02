import os
from PIL import Image

# Project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))

INPUT_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "sentinel",
    "SEN-2 LULC",
    "train_images",
    "train"
)

OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "sentinel",
    "SEN-2 LULC",
    "train_images",
    "train_cleaned"
)

# Create output folder
os.makedirs(OUTPUT_PATH, exist_ok=True)

print("Loading Sentinel dataset...")
print("Input Path:", INPUT_PATH)

count = 0
removed = 0

for file in os.listdir(INPUT_PATH):

    if file.endswith(".png"):

        try:
            image_path = os.path.join(INPUT_PATH, file)

            img = Image.open(image_path)

            # Ensure RGB format
            img = img.convert("RGB")

            # Save cleaned image
            output_file = os.path.join(OUTPUT_PATH, file)
            img.save(output_file)

            count += 1

        except Exception:
            removed += 1
            print("Removed corrupted file:", file)


print("\nSentinel cleaning completed!")
print("Images processed:", count)
print("Corrupted images removed:", removed)
print("Saved to:", OUTPUT_PATH)