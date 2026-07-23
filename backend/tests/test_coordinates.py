import pytest

from app.spatial.coordinates import (
    validate_latitude,
    validate_longitude,
    create_coordinate,
)


def test_valid_latitude():
    assert validate_latitude(20.5) is True


def test_invalid_latitude():
    assert validate_latitude(100) is False


def test_valid_longitude():
    assert validate_longitude(85.8) is True


def test_invalid_longitude():
    assert validate_longitude(200) is False


def test_create_coordinate_invalid_latitude():
    with pytest.raises(ValueError):
        create_coordinate(100, 85)


def test_create_coordinate_invalid_longitude():
    with pytest.raises(ValueError):
        create_coordinate(20, 200)