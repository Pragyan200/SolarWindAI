import math
import requests


class OSMClient:
    """
    Client for retrieving road and accessibility
    information from OpenStreetMap.
    """

    def __init__(self):

        self.overpass_url = (
            "https://overpass-api.de/api/interpreter"
        )

        self.headers = {
            "User-Agent":
                "SolarWindAI/1.0 "
                "(renewable-energy-analysis-project)"
        }

    def get_infrastructure(
        self,
        latitude: float,
        longitude: float
    ):

        if not (-90 <= latitude <= 90):
            raise ValueError(
                "Invalid latitude."
            )

        if not (-180 <= longitude <= 180):
            raise ValueError(
                "Invalid longitude."
            )

        query = f"""
        [out:json][timeout:60];

        (
          way["highway"]
          (around:5000,{latitude},{longitude});
        );

        out geom;
        """

        try:

            response = requests.get(
                self.overpass_url,
                params={"data": query},
                headers=self.headers,
                timeout=90
            )

            response.raise_for_status()

            data = response.json()

        except requests.RequestException as e:

            raise ConnectionError(
                "Unable to connect to "
                f"OpenStreetMap: {e}"
            )

        elements = data.get(
            "elements",
            []
        )

        roads = []

        for element in elements:

            tags = element.get(
                "tags",
                {}
            )

            highway_type = tags.get(
                "highway"
            )

            geometry = element.get(
                "geometry",
                []
            )

            if highway_type:

                roads.append({
                    "type":
                        highway_type,

                    "geometry":
                        geometry
                })

        total_roads = len(roads)

        unique_road_types = len(
            set(
                road["type"]
                for road in roads
            )
        )

        # --------------------------------------------------
        # Find nearest road
        # --------------------------------------------------

        nearest_distance_km = None

        for road in roads:

            geometry = road[
                "geometry"
            ]

            for point in geometry:

                road_lat = point.get(
                    "lat"
                )

                road_lon = point.get(
                    "lon"
                )

                if (
                    road_lat is None
                    or road_lon is None
                ):
                    continue

                distance = self._haversine_distance(
                    latitude,
                    longitude,
                    road_lat,
                    road_lon
                )

                if (
                    nearest_distance_km
                    is None
                    or distance
                    < nearest_distance_km
                ):

                    nearest_distance_km = (
                        distance
                    )

        # --------------------------------------------------
        # Accessibility classification
        # --------------------------------------------------

        if nearest_distance_km is None:

            accessibility = "Poor"

        elif nearest_distance_km <= 1:

            accessibility = "Good"

        elif nearest_distance_km <= 3:

            accessibility = "Moderate"

        else:

            accessibility = "Poor"

        return {

            "total_roads":
                total_roads,

            "unique_road_types":
                unique_road_types,

            "distance_to_road":
                nearest_distance_km,

            "accessibility":
                accessibility,
        }

    @staticmethod
    def _haversine_distance(
        lat1,
        lon1,
        lat2,
        lon2
    ):

        earth_radius_km = 6371.0

        lat1_rad = math.radians(
            lat1
        )

        lat2_rad = math.radians(
            lat2
        )

        delta_lat = math.radians(
            lat2 - lat1
        )

        delta_lon = math.radians(
            lon2 - lon1
        )

        a = (
            math.sin(
                delta_lat / 2
            ) ** 2
            +
            math.cos(lat1_rad)
            *
            math.cos(lat2_rad)
            *
            math.sin(
                delta_lon / 2
            ) ** 2
        )

        c = 2 * math.atan2(
            math.sqrt(a),
            math.sqrt(1 - a)
        )

        return (
            earth_radius_km * c
        )