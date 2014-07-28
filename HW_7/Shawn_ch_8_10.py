import arcpy
from arcpy import env
env.workspace = "C:/Data"
fc = "newpoly2.shp"
arcpy.CreateFeatureclass_management("C:/Data", fc, "Polygon")
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array = arcpy.Array()
coordlist =[[0, 0], [0, 1000], [1000, 1000], [1000, 0]]
for x, y in coordlist:
    point = arcpy.Point(x,y)
    array.append(point)
    polygon = arcpy.Polygon(array)
    cursor.insertRow([polygon])
del cursor

import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise08"
fc = "Hawaii.shp"
newfc = "Results/Hawaii_single.shp"
arcpy.MultipartToSinglepart_management(fc, newfc)
spatialref = arcpy.Describe(newfc).spatialReference
unit = spatialref.linearUnitName
cursor = arcpy.da.SearchCursor(newfc, ["SHAPE@"])
for row in cursor:
    print ("{0} square {1}".format(row[0].area, unit))





import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise10"
mxd = arcpy.mapping.MapDocument("C:/EsriPress/Python/Data/Exercise10/
Austin_TX.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Parks")[0]
lyr = arcpy.mapping.ListLayers(mxd, "parks", df)[0]
dflist = arcpy.mapping.ListDataFrames(mxd)
for dframe in dflist:
if dframe.name <> "Parks":
    arcpy.mapping.AddLayer(dframe, lyr)
    mxd.save()
del mxd







