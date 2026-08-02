import os
import numpy as np
import rasterio

# Project root
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../..")
)

# SRTM dataset path
DATA_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "srtm",
    "india_dem.tif"
)


def explore_srtm():
    print("----- SRTM DATASET -----")

    with rasterio.open(DATA_PATH) as src:
        data = src.read(1)

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


if __name__ == "__main__":
    explore_srtm()