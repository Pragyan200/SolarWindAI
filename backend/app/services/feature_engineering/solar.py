from app.data_sources.nasa_power import NASAPowerClient

class SolarFeatureService:
    """Service responsible for solar feature engineering."""

    def __init__(self):
        self.nasa_client = NASAPowerClient()

    def build_features(self, latitude: float, longitude: float):
        """Build solar features using NASA POWER data."""

        return self.nasa_client.get_solar_data(latitude, longitude)