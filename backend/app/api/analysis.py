from fastapi import APIRouter

from app.services.analysis_pipeline import AnalysisPipeline


router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)

pipeline = AnalysisPipeline()


@router.post("/")
def analyze(
    latitude: float,
    longitude: float,
    land_area: float,
    available_land: float,
    restricted_land: bool,
    slope: float,
    distance_to_grid: float,
    distance_to_road: float,
    accessibility: str,
    electricity_tariff: float,
    cost_per_mw: float,
    additional_installation_percentage: float = 0.0
):
    return pipeline.analyze_site(
        latitude,
        longitude,
        land_area,
        available_land,
        restricted_land,
        slope,
        distance_to_grid,
        distance_to_road,
        accessibility,
        electricity_tariff,
        cost_per_mw,
        additional_installation_percentage
    )