import os
import rasterio
from rasterio.transform import rowcol


class SRTMClient:
    """Client for retrieving location-specific elevation from SRTM."""

    def __init__(self):
        project_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../..")
        )

        self.dataset_path = os.path.join(
            project_root,
            "datasets",
            "srtm",
            "india_dem_cleaned.tif"
        )

    def get_elevation(
        self,
        latitude: float,
        longitude: float
    ) -> float:
        """Return elevation in meters for the given coordinates."""

        if not -90 <= latitude <= 90:
            raise ValueError("Invalid latitude.")

        if not -180 <= longitude <= 180:
            raise ValueError("Invalid longitude.")

        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError(
                f"SRTM dataset not found: {self.dataset_path}"
            )

        with rasterio.open(self.dataset_path) as src:

            row, col = rowcol(
                src.transform,
                longitude,
                latitude
            )

            if not (
                0 <= row < src.height
                and 0 <= col < src.width
            ):
                raise ValueError(
                    "The given coordinates are outside the SRTM dataset."
                )

            elevation = src.read(
                1,
                window=((row, row + 1), (col, col + 1))
            )[0, 0]

            if src.nodata is not None and elevation == src.nodata:
                raise ValueError(
                    "No elevation data available for this location."
                )

            if elevation < 0:
                raise ValueError(
                    "Invalid elevation value."
                )

            return float(elevation)