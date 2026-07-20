from app.services.feature_engineering.solar import SolarFeatureService
from app.services.feature_engineering.wind import WindFeatureService
from app.services.feature_engineering.terrain import TerrainFeatureService
from app.services.feature_engineering.infrastructure import InfrastructureFeatureService


class FeatureBuilder:
    """Builds all project features."""

    def __init__(self):
        self.solar_service = SolarFeatureService()
        self.wind_service = WindFeatureService()
        self.terrain_service = TerrainFeatureService()
        self.infrastructure_service = InfrastructureFeatureService()

    def build_all_features(self, latitude: float, longitude: float):
        """
        Placeholder integration point for all feature engineering services.
        """

        solar = self.solar_service.build_features(latitude, longitude)
        wind = self.wind_service.build_features(latitude, longitude)
        terrain = self.terrain_service.build_features(latitude, longitude)
        infrastructure = self.infrastructure_service.build_features(latitude, longitude)

        return {
            "solar": solar,
            "wind": wind,
            "terrain": terrain,
            "infrastructure": infrastructure,
        }