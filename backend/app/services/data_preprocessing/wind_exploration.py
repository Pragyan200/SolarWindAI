import rasterio
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

WIND_FILE = os.path.abspath(
    os.path.join(
        BASE_DIR,
        "..",
        "..",
        "..",
        "..",
        "datasets",
        "global_wind_atlas",
        "IND_wind-speed_100m.tif",
    )
)

with rasterio.open(WIND_FILE) as src:
    data = src.read(1)

    print("\n----- GLOBAL WIND ATLAS DATASET -----")
    print("Width:", src.width)
    print("Height:", src.height)
    print("Bands:", src.count)
    print("Data Type:", src.dtypes)
    print("CRS:", src.crs)
    print("Resolution:", src.res)
    print("NoData Value:", src.nodata)

    print("\n----- RASTER STATISTICS -----")
    print("Minimum:", np.nanmin(data))
    print("Maximum:", np.nanmax(data))
    print("Mean:", np.nanmean(data))
    print("NaN Values:", np.isnan(data).sum())