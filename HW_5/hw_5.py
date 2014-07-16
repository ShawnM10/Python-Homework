import os
import arcpy    

arcpy.env.workspace = "C:/Users/samuse6610/Desktop/Python/Data/Exercise05"
outWorkspace = "P:/Python/ch6.gdb"
fclist = arcpy.ListFeatureClasses("")

for fc in fclist:
    desc = arcpy.Describe(feature)
    print("{} is a {}".format(desc.name, desc.shapeType))
    if desc.shapeType == 'Polygon':
        print('it is a polygon')
        outFeatureClass = os.path.join(outWorkspace, fc.strip(".shp"))
        arcpy.CopyFeatures_management(fc, outFeatureClass)

