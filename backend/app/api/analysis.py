from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.analysis_pipeline import AnalysisPipeline


router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)


# ============================================================
# REQUEST MODEL
# ============================================================
# Frontend only needs to send latitude and longitude.
# Everything else is obtained automatically or given a
# safe default inside the backend.
# ============================================================

class AnalysisRequest(BaseModel):

    latitude: float = Field(
        ...,
        ge=-90,
        le=90
    )

    longitude: float = Field(
        ...,
        ge=-180,
        le=180
    )


# ============================================================
# PIPELINE
# ============================================================

pipeline = AnalysisPipeline()


# ============================================================
# ANALYZE SITE
# ============================================================

@router.post("/")
def analyze_analysis(request: AnalysisRequest):

    try:

        # ----------------------------------------------------
        # Values that are NOT available directly from the
        # frontend are handled here.
        # ----------------------------------------------------

        # Average land area assumption
        land_area = 10.0

        # Usable portion of the land
        available_land = 8.0

        # Default environmental restriction
        restricted_land = False

        # Slope is NOT taken from frontend.
        # AnalysisPipeline obtains it from SRTM.
        slope = 0.0

        # Distance to grid is not currently obtained from
        # an external dataset, therefore use a fixed value.
        distance_to_grid = 5.0

        # These two are overwritten by OSM inside the pipeline.
        distance_to_road = 0.0
        accessibility = "Unknown"

        # Financial assumptions
        electricity_tariff = 5.0

        cost_per_mw = 5000000.0

        additional_installation_percentage = 0.0


        # ----------------------------------------------------
        # RUN ANALYSIS
        # ----------------------------------------------------

        result = pipeline.analyze_site(

            latitude=request.latitude,

            longitude=request.longitude,

            land_area=land_area,

            available_land=available_land,

            restricted_land=restricted_land,

            slope=slope,

            distance_to_grid=distance_to_grid,

            distance_to_road=distance_to_road,

            accessibility=accessibility,

            electricity_tariff=electricity_tariff,

            cost_per_mw=cost_per_mw,

            additional_installation_percentage=(
                additional_installation_percentage
            ),
        )

        return result


    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


    except FileNotFoundError as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


    except ConnectionError as e:

        raise HTTPException(
            status_code=503,
            detail=str(e)
        )


    except Exception as e:

        # This gives a useful error instead of a blank
        # "Internal Server Error".
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(e)}"
        )