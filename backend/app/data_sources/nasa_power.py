import requests
from requests.exceptions import RequestException

BASE_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"


class NASAPowerClient:
    """Client for accessing NASA POWER data."""

    def get_solar_data(self, latitude: float, longitude: float):

        params = {
            "parameters": "ALLSKY_SFC_SW_DWN,T2M,RH2M,WS50M",
            "community": "RE",
            "longitude": longitude,
            "latitude": latitude,
            "start": "20240101",
            "end": "20240105",
            "format": "JSON"
        }

        try:
            response = requests.get(
                BASE_URL,
                params=params,
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            parameters = data["properties"]["parameter"]

            def average(values):
                numeric = [
                    float(v)
                    for v in values.values()
                    if v is not None and v >= 0
                ]
                return sum(numeric) / len(numeric)

            return {
                "solar_irradiance": average(parameters["ALLSKY_SFC_SW_DWN"]),
                "temperature": average(parameters["T2M"]),
                "relative_humidity": average(parameters["RH2M"]),
                "wind_speed_50m": average(parameters["WS50M"])
            }

        except RequestException as e:
            raise ConnectionError(
                f"Unable to connect to NASA POWER API: {e}"
            )