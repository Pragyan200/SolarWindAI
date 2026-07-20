class NASAPowerClient:
    """Client for accessing NASA POWER
    data."""

    def get_solar_data(self,latitude:float,
longitude:float):
        """
        
        Retrieve solar data.
        
        Inputs:
        latitude(float)
        logitude(float)


        Returns:
        Placeholder for solar dataset


        Raises:
        ConnectionError:if the data source cannot be reached.
        VauleError:if coordinates are invalid.
        FileNotFoundError:if the data is unavailable.
        """

        raise NotimplementedError("NASA POWER client is not implemented yet.")