from app.evaluation.weights import (
    SOLAR_WEIGHT,
    WIND_WEIGHT,
    SLOPE_WEIGHT,
    GRID_DISTANCE_WEIGHT,
    ROAD_DISTANCE_WEIGHT,
)


def compute_score(features: dict) -> float:
    """
    Compute a weighted suitability score from a feature dictionary.

    Expected keys:
        solar
        wind
        slope
        grid_distance
        road_distance
    """

    score = (
        (features.get("solar", 0) * SOLAR_WEIGHT)
        + (features.get("wind", 0) * WIND_WEIGHT)
        + (features.get("slope", 0) * SLOPE_WEIGHT)
        + (features.get("grid_distance", 0) * GRID_DISTANCE_WEIGHT)
        + (features.get("road_distance", 0) * ROAD_DISTANCE_WEIGHT)
    )

    return round(score, 2)