import pandas as pd
import os

print("Loading datasets...")

# Load datasets
nasa = pd.read_csv(
    "datasets/nasa_power/Nasa Power_cleaned.csv"
)

wind = pd.read_csv(
    "datasets/global_wind_atlas/wind_features.csv"
)

srtm = pd.read_csv(
    "datasets/srtm/srtm_features.csv"
)

osm = pd.read_csv(
    "datasets/openstreetmap/osm_features.csv"
)

sentinel = pd.read_csv(
    "datasets/sentinel/sentinel_features.csv"
)


# Select important NASA POWER features
nasa_features = nasa[
    [
        "ALLSKY_SFC_SW_DWN",
        "T2M",
        "RH2M",
        "WS50M"
    ]
]


# Select important Wind Atlas features
wind_features = wind[
    [
        "wind_speed",
        "power_density"
    ]
]

# Match wind rows with NASA data size
wind_features = wind_features.iloc[:len(nasa_features)].reset_index(drop=True)


# Repeat SRTM single-row data
srtm_features = pd.DataFrame(
    {
        "mean_elevation": 
        [srtm["mean_elevation"].iloc[0]] * len(nasa_features)
    }
)


# Repeat OSM single-row data
osm_features = pd.DataFrame(
    {
        "total_roads":
        [osm["total_roads"].iloc[0]] * len(nasa_features)
    }
)


# Repeat Sentinel single-row data
sentinel_features = pd.DataFrame(
    {
        "average_pixel_value":
        [sentinel["average_pixel_value"].iloc[0]] * len(nasa_features)
    }
)


# Combine selected features
training_data = pd.concat(
    [
        nasa_features.reset_index(drop=True),
        wind_features,
        srtm_features,
        osm_features,
        sentinel_features
    ],
    axis=1
)


# Create baseline target variable
# Temporary target for first ML baseline
training_data["energy_output"] = (
    training_data["ALLSKY_SFC_SW_DWN"]
    * training_data["wind_speed"]
)


# Remove missing values
training_data = training_data.dropna()


# Create ML dataset folder
os.makedirs(
    "datasets/ml",
    exist_ok=True
)


# Save training dataset
training_data.to_csv(
    "datasets/ml/training_data.csv",
    index=False
)


print("Training dataset prepared successfully!")
print("Dataset shape:", training_data.shape)
print("\nSelected features:")
print(training_data.columns.tolist())

print("\nSample data:")
print(training_data.head())