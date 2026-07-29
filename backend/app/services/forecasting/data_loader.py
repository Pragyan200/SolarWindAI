from typing import List, Dict


class TimeSeriesDataLoader:
    """
    Loads historical renewable energy data
    and preserves chronological order.
    """

    def load_data(self, historical_data: List[Dict]) -> List[Dict]:
        """
        Sort historical data by date.
        """

        return sorted(
            historical_data,
            key=lambda x: x["date"]
        )