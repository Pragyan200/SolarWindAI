def calculate_wind_class(wind_speed: float) -> str:
    """
    Classify wind resource based on average wind speed (m/s).
    """

    if wind_speed < 3:
        return "Poor"
    elif wind_speed < 5:
        return "Moderate"
    elif wind_speed < 7:
        return "Good"
    else:
        return "Excellent"

    
def calculate_capacity_factor(wind_speed: float) -> float:
    """
    Estimate wind turbine capacity factor based on average wind speed.
    Returns a value between 0 and 1.
    """

    if wind_speed < 3:
        return 0.10
    elif wind_speed < 5:
        return 0.25
    elif wind_speed < 7:
        return 0.40
    else:
        return 0.55


def classify_wind_site(wind_speed: float) -> dict:
    """
    Return a complete wind assessment for a site.
    """

    wind_class = calculate_wind_class(wind_speed)
    capacity_factor = calculate_capacity_factor(wind_speed)

    return {
        "wind_speed": wind_speed,
        "wind_class": wind_class,
        "capacity_factor": capacity_factor
    }