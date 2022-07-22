import sys
sys.path.append('.')

import rasterio                  # I/O raster data (netcdf, height, geotiff, ...)
import rasterio.mask
import rasterio.warp             # Reproject raster samples
import rasterio.merge
from rasterio.transform import rowcol
import fiona                     # I/O vector data (shape, geojson, ...)
import pyproj                    # Change coordinate reference system
import geopandas as gps
import pandas as pd
import shapely
from shapely.geometry import box, Point
import json

import numpy as np               # numerical array manipulation
import time
import os
from PIL import Image
import PIL.ImageDraw
from core.visualize import display_images
from core.frame_info import image_normalize

import matplotlib.pyplot as plt  # plotting tools
from tqdm import tqdm
import warnings                  # ignore annoying warnings --> lol this is really bad practice @Ankit
#warnings.filterwarnings("ignore")

from config import Preprocessing
# In case you are using a different folder name such as configLargeCluster, then you should import from the respective folder 
# Eg. from configLargeCluster import Preprocessing

config = Preprocessing.Configuration()

