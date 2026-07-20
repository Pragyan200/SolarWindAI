from app.data_sources.nasa_power import NASAPowerClient

class SolarFeatureService:
    """Service resposible for solar feature engineering."""

    def_init_(self):
    self.nasa_client=NASAPowerClient()

    def build_features(self,latitude:float,longitude:float):
        """Bulid solar features using NASA POWER data."""

        return self.nasa_client.get_solar_data(latitude,longitude)