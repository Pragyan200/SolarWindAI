from app.data_sources.srtm import SRTMClient


class TerrainFeatureService:
    """Service responsible for terrain feature engineering."""

    def __init__(self):
        self.srtm_client = SRTMClient()

    def build_features(self, latitude: float, longitude: float):
        """
        Build terrain features using SRTM elevation data.
        """
        return self.srtm_client.get_elevation_data(latitude, longitude)