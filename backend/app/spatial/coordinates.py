from dataclasses import dataclass


@dataclass
class Coordinate:
    latitude: float
    longitude: float


def validate_latitude(latitude: float) -> bool:
    """Return True if latitude is between -90 and 90."""
    return -90 <= latitude <= 90


def validate_longitude(longitude: float) -> bool:
    """Return True if longitude is between -180 and 180."""
    return -180 <= longitude <= 180


def create_coordinate(latitude: float, longitude: float) -> Coordinate:
    """
    Validate latitude and longitude and return a Coordinate object.
    Raises ValueError if either coordinate is invalid.
    """
    if not validate_latitude(latitude):
        raise ValueError("Invalid latitude. Must be between -90 and 90.")

    if not validate_longitude(longitude):
        raise ValueError("Invalid longitude. Must be between -180 and 180.")

    return Coordinate(latitude=latitude, longitude=longitude)