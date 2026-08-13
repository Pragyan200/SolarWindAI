import requests


class OSMClient:
    def __init__(self):
        self.overpass_url = "https://overpass-api.de/api/interpreter"

        self.headers = {
            "User-Agent": "SolarWindAI/1.0 (renewable-energy-analysis-project)"
        }

    def get_infrastructure(self, latitude: float, longitude: float):
        """
        Get road/infrastructure information from OpenStreetMap
        using the Overpass API.
        """

        if not (-90 <= latitude <= 90):
            raise ValueError("Invalid latitude.")

        if not (-180 <= longitude <= 180):
            raise ValueError("Invalid longitude.")

        query = f"""
        [out:json][timeout:60];

        (
          way["highway"](around:5000,{latitude},{longitude});
        );

        out tags;
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
                f"Unable to connect to OpenStreetMap: {e}"
            )

        elements = data.get("elements", [])

        roads = []

        for element in elements:
            tags = element.get("tags", {})

            highway_type = tags.get("highway")

            if highway_type:
                roads.append(highway_type)

        total_roads = len(roads)
        unique_road_types = len(set(roads))

        return {
            "total_roads": total_roads,
            "unique_road_types": unique_road_types
        }