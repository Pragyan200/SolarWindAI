import os
import geopandas as gpd

# Project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))

INPUT_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "openstreetmap",
    "gis_osm_roads_free_1.shp"
)

OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "openstreetmap",
    "gis_osm_roads_free_1_cleaned.shp"
)

print("Loading OpenStreetMap dataset...")

# Load dataset
gdf = gpd.read_file(INPUT_PATH)

print("Cleaning dataset...")

# Remove duplicate rows
gdf = gdf.drop_duplicates()

# Fill missing values
gdf["name"] = gdf["name"].fillna("Unknown")
gdf["ref"] = gdf["ref"].fillna("Unknown")

# Save cleaned dataset
gdf.to_file(OUTPUT_PATH)

print("Dataset cleaned successfully!")
print("Saved to:", OUTPUT_PATH)