from app.services.forecasting.solar_forecasting import SolarForecastService
from app.services.forecasting.wind_forecasting import WindForecastService


class HybridForecastService:
    """
    Combines solar and wind forecasting inputs.
    """

    def __init__(self):
        self.solar = SolarForecastService()
        self.wind = WindForecastService()

    def prepare_forecast_data(self, solar_data, wind_data):
        return {
            "solar": self.solar.prepare_forecast_data(solar_data),
            "wind": self.wind.prepare_forecast_data(wind_data)
        }