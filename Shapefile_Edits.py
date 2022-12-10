##Follow below tasks to open, edit, create ESRI shapefiles##
## Task 1 ##

#import required modules
from osgeo import ogr
import gdalconst
import math
import sys
import os

driver = ogr.GetDriverByName('ESRI Shapefile') #Define driver as ESRI Shapefile

fn = r'PowerLine.shp' #open PowerLine.shp. If unable to open sys.exit.
dataSource = driver.Open(fn,0)
if dataSource is None:
    print ('Unable to open',fn,'.')
    sys.exit(1)
print ('Opening', fn,'...')

featurePower = dataSource.GetLayer(0).GetFeature(0) #Define variables to find length of PowerLine.shp
geometry = featurePower.GetGeometryRef()
length = geometry.Length()
x1 = geometry.GetX(0) #finding point values in LINESTRING
x2 = geometry.GetX(1)
y1 = geometry.GetY(0)
y2 = geometry.GetY(1)
x3 = geometry.GetX(2)
x4 = geometry.GetX(3)
y3 = geometry.GetY(2)
y4 = geometry.GetY(3)
d =((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 #distance calculations
d2 =((x3 - x4) ** 2 + (y3 - y4) ** 2) ** 0.5
mid = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
dist = d + d2 + mid

#print distance in length and miles from calculation above
print ('The length of', fn, 'is', length, 'in feet or', (dist / 5280), 'in miles.')


dataSource.Destroy() #Free memory for datasource

## End Task 1 ##

## Task 2 ##

driver = ogr.GetDriverByName('ESRI Shapefile') #Define driver as ESRI Shapefile

parcels = r'Parcels.shp' #open Parcels.shp. If unable to open sys.exit program.
ds = driver.Open(parcels,0)
print ('Opening', parcels,'...')
if ds is None:
    print ('Unable to open',parcels,'.')
    sys.exit(1)
   
#get the first (and only) data layer
layer = ds.GetLayer(0)
layerName = layer.GetName()
layerType = layer.GetGeomType()
layerTypeS = ogr.GeometryTypeToName(layerType)
layerCount = layer.GetFeatureCount()


print ('Shapefile of', parcels, 'is a', layerTypeS, 'layer with', layerCount, 'features.')

#get access to the layer's non-spatial info: field name, type
featureDefn = layer.GetLayerDefn()
fieldCount = featureDefn.GetFieldCount()

print ("The layer's feature definition has the following", fieldCount,"fields:")

#loop through all fields in Parcels.shp
for i in range(fieldCount):
    fieldDef = featureDefn.GetFieldDefn(i)
    fldName  = fieldDef.GetNameRef()
    fldType  = fieldDef.GetType()
    fldTypeS = fieldDef.GetFieldTypeName(fldType) #convert integer ftype to text equiv

    values = (fldName, fldTypeS)

    print(values)

## End of Task 2 ##

## Task 3 ##

print ('There are', layer.GetFeatureCount(), 'total parcels in', parcels,'.')

layer.SetSpatialFilter(featurePower.GetGeometryRef()) #set filter for powerlines that intersect parcels
intersect_count = layer.GetFeatureCount() #find feature count of Parcels.shp
feat = layer.GetFeature(i)

print ('There are', intersect_count, 'parcels in',parcels, 'intersecting the PowerLine.shp')

for feat in layer:
    print ('The addresses intersecting PowerLine.shp are' ,feat.GetField('SITUSADDR'), 'with an area of',feat.GetField('AREA'))


ds.Destroy()

## End of Task 3 ##

## Task 4 ##

DataDir = r'C:\Users\Kyle\Nikki\GEOG378\LAB7\\' #set directory of working files
Power = DataDir + 'PowerLine.shp' #set directory of Powerline.shp
Parcel = DataDir + 'Parcels.shp' #set directory of Parcels.shp

NewOutput = DataDir + 'SelectParcels.shp' #set directory for SelectParcels.shp to be created

bufferWidth = 250 #set buffer for 250 feet

driver = ogr.GetDriverByName('ESRI Shapefile') #define driver as ESRI Shapefile

powerDriver = driver.Open(Power, gdalconst.GA_ReadOnly) 
parcelDriver = driver.Open(Parcel, gdalconst.GA_ReadOnly)

#Open driver for Powerline file. If unable to open sys.exit.
if powerDriver is None:
    print('Invalid input driver for Powerlines.')
    sys.exit(1)
#Open driver for Parcels file. If unable to open sys.exit.
if parcelDriver is None:
    print('Invalid input driver for Parcels.')
    sys.exit(1)

inputDS = driver.Open(Power)
if inputDS is None:
    print('Unable to open', Power, 'file.')
    sys.exit(1)

#define variables to acquire features, geometry, counts, etc. for Powerline.shp
powerLayer = powerDriver.GetLayer(0)
powerFeature = powerLayer.GetNextFeature()
powerGeom = powerFeature.GetGeometryRef()
parcelLayer = parcelDriver.GetLayer(0)
parcelCount = parcelLayer.GetFeatureCount()

#remove previous version of inputLayer if exists
inputLayer = inputDS.GetLayer()
if os.path.exists(NewOutput):
    os.remove(NewOutput)

#Create 250ft buffer around powerline.shp. If unable to create sys.exit.
powerBuffer = powerGeom.Buffer(bufferWidth)
print('Created 250 ft buffer around', fn,'.')

try:
    outputDS = driver.CreateDataSource(NewOutput)
except:
    print('Unable to create buffer file',NewOutput,'.')
    sys.exit(1)

#Create new shapefile of Parcels within the 250ft buffer. If unable to create sys.exit.
newLayer = outputDS.CreateLayer('SelectParcels',geom_type = ogr.wkbPolygon)
if newLayer is None:
    print('Unable to create layer for buffer.')
    sys.exit(1)

newLayerDef = newLayer.GetLayerDefn()

featureID = 0 #start features with a featureID of 0

#for loop to find if parcels are within 250 ft buffer
for Parcel in parcelLayer:
    parcelGeom = Parcel.GetGeometryRef() 
    bufferContains = powerBuffer.Contains(parcelGeom) 
    names = Parcel.GetField('SITUSADDR')
    fields = (names)

    if bufferContains == True:
        try:
            newFeature = ogr.Feature(newLayerDef)
            newFeature.SetGeometry(parcelGeom)
            newFeature.SetField('SITUSADDR', names)
            newFeature.SetFID(featureID)
            newLayer.CreateFeature(newFeature)
            newFeature.Destroy()
        except:
            print('Unable to print parcel number', featureID,'to',parcels,'.')
            newFeature.Destroy()
        featureID += 1

print(featureID,'parcels have been successfully written to',parcels,'.')

#Close and free memory for features
inputDS.Destroy()
outputDS.Destroy()







