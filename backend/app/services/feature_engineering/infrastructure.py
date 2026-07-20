from app.data_sources.osm import OSMClient


class InfrastructureFeatureService:
    """Service responsible for infrastructure feature engineering."""

    def __init__(self):
        self.osm_client = OSMClient()

    def build_features(self, latitude: float, longitude: float):
        """
        Build infrastructure features using OpenStreetMap data.
        """
        return self.osm_client.get_infrastructure_data(latitude, longitude)