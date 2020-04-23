import arceditor
#import pandas as pd
#import numpy as np
#import time
#import datetime
#from datetime import datetime, timedelta
#from datetime import date
import arcpy, re, os, errno
from arcpy import env
#import subprocess
#import shutil
#from shutil import copyfile
arcpy.SetLogHistory(False)
arcpy.env.overwriteOutput = True


metric = "ADA"
metricmoniker = "ADA"
mxdpath = r"C:\IOT2\Kickoff\Appr_ADA.mxd"
sourcegdb = "C:\\IOT2\\IOT2_KickoffData.gdb"

rootpath = r"C:"
topfolder = r"\IOT2"
secondfolder = r"\Deliverables"
filegdb = r"\IOT2.gdb"
shapefolder = "Shapefiles"

bridgebuffer = "125 Feet"
nonartbuffer = "125 Feet"
artbuffer = "125 Feet"

Engineering_SDE_Bridge = "C:\\IOT2\\IOT2_KickoffData.gdb\\IOT2_Bridges"
SDE_Bridges_Lay = "SDE.Bridges_Layer"
Engineering_SDE_StreetsNonArterial_IOTtwo = "C:\\IOT2\\IOT2_KickoffData.gdb\\IOT2_NonArt"
SDE_StreetsNonArterial_IOTtwo = "SDE.StreetsNonArterial_IOT2_"
Engineering_SDE_StreetsArterial_IOTtwo = "C:\\IOT2\\IOT2_KickoffData.gdb\\IOT2_Art"
SDE_StreetsArterial_IOT2_Layer = "SDE.StreetsArterial_IOT2_Lay"

env.workspace = r"C:\IOT2\Kickoff"
mxd = arcpy.mapping.MapDocument(mxdpath)
projName = mxd.dataDrivenPages.pageRow.CityProject
ddp = mxd.dataDrivenPages
indexLayer = ddp.indexLayer


if arcpy.Exists(rootpath + topfolder + filegdb):
	print "Connection to " + rootpath + topfolder + filegdb + ".gdb already exists"
else:
	# Process: Create Database Connection
	# Process: Create File GDB
	arcpy.CreateFileGDB_management(rootpath + topfolder + secondfolder, filegdb, "CURRENT")
	print "Created connection to " + rootpath + topfolder + secondfolder + filegdb
		
# Test array Bridges
#trafCol_Array = ['2037B0269Z', '2037B0271Z']

# Production array Bridges
trafCol_Array = ['2037B0167Z', '2037B0173Z', '2037B0183Z', '2037B0204Z', '2037B0225Z', '2037B0232Z', '2037B0241Z', '2037B0258Z', '2037B0261A', '2037B0263Z', '2037B0269Z', '2037B0271Z', '2037B0286Z', '2037B0301Z', '2037B0315Z', '2037B0322Z', '2037B0336Z', '2037B0343Z', '2037B0404Z', '2037B0425Z']

