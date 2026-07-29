from datetime import datetime


class TimeFeatureExtractor:
    """
    Extracts time-based features from a date.
    """

    def extract_features(self, date_str: str) -> dict:
        """
        Extract year, month, day,
        day of year, and week number.
        """

        date = datetime.strptime(date_str, "%Y-%m-%d")

        return {
            "year": date.year,
            "month": date.month,
            "day": date.day,
            "day_of_year": date.timetuple().tm_yday,
            "week_number": date.isocalendar().week
        }