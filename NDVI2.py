from osgeo import gdal
gdal.UseExceptions()
import numpy as np
import sys


redband = gdal.Open ('L71026029_02920000609_B30_CLIP.tif')
if redband is None:
    print ('Unable to open file.')
    sys.exit(1)

r = np.array(redband.GetRasterBand(1).ReadAsArray(), dtype = float)

nirband = gdal.Open('L71026029_02920000609_B40_CLIP.tif')
if nirband is None:
    print ('Unable to open file.')
    sys.exit(1)

n = np.array(nirband.GetRasterBand(1).ReadAsArray(), dtype = float)

tableshape = r.shape
ndvi = (n - r)/(n + r)

drv = gdal.GetDriverByName ('GTiff')
dst_ds = drv.Create ('test.tif', tableshape[1], tableshape[0], 1, gdal.GDT_Float32)
dst_ds.GetRasterBand(1).WriteArray(ndvi)
dst_ds = None
print ('The NDVI image is saved.')