for trafCol_Num in trafCol_Array:
	mxd = arcpy.mapping.MapDocument(mxdpath)
	ddp = mxd.dataDrivenPages
	indexLayer = ddp.indexLayer
	print  rootpath + topfolder + secondfolder + "\\" + trafCol_Num 

	if arcpy.Exists(rootpath + topfolder):
		print "The local path " + rootpath + topfolder + " already exists"
	else:
		arcpy.CreateFolder_management(rootpath, topfolder)
		print "Created local path " + rootpath + topfolder 
		
	if arcpy.Exists(rootpath + topfolder + secondfolder):
		print "The local path " + rootpath + topfolder + secondfolder + " already exists"
	else:
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder)
		print "Created local path " + rootpath + topfolder + secondfolder
		
	
	if arcpy.Exists(rootpath + topfolder + secondfolder + "\\" + trafCol_Num):
		print "The local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + " already exists"
	else:
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder + "\\" + trafCol_Num)
		print "Created local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num 
		
	if arcpy.Exists(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric):
		print "The local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + " already exists"
	else:
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric)
		print "Created local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric
		
	if arcpy.Exists(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder):
		print "The local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder + " already exists"
	else:
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder)
		print "Created local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder
	
	# Local variables:
	ADA_UnsigRamps = sourcegdb + "\\ADA_UnsigRamps"
	ADA_UnsigRamps_2036A0064Z = "ADA_UnsigRamps_" + trafCol_Num
	ADA_UnsigRamps_2036A0064Z__2_ = ADA_UnsigRamps_2036A0064Z
	IOT2_Art = Engineering_SDE_Bridge
	IOT2_Art_2036A0064Z = "IOT2_Bridge_" + trafCol_Num
	ADA_UnsigInt = sourcegdb + "\\ADA_UnsigInt"
	ADA_UnsigInt_2036A0064Z = "ADA_UnsigInt_" + trafCol_Num
	ADA_UnsigCorner = sourcegdb + "\\ADA_UnsigCorner"
	ADA_UnsigCorner_2036A0064Z = "ADA_UnsigCorner_" + trafCol_Num
	ADA_TransitStops = sourcegdb + "\\ADA_TransitStops"
	ADA_TransitStops_2036A0064Z = "ADA_TransitStops_" + trafCol_Num
	ADA_SigRamps = sourcegdb + "\\ADA_SigRamps"
	ADA_SigRamps_2036A0064Z = "ADA_SigRamps_" + trafCol_Num
	ADA_SigInt = sourcegdb + "\\ADA_SigInt"
	ADA_SigInt_2036A0064Z = "ADA_SigInt_" + trafCol_Num
	ADA_SigCorner = sourcegdb + "\\ADA_SigCorner"
	ADA_SigCorner_2036A0064Z = "ADA_SigCorner_" + trafCol_Num
	ADA_Sidewalks = sourcegdb + "\\ADA_Sidewalks"
	ADA_Sidewalks_2036A0064Z = "ADA_Sidewalks_" + trafCol_Num
	ADA_Driveway = sourcegdb + "\\ADA_Driveway"
	ADA_Driveway_2036A0064Z = "ADA_Driveway_" + trafCol_Num
	Shapefiles = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder
	Shapefiles__3_ = Shapefiles
	ADA_Driveway_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_Driveway_" + trafCol_Num + ".xls"
	ADA_Sidewalks_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_Sidewalks_" + trafCol_Num + ".xls"
	ADA_SigCorner_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_SigCorner_" + trafCol_Num + ".xls"
	ADA_SigInt_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_SigInt_" + trafCol_Num + ".xls"
	ADA_SigRamps_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_SigRamps_" + trafCol_Num + ".xls"
	ADA_TransitStops_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_TransitStops_" + trafCol_Num + ".xls"
	ADA_UnsigCorner_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_UnsigCorner_" + trafCol_Num + ".xls"
	ADA_UnsigInt_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_UnsigInt_" + trafCol_Num + ".xls"
	ADA_UnsigRamps_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_UnsigRamps_" + trafCol_Num + ".xls"
	ADA_Sidewalks_2036A0064Z__2_ = ADA_Sidewalks_2036A0064Z
	ADA_UnsigInt_2036A0064Z__2_ = ADA_UnsigInt_2036A0064Z
	ADA_UnsigCorner_2036A0064Z__2_ = ADA_UnsigCorner_2036A0064Z
	ADA_TransitStops_2036A0064Z__2_ = ADA_TransitStops_2036A0064Z
	ADA_SigRamps_2036A0064Z__2_ = ADA_SigRamps_2036A0064Z
	ADA_SigInt_2036A0064Z__2_ = ADA_SigInt_2036A0064Z
	ADA_SigCorner_2036A0064Z__2_ = ADA_SigCorner_2036A0064Z
	ADA_Driveway_2036A0064Z__2_ = ADA_Driveway_2036A0064Z

	# Process: Make Feature Layer (9)
	arcpy.MakeFeatureLayer_management(ADA_UnsigRamps, ADA_UnsigRamps_2036A0064Z, "", "", "")

	# Process: Make Feature Layer (10)
	arcpy.MakeFeatureLayer_management(IOT2_Art, IOT2_Art_2036A0064Z, "CityProjec = '" + trafCol_Num + "'", "", "")

	# Process: Select Layer By Location (2)
	arcpy.SelectLayerByLocation_management(ADA_UnsigRamps_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, bridgebuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer (8)
	arcpy.MakeFeatureLayer_management(ADA_UnsigInt, ADA_UnsigInt_2036A0064Z, "", "", "")

	# Process: Select Layer By Location (3)
	arcpy.SelectLayerByLocation_management(ADA_UnsigInt_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, bridgebuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer (7)
	arcpy.MakeFeatureLayer_management(ADA_UnsigCorner, ADA_UnsigCorner_2036A0064Z, "", "", "")

	# Process: Select Layer By Location (4)
	arcpy.SelectLayerByLocation_management(ADA_UnsigCorner_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, bridgebuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer (6)
	arcpy.MakeFeatureLayer_management(ADA_TransitStops, ADA_TransitStops_2036A0064Z, "", "", "")

	# Process: Select Layer By Location (5)
	arcpy.SelectLayerByLocation_management(ADA_TransitStops_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, bridgebuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer (5)
	arcpy.MakeFeatureLayer_management(ADA_SigRamps, ADA_SigRamps_2036A0064Z, "", "", "")

	# Process: Select Layer By Location (6)
	arcpy.SelectLayerByLocation_management(ADA_SigRamps_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, bridgebuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer (4)
	arcpy.MakeFeatureLayer_management(ADA_SigInt, ADA_SigInt_2036A0064Z, "", "", "")

	# Process: Select Layer By Location (7)
	arcpy.SelectLayerByLocation_management(ADA_SigInt_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, bridgebuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer (3)
	arcpy.MakeFeatureLayer_management(ADA_SigCorner, ADA_SigCorner_2036A0064Z, "", "", "")

	# Process: Select Layer By Location (8)
	arcpy.SelectLayerByLocation_management(ADA_SigCorner_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, bridgebuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer (2)
	arcpy.MakeFeatureLayer_management(ADA_Sidewalks, ADA_Sidewalks_2036A0064Z, "", "", "")

	# Process: Select Layer By Location
	arcpy.SelectLayerByLocation_management(ADA_Sidewalks_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, bridgebuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer
	arcpy.MakeFeatureLayer_management(ADA_Driveway, ADA_Driveway_2036A0064Z, "", "", "")

	# Process: Select Layer By Location (9)
	arcpy.SelectLayerByLocation_management(ADA_Driveway_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, bridgebuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Get Count (9)
	resultDriveway = arcpy.GetCount_management(ADA_Driveway_2036A0064Z__2_)
	count = int(resultDriveway.getOutput(0))
	print str(count) + " ADA driveways in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_Driveway_2036A0064Z__2_, ADA_Driveway_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_Driveway_2036A0064Z, Shapefiles)
		print "Exported driveways for " + trafCol_Num
	else:
		print "Did not export driveways for " + trafCol_Num

	# Process: Get Count (2)
	resultSidewalks = arcpy.GetCount_management(ADA_Sidewalks_2036A0064Z__2_)
	count = int(resultSidewalks.getOutput(0))
	print str(count) + " ADA sidewalks in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_Sidewalks_2036A0064Z__2_, ADA_Sidewalks_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_Sidewalks_2036A0064Z, Shapefiles)
		print "Exported sidewalks for " + trafCol_Num
	else:
		print "Did not export sidewalks for " + trafCol_Num

	# Process: Get Count (7)
	resultsSigCorner = arcpy.GetCount_management(ADA_SigCorner_2036A0064Z__2_)
	count = int(resultsSigCorner.getOutput(0))
	print str(count) + " ADA Signalized Corners in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_SigCorner_2036A0064Z__2_, ADA_SigCorner_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_SigCorner_2036A0064Z, Shapefiles)
		print "Exported Signalized Corners for " + trafCol_Num
	else:
		print "Did not export Signalized Corners for " + trafCol_Num

	# Process: Get Count (8)
	resultsSigInt = arcpy.GetCount_management(ADA_SigInt_2036A0064Z__2_)
	count = int(resultsSigInt.getOutput(0))
	print str(count) + " ADA Signalized Intersections in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_SigInt_2036A0064Z__2_, ADA_SigInt_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_SigInt_2036A0064Z, Shapefiles)
		print "Exported Signalized Intersections for " + trafCol_Num
	else:
		print "Did not export Signalized Intersections for " + trafCol_Num

	# Process: Get Count (6)
	resultsSigRamps = arcpy.GetCount_management(ADA_SigRamps_2036A0064Z__2_)
	count = int(resultsSigRamps.getOutput(0))
	print str(count) + " ADA Signalized Ramps in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_SigRamps_2036A0064Z__2_, ADA_SigRamps_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_SigRamps_2036A0064Z, Shapefiles)
		print "Exported Signalized Ramps for " + trafCol_Num
	else:
		print "Did not export Signalized Ramps for " + trafCol_Num

	# Process: Get Count (5)
	resultsTransitStops = arcpy.GetCount_management(ADA_TransitStops_2036A0064Z__2_)
	count = int(resultsTransitStops.getOutput(0))
	print str(count) + " ADA Transit Stops in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_TransitStops_2036A0064Z__2_, ADA_TransitStops_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_TransitStops_2036A0064Z, Shapefiles)
		print "Exported Transit Stops for " + trafCol_Num
	else:
		print "Did not export Transit Stops for " + trafCol_Num

	# Process: Get Count (4)
	resultsUnsigCorner = arcpy.GetCount_management(ADA_UnsigCorner_2036A0064Z__2_)
	count = int(resultsUnsigCorner.getOutput(0))
	print str(count) + " ADA Unsignalized Corners in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_UnsigCorner_2036A0064Z__2_, ADA_UnsigCorner_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_UnsigCorner_2036A0064Z, Shapefiles)
		print "Exported Unsignalized Corners for " + trafCol_Num
	else:
		print "Did not export Unsignalized Corners for " + trafCol_Num

	# Process: Get Count (3)
	resultsUnsigInt = arcpy.GetCount_management(ADA_UnsigInt_2036A0064Z__2_)
	count = int(resultsUnsigInt.getOutput(0))
	print str(count) + " ADA Unsignalized Intersections in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_UnsigInt_2036A0064Z__2_, ADA_UnsigInt_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_UnsigInt_2036A0064Z, Shapefiles)
		print "Exported Unsignalized Intersections for " + trafCol_Num
	else:
		print "Did not export Unsignalized Intersections for " + trafCol_Num

	# Process: Get Count
	resultsUnsigRamps = arcpy.GetCount_management(ADA_UnsigRamps_2036A0064Z__2_)
	count = int(resultsUnsigRamps.getOutput(0))
	print str(count) + " ADA Unsignalized Ramps in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_UnsigRamps_2036A0064Z__2_, ADA_UnsigRamps_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_UnsigRamps_2036A0064Z, Shapefiles)
		print "Exported Unsignalized Ramps for " + trafCol_Num
	else:
		print "Did not export Unsignalized Ramps for " + trafCol_Num
	
for trafCol_Num in trafCol_Array:
	mxd = arcpy.mapping.MapDocument(mxdpath)
	ddp = mxd.dataDrivenPages
	indexLayer = ddp.indexLayer
	
	arcpy.SelectLayerByAttribute_management(indexLayer, "NEW_SELECTION", "CityProject = '" + trafCol_Num + "'")
	
	print "Exporting " + metricmoniker + "_"  + trafCol_Num + ".pdf"
	ddp.exportToPDF(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + metricmoniker + "_"  + trafCol_Num + ".pdf", "SELECTED")
	print "Exported " + metricmoniker + "_"  + trafCol_Num + ".pdf"
	
	del mxd
	del ddp
	del indexLayer

# Test array Art
#trafCol_Array = ['2036A0064Z', '2036A0065Z']

# Production array Art
trafCol_Array = ['2036A0001Z', '2036A0002Z', '2036A0003Z', '2036A0004Z', '2036A0005Z', '2036A0007Z', '2036A0008Z', '2036A0009Z', '2036A0010Z', '2036A0012Z', '2036A0014Z', '2036A0015Z', '2036A0016Z', '2036A0017Z', '2036A0018Z', '2036A0019Z', '2036A0020Z', '2036A0021Z', '2036A0022Z', '2036A0023Z', '2036A0025Z', '2036A0026Z', '2036A0028Z', '2036A0029Z', '2036A0030Z', '2036A0031Z', '2036A0033Z', '2036A0034Z', '2036A0036Z', '2036A0037Z', '2036A0041Z', '2036A0042Z', '2036A0043Z', '2036A0044Z', '2036A0045Z', '2036A0046Z', '2036A0047Z', '2036A0049Z', '2036A0050Z', '2036A0051Z', '2036A0052Z', '2036A0053Z', '2036A0057Z', '2036A0058Z', '2036A0059Z', '2036A0060Z', '2036A0061Z', '2036A0062Z', '2036A0063Z', '2036A0064Z', '2036A0065Z', '2036A0066Z', '2036A0067Z', '2036A0068Z', '2036A0069Z', '2036A0070Z', '2036A0071Z', '2036A0072Z', '2036A0073Z', '2036A0074Z', '2036A0075Z', '2036A0077Z', '2036A0078Z', '2036A0079Z', '2036A0080Z', '2036A0081Z', '2036A0082Z', '2036A0083Z', '2036A0084Z', '2036A0085Z', '2036A0092Z', '2036A0094Z', '2036A0102Z', '2036A0108Z', '2036A0109Z', '2036A0110Z', '2036A0111Z', '2036A0112Z', '2036A0117Z', '2036A0119Z', '2036A0122Z', '2036A0123Z', '2036A0124Z', '2036A0125Z', '2036A0126Z', '2036D0001Z', '2036W0001Z', '2036W0002Z', '2036W0004Z', '2036W0005Z', '2036W0006Z']

for trafCol_Num in trafCol_Array:
	mxd = arcpy.mapping.MapDocument(mxdpath)
	ddp = mxd.dataDrivenPages
	indexLayer = ddp.indexLayer
	print  rootpath + topfolder + secondfolder + "\\" + trafCol_Num 

	if arcpy.Exists(rootpath + topfolder):
		print "The local path " + rootpath + topfolder + " already exists"
	else:
		arcpy.CreateFolder_management(rootpath, topfolder)
		print "Created local path " + rootpath + topfolder 
		
	if arcpy.Exists(rootpath + topfolder + secondfolder):
		print "The local path " + rootpath + topfolder + secondfolder + " already exists"
	else:
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder)
		print "Created local path " + rootpath + topfolder + secondfolder
		
	
	if arcpy.Exists(rootpath + topfolder + secondfolder + "\\" + trafCol_Num):
		print "The local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + " already exists"
	else:
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder + "\\" + trafCol_Num)
		print "Created local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num 
		
	if arcpy.Exists(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric):
		print "The local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + " already exists"
	else:
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric)
		print "Created local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric
		
	if arcpy.Exists(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder):
		print "The local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder + " already exists"
	else:
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder)
		print "Created local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder

	# Local variables:
	ADA_UnsigRamps = sourcegdb + "\\ADA_UnsigRamps"
	ADA_UnsigRamps_2036A0064Z = "ADA_UnsigRamps_" + trafCol_Num
	ADA_UnsigRamps_2036A0064Z__2_ = ADA_UnsigRamps_2036A0064Z
	IOT2_Art = Engineering_SDE_StreetsArterial_IOTtwo
	IOT2_Art_2036A0064Z = "IOT2_Art_" + trafCol_Num
	ADA_UnsigInt = sourcegdb + "\\ADA_UnsigInt"
	ADA_UnsigInt_2036A0064Z = "ADA_UnsigInt_" + trafCol_Num
	ADA_UnsigCorner = sourcegdb + "\\ADA_UnsigCorner"
	ADA_UnsigCorner_2036A0064Z = "ADA_UnsigCorner_" + trafCol_Num
	ADA_TransitStops = sourcegdb + "\\ADA_TransitStops"
	ADA_TransitStops_2036A0064Z = "ADA_TransitStops_" + trafCol_Num
	ADA_SigRamps = sourcegdb + "\\ADA_SigRamps"
	ADA_SigRamps_2036A0064Z = "ADA_SigRamps_" + trafCol_Num
	ADA_SigInt = sourcegdb + "\\ADA_SigInt"
	ADA_SigInt_2036A0064Z = "ADA_SigInt_" + trafCol_Num
	ADA_SigCorner = sourcegdb + "\\ADA_SigCorner"
	ADA_SigCorner_2036A0064Z = "ADA_SigCorner_" + trafCol_Num
	ADA_Sidewalks = sourcegdb + "\\ADA_Sidewalks"
	ADA_Sidewalks_2036A0064Z = "ADA_Sidewalks_" + trafCol_Num
	ADA_Driveway = sourcegdb + "\\ADA_Driveway"
	ADA_Driveway_2036A0064Z = "ADA_Driveway_" + trafCol_Num
	Shapefiles = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder
	Shapefiles__3_ = Shapefiles
	ADA_Driveway_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_Driveway_" + trafCol_Num + ".xls"
	ADA_Sidewalks_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_Sidewalks_" + trafCol_Num + ".xls"
	ADA_SigCorner_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_SigCorner_" + trafCol_Num + ".xls"
	ADA_SigInt_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_SigInt_" + trafCol_Num + ".xls"
	ADA_SigRamps_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_SigRamps_" + trafCol_Num + ".xls"
	ADA_TransitStops_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_TransitStops_" + trafCol_Num + ".xls"
	ADA_UnsigCorner_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_UnsigCorner_" + trafCol_Num + ".xls"
	ADA_UnsigInt_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_UnsigInt_" + trafCol_Num + ".xls"
	ADA_UnsigRamps_2036A0064Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\ADA_UnsigRamps_" + trafCol_Num + ".xls"
	ADA_Sidewalks_2036A0064Z__2_ = ADA_Sidewalks_2036A0064Z
	ADA_UnsigInt_2036A0064Z__2_ = ADA_UnsigInt_2036A0064Z
	ADA_UnsigCorner_2036A0064Z__2_ = ADA_UnsigCorner_2036A0064Z
	ADA_TransitStops_2036A0064Z__2_ = ADA_TransitStops_2036A0064Z
	ADA_SigRamps_2036A0064Z__2_ = ADA_SigRamps_2036A0064Z
	ADA_SigInt_2036A0064Z__2_ = ADA_SigInt_2036A0064Z
	ADA_SigCorner_2036A0064Z__2_ = ADA_SigCorner_2036A0064Z
	ADA_Driveway_2036A0064Z__2_ = ADA_Driveway_2036A0064Z

	# Process: Make Feature Layer (9)
	arcpy.MakeFeatureLayer_management(ADA_UnsigRamps, ADA_UnsigRamps_2036A0064Z, "", "", "")

	# Process: Make Feature Layer (10)
	arcpy.MakeFeatureLayer_management(IOT2_Art, IOT2_Art_2036A0064Z, "CityProjec = '" + trafCol_Num + "'", "", "")

	# Process: Select Layer By Location (2)
	arcpy.SelectLayerByLocation_management(ADA_UnsigRamps_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, artbuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer (8)
	arcpy.MakeFeatureLayer_management(ADA_UnsigInt, ADA_UnsigInt_2036A0064Z, "", "", "")

	# Process: Select Layer By Location (3)
	arcpy.SelectLayerByLocation_management(ADA_UnsigInt_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, artbuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer (7)
	arcpy.MakeFeatureLayer_management(ADA_UnsigCorner, ADA_UnsigCorner_2036A0064Z, "", "", "")

	# Process: Select Layer By Location (4)
	arcpy.SelectLayerByLocation_management(ADA_UnsigCorner_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, artbuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer (6)
	arcpy.MakeFeatureLayer_management(ADA_TransitStops, ADA_TransitStops_2036A0064Z, "", "", "")

	# Process: Select Layer By Location (5)
	arcpy.SelectLayerByLocation_management(ADA_TransitStops_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, artbuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer (5)
	arcpy.MakeFeatureLayer_management(ADA_SigRamps, ADA_SigRamps_2036A0064Z, "", "", "")

	# Process: Select Layer By Location (6)
	arcpy.SelectLayerByLocation_management(ADA_SigRamps_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, artbuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer (4)
	arcpy.MakeFeatureLayer_management(ADA_SigInt, ADA_SigInt_2036A0064Z, "", "", "")

	# Process: Select Layer By Location (7)
	arcpy.SelectLayerByLocation_management(ADA_SigInt_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, artbuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer (3)
	arcpy.MakeFeatureLayer_management(ADA_SigCorner, ADA_SigCorner_2036A0064Z, "", "", "")

	# Process: Select Layer By Location (8)
	arcpy.SelectLayerByLocation_management(ADA_SigCorner_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, artbuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer (2)
	arcpy.MakeFeatureLayer_management(ADA_Sidewalks, ADA_Sidewalks_2036A0064Z, "", "", "")

	# Process: Select Layer By Location
	arcpy.SelectLayerByLocation_management(ADA_Sidewalks_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, artbuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Make Feature Layer
	arcpy.MakeFeatureLayer_management(ADA_Driveway, ADA_Driveway_2036A0064Z, "", "", "")

	# Process: Select Layer By Location (9)
	arcpy.SelectLayerByLocation_management(ADA_Driveway_2036A0064Z, "INTERSECT", IOT2_Art_2036A0064Z, artbuffer, "NEW_SELECTION", "NOT_INVERT")

	# Process: Get Count (9)
	resultDriveway = arcpy.GetCount_management(ADA_Driveway_2036A0064Z__2_)
	count = int(resultDriveway.getOutput(0))
	print str(count) + " ADA driveways in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_Driveway_2036A0064Z__2_, ADA_Driveway_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_Driveway_2036A0064Z, Shapefiles)
		print "Exported driveways for " + trafCol_Num
	else:
		print "Did not export driveways for " + trafCol_Num

	# Process: Get Count (2)
	resultSidewalks = arcpy.GetCount_management(ADA_Sidewalks_2036A0064Z__2_)
	count = int(resultSidewalks.getOutput(0))
	print str(count) + " ADA sidewalks in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_Sidewalks_2036A0064Z__2_, ADA_Sidewalks_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_Sidewalks_2036A0064Z, Shapefiles)
		print "Exported sidewalks for " + trafCol_Num
	else:
		print "Did not export sidewalks for " + trafCol_Num

	# Process: Get Count (7)
	resultsSigCorner = arcpy.GetCount_management(ADA_SigCorner_2036A0064Z__2_)
	count = int(resultsSigCorner.getOutput(0))
	print str(count) + " ADA Signalized Corners in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_SigCorner_2036A0064Z__2_, ADA_SigCorner_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_SigCorner_2036A0064Z, Shapefiles)
		print "Exported Signalized Corners for " + trafCol_Num
	else:
		print "Did not export Signalized Corners for " + trafCol_Num

	# Process: Get Count (8)
	resultsSigInt = arcpy.GetCount_management(ADA_SigInt_2036A0064Z__2_)
	count = int(resultsSigInt.getOutput(0))
	print str(count) + " ADA Signalized Intersections in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_SigInt_2036A0064Z__2_, ADA_SigInt_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_SigInt_2036A0064Z, Shapefiles)
		print "Exported Signalized Intersections for " + trafCol_Num
	else:
		print "Did not export Signalized Intersections for " + trafCol_Num

	# Process: Get Count (6)
	resultsSigRamps = arcpy.GetCount_management(ADA_SigRamps_2036A0064Z__2_)
	count = int(resultsSigRamps.getOutput(0))
	print str(count) + " ADA Signalized Ramps in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_SigRamps_2036A0064Z__2_, ADA_SigRamps_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_SigRamps_2036A0064Z, Shapefiles)
		print "Exported Signalized Ramps for " + trafCol_Num
	else:
		print "Did not export Signalized Ramps for " + trafCol_Num

	# Process: Get Count (5)
	resultsTransitStops = arcpy.GetCount_management(ADA_TransitStops_2036A0064Z__2_)
	count = int(resultsTransitStops.getOutput(0))
	print str(count) + " ADA Transit Stops in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_TransitStops_2036A0064Z__2_, ADA_TransitStops_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_TransitStops_2036A0064Z, Shapefiles)
		print "Exported Transit Stops for " + trafCol_Num
	else:
		print "Did not export Transit Stops for " + trafCol_Num

	# Process: Get Count (4)
	resultsUnsigCorner = arcpy.GetCount_management(ADA_UnsigCorner_2036A0064Z__2_)
	count = int(resultsUnsigCorner.getOutput(0))
	print str(count) + " ADA Unsignalized Corners in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_UnsigCorner_2036A0064Z__2_, ADA_UnsigCorner_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_UnsigCorner_2036A0064Z, Shapefiles)
		print "Exported Unsignalized Corners for " + trafCol_Num
	else:
		print "Did not export Unsignalized Corners for " + trafCol_Num

	# Process: Get Count (3)
	resultsUnsigInt = arcpy.GetCount_management(ADA_UnsigInt_2036A0064Z__2_)
	count = int(resultsUnsigInt.getOutput(0))
	print str(count) + " ADA Unsignalized Intersections in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_UnsigInt_2036A0064Z__2_, ADA_UnsigInt_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_UnsigInt_2036A0064Z, Shapefiles)
		print "Exported Unsignalized Intersections for " + trafCol_Num
	else:
		print "Did not export Unsignalized Intersections for " + trafCol_Num

	# Process: Get Count
	resultsUnsigRamps = arcpy.GetCount_management(ADA_UnsigRamps_2036A0064Z__2_)
	count = int(resultsUnsigRamps.getOutput(0))
	print str(count) + " ADA Unsignalized Ramps in " + trafCol_Num

	if count > 0:
		# Process: Table To Excel
		arcpy.TableToExcel_conversion(ADA_UnsigRamps_2036A0064Z__2_, ADA_UnsigRamps_2036A0064Z_xls, "NAME", "CODE")
		arcpy.FeatureClassToShapefile_conversion(ADA_UnsigRamps_2036A0064Z, Shapefiles)
		print "Exported Unsignalized Ramps for " + trafCol_Num
	else:
		print "Did not export Unsignalized Ramps for " + trafCol_Num
		
for trafCol_Num in trafCol_Array:
	mxd = arcpy.mapping.MapDocument(mxdpath)
	ddp = mxd.dataDrivenPages
	indexLayer = ddp.indexLayer
	
	arcpy.SelectLayerByAttribute_management(indexLayer, "NEW_SELECTION", "CityProject = '" + trafCol_Num + "'")
	
	print "Exporting " + metricmoniker + "_"  + trafCol_Num + ".pdf"
	ddp.exportToPDF(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + metricmoniker + "_"  + trafCol_Num + ".pdf", "SELECTED")
	print "Exported " + metricmoniker + "_"  + trafCol_Num + ".pdf"
	
	del mxd
	del ddp
	del indexLayer

print "Done."