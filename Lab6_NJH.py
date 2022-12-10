## This program creates an NDVI image from Red band and NIR band images

#import required modules for NDVI output
from osgeo import gdal
gdal.UseExceptions() #Enable exceptions in GDAL
import numpy as np 
import sys

red = 'L71026029_02920000609_B30_CLIP.tif' #define variable for red band file
try: #try to open variable red
    redband = gdal.Open(red)
    print ('Red band file is valid.')
except: #exception statement if unable to open red file
    print ('Unable to open', red,'. Program will close.')
    sys.exit(1) #program will quit if unable to find red file

#read rasterband(1) as an array and set data type to float
r = np.array(redband.GetRasterBand(1).ReadAsArray(), dtype = float)

nir = 'L71026029_02920000609_B40_CLIP.tif' #define variable for nir band file
try: #try to open variable nir
    nirband = gdal.Open(nir)
    print ('NIR file is valid.')
except: #exception statement if unable to open red file
    print ('Unable to open', nir,'. Program will close.')
    sys.exit(1) #program will quit if unable to find nir file

#read rasterband(1) as an array and set data type to float    
n = np.array(nirband.GetRasterBand(1).ReadAsArray(), dtype = float)

geotrans = redband.GetGeoTransform() #defining variable for transformation
project = redband.GetProjection() #defining variable for projection
tableshape = r.shape #defining variable for shape

ndvi = (n-r)/(n+r) #formula for NDVI
driver = gdal.GetDriverByName('GTiff') #fetch GTiff driver

#create NDVI image as OutputNDVI.tif
dst_ds = driver.Create('OutputNDVI.tif', tableshape[1], tableshape[0], 1, gdal.GDT_Float32)
dst_ds.SetGeoTransform(geotrans) #use same transformation as red band file for OutputNDVI.tif
dst_ds.SetProjection(project) #use same projection as red band file for OutputNDVI.tif
dst_ds.GetRasterBand(1).WriteArray(ndvi) #create NDVI raster
dst_ds = None # save, close

print ('The NDVI image is saved.')


