from sqlalchemy.orm import Session

from app.models.feature import Feature
from app.schemas.feature import FeatureCreate


class FeatureStoreService:
    def __init__(self, db: Session):
        self.db = db

    def save_feature(self, feature: FeatureCreate):
        db_feature = Feature(
            latitude=feature.latitude,
            longitude=feature.longitude,
            solar_irradiance=feature.solar_irradiance,
            wind_speed=feature.wind_speed,
            temperature=feature.temperature,
            humidity=feature.humidity,
            elevation=feature.elevation,
            slope=feature.slope,
        )

        self.db.add(db_feature)
        self.db.commit()
        self.db.refresh(db_feature)

        return db_feature
    

    def get_all_features(self):
        return self.db.query(Feature).all()
    

    def get_feature_by_location(self, latitude: float, longitude: float):
        return (
            self.db.query(Feature)
            .filter(
                Feature.latitude == latitude,
                Feature.longitude == longitude
            )
            .first()
        )
    
    def get_feature_by_id(self, feature_id: int):
        return self.db.query(Feature).filter(Feature.id == feature_id).first()