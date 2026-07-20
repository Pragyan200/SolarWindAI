class GlobalWindAtlasClient:
    """Client for accessing Global Wind Atlas data."""

    def get_wind_data(self,latitude:float,
longitude:float):
        """
        Retrieve wind data
        
        inputs:
        latitude(float)
        longitude(float)
        
        
        Returns:
        Placeholder for Wind dataset.
        
        
        Raises:
        ConnectionError:if the data source cannot be reached.
        VauleError:if coordinates are invalid.
        FileNotFoundError:if the data is unavailable.
        """
        raise NotImplementedError("Global Wind Atlas client is not implemented yet.")