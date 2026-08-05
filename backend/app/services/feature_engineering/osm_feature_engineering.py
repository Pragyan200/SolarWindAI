import os
import csv
import geopandas as gpd

# Project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))

# Input shapefile
INPUT_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "openstreetmap",
    "gis_osm_roads_free_1.shp"
)

# Output CSV
OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "openstreetmap",
    "osm_features.csv"
)

print("Loading OpenStreetMap roads dataset...")

gdf = gpd.read_file(INPUT_PATH)

print("Dataset loaded successfully!")

total_roads = len(gdf)
road_types = gdf["fclass"].nunique()

print("\nOSM Feature Statistics")
print("Total Roads:", total_roads)
print("Unique Road Types:", road_types)

with open(OUTPUT_PATH, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["total_roads", "unique_road_types"])
    writer.writerow([total_roads, road_types])

print("\nFeature extraction completed!")
print("Saved to:", OUTPUT_PATH)

