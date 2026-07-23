"""
Configurable constraint thresholds.
"""

MAX_SLOPE = 15.0
MIN_SOLAR_IRRADIANCE = 4.5
MIN_WIND_SPEED = 5.0
MAX_GRID_DISTANCE = 10.0
MAX_ROAD_DISTANCE = 5.0


def check_slope(slope: float) -> bool:
    """Return True if the slope is within the allowable limit."""
    return slope <= MAX_SLOPE


def check_solar_irradiance(solar_irradiance: float) -> bool:
    """Return True if solar irradiance meets the minimum threshold."""
    return solar_irradiance >= MIN_SOLAR_IRRADIANCE


def check_wind_speed(wind_speed: float) -> bool:
    """Return True if wind speed meets the minimum threshold."""
    return wind_speed >= MIN_WIND_SPEED


def check_grid_distance(grid_distance: float) -> bool:
    """Return True if grid distance is within the allowable limit."""
    return grid_distance <= MAX_GRID_DISTANCE


def check_road_distance(road_distance: float) -> bool:
    """Return True if road distance is within the allowable limit."""
    return road_distance <= MAX_ROAD_DISTANCE