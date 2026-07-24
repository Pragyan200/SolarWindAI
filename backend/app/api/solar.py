from fastapi import APIRouter, HTTPException
from app.services.feature_engineering.solar import SolarFeatureService

router = APIRouter(prefix="/solar", tags=["Solar"])

solar_service = SolarFeatureService()


@router.get("/features")
def get_solar_features(latitude: float, longitude: float):

    if not (-90 <= latitude <= 90):
        raise HTTPException(
            status_code=400,
            detail="Latitude must be between -90 and 90."
        )

    if not (-180 <= longitude <= 180):
        raise HTTPException(
            status_code=400,
            detail="Longitude must be between -180 and 180."
        )

    try:
        return solar_service.build_features(latitude, longitude)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))