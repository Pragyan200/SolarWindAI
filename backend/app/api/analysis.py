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
    available_land: float
):
    return pipeline.analyze_site(
        latitude,
        longitude,
        land_area,
        available_land
    )