import os
import rasterio


class GlobalWindAtlasClient:
    def __init__(self):
        # Project root:
        # C:\Users\DELL\Downloads\Github\SolarWindAI
        base_dir = r"C:\Users\DELL\Downloads\Github\SolarWindAI"

        self.wind_speed_path = os.path.join(
            base_dir,
            "datasets",
            "global_wind_atlas",
            "IND_wind-speed_100m_cleaned.tif"
        )

        self.power_density_path = os.path.join(
            base_dir,
            "datasets",
            "global_wind_atlas",
            "IND_power-density_100m_cleaned.tif"
        )

    def get_wind_data(self, latitude: float, longitude: float):
        """Return wind speed and power density for a location."""

        # Validate latitude
        if not (-90 <= latitude <= 90):
            raise ValueError("Invalid latitude.")

        # Validate longitude
        if not (-180 <= longitude <= 180):
            raise ValueError("Invalid longitude.")

        # Check wind speed file
        if not os.path.exists(self.wind_speed_path):
            raise FileNotFoundError(
                f"Wind speed dataset not found: {self.wind_speed_path}"
            )

        # Check power density file
        if not os.path.exists(self.power_density_path):
            raise FileNotFoundError(
                f"Power density dataset not found: {self.power_density_path}"
            )

        # Read wind speed
        with rasterio.open(self.wind_speed_path) as src:
            wind_value = next(src.sample([(longitude, latitude)]))[0]

        # Read power density
        with rasterio.open(self.power_density_path) as src:
            power_value = next(src.sample([(longitude, latitude)]))[0]

        # Handle NoData values
        if wind_value == src.nodata:
            wind_value = 0.0

        if power_value == src.nodata:
            power_value = 0.0

        return {
            "wind_speed": float(wind_value),
            "power_density": float(power_value)
        }