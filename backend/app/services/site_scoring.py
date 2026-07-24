def normalize(value: float, minimum: float, maximum: float) -> float:
    """
    Normalize a value to a 0–100 scale.
    Higher values receive higher scores.
    """
    if maximum == minimum:
        return 0.0

    score = ((value - minimum) / (maximum - minimum)) * 100
    return max(0.0, min(100.0, score))


def inverse_normalize(value: float, minimum: float, maximum: float) -> float:
    """
    Normalize a value where lower values are better.
    Example: slope, distance to road, distance to grid.
    """
    if maximum == minimum:
        return 0.0

    score = ((maximum - value) / (maximum - minimum)) * 100
    return max(0.0, min(100.0, score))


def renewable_resource_score(
    solar_irradiance: float,
    wind_speed: float,
) -> float:
    solar_score = normalize(solar_irradiance, 2.0, 8.0)
    wind_score = normalize(wind_speed, 2.0, 15.0)

    return (solar_score + wind_score) / 2


def terrain_score(
    slope: float,
    elevation: float,
) -> float:
    slope_score = inverse_normalize(slope, 0.0, 45.0)
    elevation_score = normalize(elevation, 0.0, 3000.0)

    return (slope_score + elevation_score) / 2


def infrastructure_score(
    distance_to_grid: float,
    distance_to_road: float,
) -> float:
    grid_score = inverse_normalize(distance_to_grid, 0.0, 50.0)
    road_score = inverse_normalize(distance_to_road, 0.0, 50.0)

    return (grid_score + road_score) / 2


def environmental_score(environment_score: float) -> float:
    """
    Assumes the environmental score is already between 0 and 100.
    """
    return max(0.0, min(100.0, environment_score))


def economic_score(economic_value: float) -> float:
    """
    Assumes the economic score is already between 0 and 100.
    """
    return max(0.0, min(100.0, economic_value))


DEFAULT_WEIGHTS = {
    "renewable": 0.40,
    "terrain": 0.20,
    "infrastructure": 0.20,
    "environment": 0.10,
    "economic": 0.10,
}


def calculate_overall_score(
    renewable: float,
    terrain: float,
    infrastructure: float,
    environment: float,
    economic: float,
    weights: dict = DEFAULT_WEIGHTS,
) -> dict:
    """
    Calculate the overall site suitability score.
    Returns category scores and the overall score.
    """

    overall = (
        renewable * weights["renewable"]
        + terrain * weights["terrain"]
        + infrastructure * weights["infrastructure"]
        + environment * weights["environment"]
        + economic * weights["economic"]
    )

    return {
        "renewable_score": round(renewable, 2),
        "terrain_score": round(terrain, 2),
        "infrastructure_score": round(infrastructure, 2),
        "environmental_score": round(environment, 2),
        "economic_score": round(economic, 2),
        "overall_score": round(overall, 2),
    }


def rank_candidate_sites(sites: list) -> list:
    """
    Rank candidate sites by overall score (highest first).
    """

    return sorted(
        sites,
        key=lambda site: site["overall_score"],
        reverse=True,
    )