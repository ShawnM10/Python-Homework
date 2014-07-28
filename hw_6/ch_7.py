import arcpy
from arcpy import env
    env.workspace = "C:/Users/samuse6610/desktop/Python/Exercise07"
    sql1 = " \"FEATURE\" = 'Airport'"
    sql2 = " \"FEATURE\" = 'Seaplane Base'"
    arcpy.Select_analysis ("airports.shp", "Results/airports_final.shp",sql1)
    arcpy.Select_analysis ("airports.shp", "Results/seaports.shp", sql2)
    arcpy.Buffer_analysis("Results/airports_final.shp", "Results/aiports_buffers.shp", "15000 METERS")
    arcpy.Buffer_analysis("Results/seaports.shp", "Results/seaports_buffers.shp", "7500 METERS"


import arcpy
from arcpy import env
    env.workspace = "C:/Users/samuse6610/desktop/Python/Exercise07"
    fc = "roads.shp"
    arcpy.AddField_management(fc, "FERRY", "TEXT", "", "", 20)
    cursor = arcpy.da.UpdateCursor(fc, ["FEATURE", "FERRY"])
    for row in cursor:
    if row[0] == "Ferry Crossing":
        row[1] = "YES"
    else:
        row[1]= "NO"
        cursor.updateRow(row)
