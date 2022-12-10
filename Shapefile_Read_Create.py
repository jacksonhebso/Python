##Following tasks to import, read, edit, and create ESRI shapefiles##
## Task 1 ##

import arcpy #import modules

with arcpy.da.SearchCursor("PowerLine.shp", "SHAPE@LENGTH") as cursor: #arcpy command used to access field data of powerline shape length
    print ('Opening Powerline.shp...')
    for f in cursor:
        print ('The length of the polyline is', f[0],'feet or',(f[0]/5280),'in miles.\n') #divide f[0] or shape length by 5280 to find miles


## Task 2 ##

arcpy.env.workspace = r'C:\Users\Kyle\Nikki\GEOG378\LAB8' #Set workspace

fc = 'Parcels.shp' #Define Parcels.shp

print('Opening',fc,'...')
desc = arcpy.Describe(fc) #arcpy command used to describe/define features

print('The fields for',fc, 'are:') 
for field in desc.fields: #for loop to print all fields to include field name, length, precision, and type
    fldName       = field.name
    fldWidth      = field.length  
    fldPrecision  = field.precision
    fldTypeS      = field.type    

    values = (fldName,fldTypeS,fldWidth,fldPrecision) #define value set
    fmt    = '%s: %s (%d.%d)' #format for values
    print(fmt % values)

print('\n')


## Task 3 ##

arcpy.env.overwriteOutput = True ##Set overwrite option

try:
    #Make a layer from the feature class
    arcpy.MakeFeatureLayer_management(r'C:\Users\Kyle\Nikki\GEOG378\LAB8\LAB8.gdb\Parcels','Parcels_lyr')
    print('Creating Parcels_lyr...')
    #Select all Parcels that overlap the intersect the Powerline.shp
    arcpy.SelectLayerByLocation_management('Parcels_lyr','INTERSECT', r'C:\Users\Kyle\Nikki\GEOG378\LAB8\LAB8.gdb\Powerline','','NEW_SELECTION')
    print('Running Select by Location...')
    #Write the selected features to a new feature class
    arcpy.CopyFeatures_management('Parcels_lyr', r'C:\Users\Kyle\Nikki\GEOG378\LAB8\LAB8.gdb\SelectParcels')
    #Define variables for the fields to be printed from new feature class SelectParcels
    fields = ['SITUSADDR', 'AREA']
    selection = r'C:\Users\Kyle\Nikki\GEOG378\LAB8\LAB8.gdb\SelectParcels'
    #Access fields and selection variables
    with arcpy.da.SearchCursor(selection, fields) as cursor:
        print('The parcels that intersect the Powerline.shp are:')
        for row in cursor: #print all features for each row in SelectParcels
            print(u'{0} with an area of {1} feet.'.format(row[0],row[1]))
except:
    print(arcpy.GetMessages()) #Prints runtime messages

print('\n')


## Task 4 ##

arcpy.env.overwriteOutput = True #Set overwrite option

arcpy.env.workspace = r'C:\Users\Kyle\Nikki\GEOG378\LAB8\LAB8.gdb' #Set workspace

#Create 250 ft buffer around Powerline.shp
print('Creating 250 ft buffer around Powerline.shp...')
arcpy.Buffer_analysis('Powerline', r'C:\Users\Kyle\Nikki\GEOG378\LAB8\LAB8.gdb\buffer', '250 Feet', "FULL", "ROUND", "LIST")

#Make a layer from the feature class
arcpy.MakeFeatureLayer_management(r'C:\Users\Kyle\Nikki\GEOG378\LAB8\LAB8.gdb\Parcels','Parcels_lyr')
print('Creating Parcels_lyr...')

#Select all Parcels that are within 250ft buffer of Powerline.shp
arcpy.SelectLayerByLocation_management('Parcels_lyr','COMPLETELY_WITHIN', r'C:\Users\Kyle\Nikki\GEOG378\LAB8\LAB8.gdb\buffer','','NEW_SELECTION')
print('Running Select by Location...')

#Write the selected features to a new feature class
arcpy.CopyFeatures_management('Parcels_lyr', r'C:\Users\Kyle\Nikki\GEOG378\LAB8\LAB8.gdb\BufferParcels')
print('Successfully created new feature class of selected parcels within the 250 ft powerline buffer.')





