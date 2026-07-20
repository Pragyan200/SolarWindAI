from app.data_sources.global_wind_atlas import GlobalWindAtlasClient


class WindFeatureService:
    """Service responsible for wind feature engineering."""

    def __init__(self):
        self.wind_client = GlobalWindAtlasClient()

    def build_features(self, latitude: float, longitude: float):
        """
        Build wind features using Global Wind Atlas data.
        """
        return self.wind_client.get_wind_data(latitude, longitude)