from app.services.forecasting.data_loader import TimeSeriesDataLoader
from app.services.forecasting.feature_extraction import TimeFeatureExtractor


class SolarForecastService:
    """
    Forecasting pipeline for solar energy.
    """

    def __init__(self):
        self.loader = TimeSeriesDataLoader()
        self.extractor = TimeFeatureExtractor()

    def prepare_forecast_data(self, historical_data):
        """
        Prepare historical data for forecasting.
        """

        data = self.loader.load_data(historical_data)

        prepared_data = []

        for record in data:
            features = self.extractor.extract_features(record["date"])

            prepared_data.append({
                **record,
                **features
            })

        return prepared_data