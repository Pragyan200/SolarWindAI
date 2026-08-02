import os
import geopandas as gpd

# Path to the OSM Roads dataset
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))

DATA_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "openstreetmap",
    "gis_osm_roads_free_1.shp"
)

print("----- OPENSTREETMAP DATASET -----")
print("Dataset Path:", DATA_PATH)

# Load dataset
gdf = gpd.read_file(DATA_PATH)

print("\n----- FIRST 5 ROWS -----")
print(gdf.head())

print("\n----- DATASET SHAPE -----")
print(gdf.shape)

print("\n----- COLUMN NAMES -----")
print(gdf.columns.tolist())

print("\n----- DATA TYPES -----")
print(gdf.dtypes)

print("\n----- MISSING VALUES -----")
print(gdf.isnull().sum())

print("\n----- CRS -----")
print(gdf.crs)