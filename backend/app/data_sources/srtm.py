import os
import math
import rasterio
from rasterio.transform import rowcol


class SRTMClient:
    """
    Client for retrieving elevation and slope
    from the SRTM Digital Elevation Model.
    """

    def __init__(self):
        project_root = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "../../.."
            )
        )

        self.dataset_path = os.path.join(
            project_root,
            "datasets",
            "srtm",
            "india_dem_cleaned.tif"
        )

    def _validate_coordinates(
        self,
        latitude: float,
        longitude: float
    ):
        if not -90 <= latitude <= 90:
            raise ValueError("Invalid latitude.")

        if not -180 <= longitude <= 180:
            raise ValueError("Invalid longitude.")

    def get_elevation(
        self,
        latitude: float,
        longitude: float
    ) -> float:
        """
        Return elevation in meters
        for the given coordinates.
        """

        self._validate_coordinates(
            latitude,
            longitude
        )

        if not os.path.exists(
            self.dataset_path
        ):
            raise FileNotFoundError(
                f"SRTM dataset not found: "
                f"{self.dataset_path}"
            )

        with rasterio.open(
            self.dataset_path
        ) as src:

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
                    "The given coordinates are "
                    "outside the SRTM dataset."
                )

            elevation = src.read(
                1,
                window=(
                    (row, row + 1),
                    (col, col + 1)
                )
            )[0, 0]

            if (
                src.nodata is not None
                and elevation == src.nodata
            ):
                raise ValueError(
                    "No elevation data available "
                    "for this location."
                )

            if elevation < 0:
                raise ValueError(
                    "Invalid elevation value."
                )

            return float(elevation)

    def get_terrain_data(
        self,
        latitude: float,
        longitude: float
    ) -> dict:
        """
        Return elevation and slope for
        the selected coordinates.

        Slope is calculated using neighboring
        DEM pixels around the selected point.
        """

        self._validate_coordinates(
            latitude,
            longitude
        )

        if not os.path.exists(
            self.dataset_path
        ):
            raise FileNotFoundError(
                f"SRTM dataset not found: "
                f"{self.dataset_path}"
            )

        with rasterio.open(
            self.dataset_path
        ) as src:

            row, col = rowcol(
                src.transform,
                longitude,
                latitude
            )

            # Make sure a 3x3 neighborhood exists.
            if (
                row < 1
                or col < 1
                or row >= src.height - 1
                or col >= src.width - 1
            ):
                raise ValueError(
                    "Not enough SRTM data around "
                    "this location to calculate slope."
                )

            window = (
                (row - 1, row + 2),
                (col - 1, col + 2)
            )

            elevation_grid = src.read(
                1,
                window=window
            )

            nodata = src.nodata

            if nodata is not None:
                if (
                    elevation_grid == nodata
                ).any():
                    raise ValueError(
                        "No elevation data available "
                        "around this location."
                    )

            center_elevation = float(
                elevation_grid[1, 1]
            )

            if center_elevation < 0:
                raise ValueError(
                    "Invalid elevation value."
                )

            # Pixel size in degrees.
            pixel_width = abs(
                src.transform.a
            )

            pixel_height = abs(
                src.transform.e
            )

            # Convert approximately from degrees
            # to meters at the selected latitude.
            latitude_meters = (
                111320.0
            )

            longitude_meters = (
                111320.0
                * math.cos(
                    math.radians(latitude)
                )
            )

            dx = (
                pixel_width
                * longitude_meters
            )

            dy = (
                pixel_height
                * latitude_meters
            )

            if dx <= 0 or dy <= 0:
                raise ValueError(
                    "Invalid SRTM pixel resolution."
                )

            # Horn's method for terrain gradient.
            dz_dx = (
                (
                    elevation_grid[0, 2]
                    + 2 * elevation_grid[1, 2]
                    + elevation_grid[2, 2]
                )
                -
                (
                    elevation_grid[0, 0]
                    + 2 * elevation_grid[1, 0]
                    + elevation_grid[2, 0]
                )
            ) / (8 * dx)

            dz_dy = (
                (
                    elevation_grid[2, 0]
                    + 2 * elevation_grid[2, 1]
                    + elevation_grid[2, 2]
                )
                -
                (
                    elevation_grid[0, 0]
                    + 2 * elevation_grid[0, 1]
                    + elevation_grid[0, 2]
                )
            ) / (8 * dy)

            slope_radians = math.atan(
                math.sqrt(
                    dz_dx ** 2
                    + dz_dy ** 2
                )
            )

            slope_degrees = math.degrees(
                slope_radians
            )

            return {
                "elevation": center_elevation,
                "slope": float(
                    slope_degrees
                )
            }