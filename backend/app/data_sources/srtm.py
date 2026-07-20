class SRTMClient:
    """Client for accessing SRTM elevation data.
    data."""

    def get_elevation(self,latitude:float,
longitude:float):
        """
        
        Retrieve elevation data.
        
        Inputs:
        latitude(float)
        logitude(float)
        

        Returns:
        Placeholder for elevation dataset


        Raises:
        ConnectionError:if the data source cannot be reached.
        VauleError:if coordinates are invalid.
        FileNotFoundError:if the data is unavailable.
        """

        raise NotimplementedError("SRTM client is not implemented yet.")