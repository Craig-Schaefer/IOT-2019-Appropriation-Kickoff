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


metric = "SSOs"
metricmoniker = "SSO"
metricpath = "C:\\IOT2\\IOT2_KickoffData.gdb\\SSOs_125"
secondmetric = "SanitarySewer"
secondmetricmoniker = "ssGravityMain"
secondmetricpath = "C:\\IOT2\\IOT2_KickoffData.gdb\\ssGMainIOT2_50"
mxdpath = r"C:\IOT2\Kickoff\Appr_SSO.mxd"

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
Collisions_TPD__3_ = metricpath
Collisions_TPD__2_ = metricpath
Collisions_TPD__7_ = secondmetricpath
Collisions_TPD__6_ = secondmetricpath
Collisions_TPD = metricpath


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
trafCol_Array = ['2037B0153Z', '2037B0167Z', '2037B0173Z', '2037B0179Z', '2037B0183Z', '2037B0201C', '2037B0204Z', '2037B0216Z', '2037B0219D', '2037B0225Z', '2037B0232A', '2037B0232Z', '2037B0236Z', '2037B0241Z', '2037B0245Z', '2037B0252Z', '2037B0258Z', '2037B0261A', '2037B0263Z', '2037B0269Z', '2037B0271Z', '2037B0286Z', '2037B0301A', '2037B0301Z', '2037B0315Z', '2037B0322Z', '2037B0329Z', '2037B0336Z', '2037B0340Z', '2037B0343Z', '2037B0346Z', '2037B0359Z', '2037B0404Z', '2037B0423Z', '2037B0424Z', '2037B0425Z', '2037B0474Z', '2037B0478Z', '2037B0482Z']

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
		
	if arcpy.Exists(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric):
		print "The local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + " already exists"
	else:
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric)
		print "Created local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric
		
	if arcpy.Exists(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder):
		print "The local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder + " already exists"
	else:
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder)
		print "Created local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder
	
	SDE_Bridges_Layer = SDE_Bridges_Lay
	Engineering_SDE_Bridges = Engineering_SDE_Bridge
	TrfCol_2036A0001Z = metricmoniker + "_" + trafCol_Num
	TrfCol_2036A0001Z__6_ = TrfCol_2036A0001Z
	TrfCol_2036A0001Z2 = secondmetricmoniker + "_" + trafCol_Num
	TrfCol_2036A0001Z2__6_ = TrfCol_2036A0001Z2
	TrfCol_2036A0001Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + metricmoniker + "_" + trafCol_Num + ".xls"
	TrfCol_2036A0001Z2_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + secondmetricmoniker + "_" + trafCol_Num + ".xls"
	TrfCol_2036A0001Z__2_ = metricmoniker + "_" + trafCol_Num
	TrfCol_2036A0001Z__5_ = TrfCol_2036A0001Z__2_
	TrfCol_2036A0001Z_xls__2_ = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + metricmoniker + "_" + trafCol_Num + ".xls"
	TrfCol_2036A0001Z__3_ = metricmoniker + "_" + trafCol_Num
	TrfCol_2036A0001Z__4_ = TrfCol_2036A0001Z__3_
	TrfCol_2036A0001Z_xls__3_ = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + metricmoniker + "_" + trafCol_Num + ".xls"
	Shapefiles = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder
	Shapefiles2 = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder
	Shapefiles__2_ = Shapefiles
	Shapefiles__3_ = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder
	Shapefiles__4_ = Shapefiles__3_
	Shapefiles__5_ = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder
	Shapefiles__6_ = Shapefiles__5_

	try:
		# Process: Make Feature Layer (5)
		arcpy.MakeFeatureLayer_management(Collisions_TPD__3_, TrfCol_2036A0001Z, "", "", "")

		# Process: Make Feature Layer (3)
		arcpy.MakeFeatureLayer_management(Engineering_SDE_Bridges, SDE_Bridges_Layer, "CityProjec = '" + trafCol_Num + "'", "", "OBJECTID OBJECTID VISIBLE NONE;TypeofFund TypeofFund VISIBLE NONE;MasterInde MasterInde VISIBLE NONE;OrdinanceR OrdinanceR VISIBLE NONE;Year Year VISIBLE NONE;ZoneID ZoneID VISIBLE NONE;CategoryDe CategoryDe VISIBLE NONE;LocationDe LocationDe VISIBLE NONE;BudgetedCo BudgetedCo VISIBLE NONE;CurrentSta CurrentSta VISIBLE NONE;DesignStar DesignStar VISIBLE NONE;Engineer Engineer VISIBLE NONE;Contractor Contractor VISIBLE NONE;PhoneConta PhoneConta VISIBLE NONE;EmailConta EmailConta VISIBLE NONE;TargetComp TargetComp VISIBLE NONE;Completed Completed VISIBLE NONE;Comments Comments VISIBLE NONE;CityProjec CityProjec VISIBLE NONE;MapReferen MapReferen VISIBLE NONE;DistrictID DistrictID VISIBLE NONE;GMRotation GMRotation VISIBLE NONE;ConstStartDate ConstStartDate VISIBLE NONE;LASTUPDATE LASTUPDATE VISIBLE NONE;LASTEDITOR LASTEDITOR VISIBLE NONE;SHAPE SHAPE VISIBLE NONE")
		print "Found " + trafCol_Num + " in Bridges."
		
		# Process: Select Layer By Location
		arcpy.SelectLayerByLocation_management(TrfCol_2036A0001Z, "INTERSECT", SDE_Bridges_Layer, bridgebuffer, "NEW_SELECTION", "NOT_INVERT")
		
		resultSSOs = arcpy.GetCount_management(TrfCol_2036A0001Z)
		count = int(resultSSOs.getOutput(0))
		print str(count) + " SSOs in " + trafCol_Num
		
		if count > 0:
		
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
			
			arcpy.TableToExcel_conversion(TrfCol_2036A0001Z__6_, TrfCol_2036A0001Z_xls, "NAME", "CODE")
			print "Made Excel file for " + trafCol_Num
			# Process: Feature Class To Shapefile (multiple)
			arcpy.FeatureClassToShapefile_conversion(TrfCol_2036A0001Z__6_, Shapefiles)
			print "Made shapefile for " + trafCol_Num
		else:
			print "No SSOs located nearby"
	except:
		print "Couldn't find " + trafCol_Num + " in Bridges."
		
	del Engineering_SDE_Bridges
	del SDE_Bridges_Layer
	
	SDE_Bridges_Layer = SDE_Bridges_Lay
	Engineering_SDE_Bridges = Engineering_SDE_Bridge
	
	try:
		# Process: Make Feature Layer (5)
		arcpy.MakeFeatureLayer_management(Collisions_TPD__7_, TrfCol_2036A0001Z2, "", "", "")

		# Process: Make Feature Layer (3)
		arcpy.MakeFeatureLayer_management(Engineering_SDE_Bridges, SDE_Bridges_Layer, "CityProjec = '" + trafCol_Num + "'", "", "OBJECTID OBJECTID VISIBLE NONE;TypeofFund TypeofFund VISIBLE NONE;MasterInde MasterInde VISIBLE NONE;OrdinanceR OrdinanceR VISIBLE NONE;Year Year VISIBLE NONE;ZoneID ZoneID VISIBLE NONE;CategoryDe CategoryDe VISIBLE NONE;LocationDe LocationDe VISIBLE NONE;BudgetedCo BudgetedCo VISIBLE NONE;CurrentSta CurrentSta VISIBLE NONE;DesignStar DesignStar VISIBLE NONE;Engineer Engineer VISIBLE NONE;Contractor Contractor VISIBLE NONE;PhoneConta PhoneConta VISIBLE NONE;EmailConta EmailConta VISIBLE NONE;TargetComp TargetComp VISIBLE NONE;Completed Completed VISIBLE NONE;Comments Comments VISIBLE NONE;CityProjec CityProjec VISIBLE NONE;MapReferen MapReferen VISIBLE NONE;DistrictID DistrictID VISIBLE NONE;GMRotation GMRotation VISIBLE NONE;ConstStartDate ConstStartDate VISIBLE NONE;LASTUPDATE LASTUPDATE VISIBLE NONE;LASTEDITOR LASTEDITOR VISIBLE NONE;SHAPE SHAPE VISIBLE NONE")
		print "Found " + trafCol_Num + " in Bridges."
		
		# Process: Select Layer By Location
		arcpy.SelectLayerByLocation_management(TrfCol_2036A0001Z2, "INTERSECT", SDE_Bridges_Layer, bridgebuffer, "NEW_SELECTION", "NOT_INVERT")

		# Process: Table To Excel
		arcpy.TableToExcel_conversion(TrfCol_2036A0001Z2__6_, TrfCol_2036A0001Z2_xls, "NAME", "CODE")
		print "Made " + secondmetricmoniker + " Excel file for " + trafCol_Num

		# Process: Feature Class To Shapefile (multiple)
		arcpy.FeatureClassToShapefile_conversion(TrfCol_2036A0001Z2__6_, Shapefiles2)
		print "Made shapefile for " + trafCol_Num
	except:
		print "Couldn't find " + trafCol_Num + " in Bridges."
	del Engineering_SDE_Bridges
	del SDE_Bridges_Layer
	
	
for trafCol_Num in trafCol_Array:
	mxd = arcpy.mapping.MapDocument(mxdpath)
	ddp = mxd.dataDrivenPages
	indexLayer = ddp.indexLayer
	
	arcpy.SelectLayerByAttribute_management(indexLayer, "NEW_SELECTION", "CityProject = '" + trafCol_Num + "'")
	
	print "Exporting " + secondmetricmoniker + "_"  + trafCol_Num + ".pdf"
	ddp.exportToPDF(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + secondmetricmoniker + "_"  + trafCol_Num + ".pdf", "SELECTED")
	print "Exported " + secondmetricmoniker + "_"  + trafCol_Num + ".pdf"
	
	del mxd
	del ddp
	del indexLayer
	

# Test array Art
#trafCol_Array = ['2036A0041Z', '2036A0042Z']

# Production array Art
trafCol_Array = ['2036A0001Z', '2036A0002Z', '2036A0003Z', '2036A0004Z', '2036A0005Z', '2036A0006Z', '2036A0007Z', '2036A0008Z', '2036A0009Z', '2036A0010Z', '2036A0011Z', '2036A0012Z', '2036A0013Z', '2036A0014Z', '2036A0015Z', '2036A0016Z', '2036A0017Z', '2036A0018Z', '2036A0019Z', '2036A0020Z', '2036A0021Z', '2036A0022Z', '2036A0023Z', '2036A0024Z', '2036A0025Z', '2036A0026Z', '2036A0028Z', '2036A0029Z', '2036A0030Z', '2036A0031Z', '2036A0033Z', '2036A0034Z', '2036A0035Z', '2036A0036Z', '2036A0037Z', '2036A0039Z', '2036A0040Z', '2036A0041Z', '2036A0042Z', '2036A0043Z', '2036A0044Z', '2036A0045Z', '2036A0046Z', '2036A0047Z', '2036A0049Z', '2036A0050Z', '2036A0051Z', '2036A0052Z', '2036A0053Z', '2036A0054Z', '2036A0055Z', '2036A0056Z', '2036A0057Z', '2036A0058Z', '2036A0059Z', '2036A0060Z', '2036A0061Z', '2036A0062Z', '2036A0063Z', '2036A0064Z', '2036A0065Z', '2036A0066Z', '2036A0067Z', '2036A0068Z', '2036A0069Z', '2036A0070Z', '2036A0071Z', '2036A0072Z', '2036A0073Z', '2036A0074Z', '2036A0075Z', '2036A0077Z', '2036A0078Z', '2036A0079Z', '2036A0080Z', '2036A0081Z', '2036A0082Z', '2036A0083Z', '2036A0084Z', '2036A0085Z', '2036A0086Z', '2036A0087Z', '2036A0088Z', '2036A0089Z', '2036A0090Z', '2036A0091Z', '2036A0092Z', '2036A0093Z', '2036A0094Z', '2036A0095Z', '2036A0096Z', '2036A0097Z', '2036A0098Z', '2036A0099Z', '2036A0100Z', '2036A0101Z', '2036A0102Z', '2036A0103Z', '2036A0104Z', '2036A0105Z', '2036A0106Z', '2036A0107Z', '2036A0108Z', '2036A0109Z', '2036A0110Z', '2036A0111Z', '2036A0112Z', '2036A0113Z', '2036A0114Z', '2036A0115Z', '2036A0116Z', '2036A0117Z', '2036A0118Z', '2036A0119Z', '2036A0120Z', '2036A0121Z', '2036A0122Z', '2036A0123Z', '2036A0124Z', '2036A0125Z', '2036A0126Z', '2036D0001Z', '2036W0001Z', '2036W0002Z', '2036W0003Z', '2036W0004Z', '2036W0005Z', '2036W0006Z']

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
		
	if arcpy.Exists(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric):
		print "The local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + " already exists"
	else:
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric)
		print "Created local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric
		
	if arcpy.Exists(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder):
		print "The local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder + " already exists"
	else:
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder)
		print "Created local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder
	
	Engineering_SDE_StreetsArterial_IOT2 = Engineering_SDE_StreetsArterial_IOTtwo
	SDE_StreetsArterial_IOT2_Lay = SDE_StreetsArterial_IOT2_Layer
	TrfCol_2036A0001Z = metricmoniker + "_" + trafCol_Num
	TrfCol_2036A0001Z__6_ = TrfCol_2036A0001Z
	TrfCol_2036A0001Z2 = secondmetricmoniker + "_" + trafCol_Num
	TrfCol_2036A0001Z2__6_ = TrfCol_2036A0001Z2
	TrfCol_2036A0001Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + metricmoniker + "_" + trafCol_Num + ".xls"
	TrfCol_2036A0001Z2_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + secondmetricmoniker + "_" + trafCol_Num + ".xls"
	TrfCol_2036A0001Z__2_ = metricmoniker + "_" + trafCol_Num
	TrfCol_2036A0001Z__5_ = TrfCol_2036A0001Z__2_
	TrfCol_2036A0001Z_xls__2_ = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + metricmoniker + "_" + trafCol_Num + ".xls"
	TrfCol_2036A0001Z__3_ = metricmoniker + "_" + trafCol_Num
	TrfCol_2036A0001Z__4_ = TrfCol_2036A0001Z__3_
	TrfCol_2036A0001Z_xls__3_ = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + metricmoniker + "_" + trafCol_Num + ".xls"
	Shapefiles = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder
	Shapefiles2 = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder
	Shapefiles__2_ = Shapefiles
	Shapefiles__3_ = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder
	Shapefiles__4_ = Shapefiles__3_
	Shapefiles__5_ = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder
	Shapefiles__6_ = Shapefiles__5_

	try:
		# Process: Make Feature Layer (6)
		arcpy.MakeFeatureLayer_management(Collisions_TPD, TrfCol_2036A0001Z__3_, "", "", "")

		# Process: Make Feature Layer
		arcpy.MakeFeatureLayer_management(Engineering_SDE_StreetsArterial_IOT2, SDE_StreetsArterial_IOT2_Lay, "CityProjec = '" + trafCol_Num + "'", "", "OBJECTID OBJECTID VISIBLE NONE;TypeofFund TypeofFund VISIBLE NONE;MasterInde MasterInde VISIBLE NONE;OrdinanceR OrdinanceR VISIBLE NONE;Year Year VISIBLE NONE;ZoneID ZoneID VISIBLE NONE;CategoryDe CategoryDe VISIBLE NONE;LocationDe LocationDe VISIBLE NONE;BudgetedCo BudgetedCo VISIBLE NONE;CurrentSta CurrentSta VISIBLE NONE;DesignStar DesignStar VISIBLE NONE;Engineer Engineer VISIBLE NONE;Contractor Contractor VISIBLE NONE;PhoneConta PhoneConta VISIBLE NONE;TargetComp TargetComp VISIBLE NONE;Completed Completed VISIBLE NONE;Comments Comments VISIBLE NONE;CityProjec CityProjec VISIBLE NONE;MapReferen MapReferen VISIBLE NONE;DistrictID DistrictID VISIBLE NONE;ConstStartDate ConstStartDate VISIBLE NONE;EmailConta EmailConta VISIBLE NONE;LASTUPDATE LASTUPDATE VISIBLE NONE;LASTEDITOR LASTEDITOR VISIBLE NONE;SHAPE SHAPE VISIBLE NONE;SHAPE.STLength() SHAPE.STLength() VISIBLE NONE")
		print "Found " + trafCol_Num + " in Arterials."

		# Process: Select Layer By Location (3)
		arcpy.SelectLayerByLocation_management(TrfCol_2036A0001Z__3_, "INTERSECT", SDE_StreetsArterial_IOT2_Lay, artbuffer, "NEW_SELECTION", "NOT_INVERT")
		
		resultSSOs = arcpy.GetCount_management(TrfCol_2036A0001Z__3_)
		count = int(resultSSOs.getOutput(0))
		print str(count) + " SSOs in " + trafCol_Num
		
		if count > 0:
		
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
			
			arcpy.TableToExcel_conversion(TrfCol_2036A0001Z__6_, TrfCol_2036A0001Z_xls, "NAME", "CODE")
			print "Made Excel file for " + trafCol_Num
			# Process: Feature Class To Shapefile (multiple)
			arcpy.FeatureClassToShapefile_conversion(TrfCol_2036A0001Z__6_, Shapefiles)
			print "Made shapefile for " + trafCol_Num
		else:
			print "No SSOs located nearby"
	except:
		print "Couldn't find " + trafCol_Num + " in Arterials."
	del Engineering_SDE_StreetsArterial_IOT2
	del SDE_StreetsArterial_IOT2_Lay
	
	Engineering_SDE_StreetsArterial_IOT2 = Engineering_SDE_StreetsArterial_IOTtwo
	SDE_StreetsArterial_IOT2_Lay = SDE_StreetsArterial_IOT2_Layer
	
	try:
		# Process: Make Feature Layer (5)
		arcpy.MakeFeatureLayer_management(Collisions_TPD__7_, TrfCol_2036A0001Z2, "", "", "")

		# Process: Make Feature Layer
		arcpy.MakeFeatureLayer_management(Engineering_SDE_StreetsArterial_IOT2, SDE_StreetsArterial_IOT2_Lay, "CityProjec = '" + trafCol_Num + "'", "", "OBJECTID OBJECTID VISIBLE NONE;TypeofFund TypeofFund VISIBLE NONE;MasterInde MasterInde VISIBLE NONE;OrdinanceR OrdinanceR VISIBLE NONE;Year Year VISIBLE NONE;ZoneID ZoneID VISIBLE NONE;CategoryDe CategoryDe VISIBLE NONE;LocationDe LocationDe VISIBLE NONE;BudgetedCo BudgetedCo VISIBLE NONE;CurrentSta CurrentSta VISIBLE NONE;DesignStar DesignStar VISIBLE NONE;Engineer Engineer VISIBLE NONE;Contractor Contractor VISIBLE NONE;PhoneConta PhoneConta VISIBLE NONE;TargetComp TargetComp VISIBLE NONE;Completed Completed VISIBLE NONE;Comments Comments VISIBLE NONE;CityProjec CityProjec VISIBLE NONE;MapReferen MapReferen VISIBLE NONE;DistrictID DistrictID VISIBLE NONE;ConstStartDate ConstStartDate VISIBLE NONE;EmailConta EmailConta VISIBLE NONE;LASTUPDATE LASTUPDATE VISIBLE NONE;LASTEDITOR LASTEDITOR VISIBLE NONE;SHAPE SHAPE VISIBLE NONE;SHAPE.STLength() SHAPE.STLength() VISIBLE NONE")
		print "Found " + trafCol_Num + " in Arterials."
		
		# Process: Select Layer By Location
		arcpy.SelectLayerByLocation_management(TrfCol_2036A0001Z2, "INTERSECT", SDE_StreetsArterial_IOT2_Lay, artbuffer, "NEW_SELECTION", "NOT_INVERT")

		# Process: Table To Excel
		arcpy.TableToExcel_conversion(TrfCol_2036A0001Z2__6_, TrfCol_2036A0001Z2_xls, "NAME", "CODE")
		print "Made " + secondmetricmoniker + " Excel file for " + trafCol_Num

		# Process: Feature Class To Shapefile (multiple)
		arcpy.FeatureClassToShapefile_conversion(TrfCol_2036A0001Z2__6_, Shapefiles2)
		print "Made " + secondmetricmoniker + " shapefile for " + trafCol_Num
	except:
		print "Couldn't find " + trafCol_Num + " in Bridges."
	del Engineering_SDE_StreetsArterial_IOT2
	del SDE_StreetsArterial_IOT2_Lay
	
		
	
for trafCol_Num in trafCol_Array:
	mxd = arcpy.mapping.MapDocument(mxdpath)
	ddp = mxd.dataDrivenPages
	indexLayer = ddp.indexLayer
	
	arcpy.SelectLayerByAttribute_management(indexLayer, "NEW_SELECTION", "CityProject = '" + trafCol_Num + "'")
	
	print "Exporting " + secondmetricmoniker + "_"  + trafCol_Num + ".pdf"
	ddp.exportToPDF(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + secondmetricmoniker + "_"  + trafCol_Num + ".pdf", "SELECTED")
	print "Exported " + secondmetricmoniker + "_"  + trafCol_Num + ".pdf"
	
	del mxd
	del ddp
	del indexLayer


del mxdpath
mxdpath = r"C:\IOT2\Kickoff\Appr_SSO_NonArt.mxd"

# Test array NonArt
#trafCol_Array = ['2036N3004Z', '2036N3005Z']

# Production array NonArt
trafCol_Array = ['2036D0001Z', '2036N1007Z', '2036N1068Z', '2036N1070Z', '2036N1071Z', '2036N1072Z', '2036N1076Z', '2036N1078Z', '2036N1097Z', '2036N1098Z', '2036N1153Z', '2036N1155Z', '2036N1157Z', '2036N2056Z', '2036N2065Z', '2036N2066Z', '2036N2131Z', '2036N3004Z', '2036N3005Z', '2036N3008Z', '2036N3010Z', '2036N3011Z', '2036N3017Z', '2036N3075Z', '2036N3080Z', '2036N3081Z', '2036N3082Z', '2036N4014Z', '2036N4015Z', '2036N4021Z', '2036N4022Z', '2036N4023Z', '2036N4029Z', '2036N4030Z', '2036N4031Z', '2036N4067Z', '2036N4069Z', '2036N5016Z', '2036N5026Z', '2036N5027Z', '2036N5033Z', '2036N5039Z', '2036N5040Z', '2036N6035Z', '2036N6142Z', '2036N6144Z', '2036N6148Z', '2036N6149Z', '2036N6150Z', '2036N7048Z', '2036N7060Z', '2036N7104Z', '2036N7109Z', '2036N7115Z', '2036N8057Z', '2036N8102Z', '2036N8113Z', '2036N8116Z', '2036N9036Z', '2036N9037Z', '2036N9038Z', '2036N9043Z', '2036N9044Z', '2036N9045Z', '2036N9049Z', '2036N9050Z', '2036N9051Z', '2036N9052Z']

for trafCol_Num in trafCol_Array:
	mxd = arcpy.mapping.MapDocument(mxdpath)
	ddp = mxd.dataDrivenPages
	indexLayer = ddp.indexLayer
	print  rootpath + topfolder + secondfolder + "\\" + trafCol_Num 

	if arcpy.Exists(rootpath + topfolder):
		print "The local path " + rootpath + topfolder + " already exists"
	else:
		# Process: Create Database Connection
		# Process: Create File Folder
		arcpy.CreateFolder_management(rootpath, topfolder)
		print "Created local path " + rootpath + topfolder 
		
	if arcpy.Exists(rootpath + topfolder + secondfolder):
		print "The local path " + rootpath + topfolder + secondfolder + " already exists"
	else:
		# Process: Create Database Connection
		# Process: Create File Folder
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder)
		print "Created local path " + rootpath + topfolder + secondfolder
		
	
	if arcpy.Exists(rootpath + topfolder + secondfolder + "\\" + trafCol_Num):
		print "The local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + " already exists"
	else:
		# Process: Create Database Connection
		# Process: Create File Folder
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder + "\\" + trafCol_Num)
		print "Created local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num 
		
	if arcpy.Exists(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric):
		print "The local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + " already exists"
	else:
		# Process: Create Database Connection
		# Process: Create File Folder
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric)
		print "Created local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric
		
	if arcpy.Exists(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder):
		print "The local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder + " already exists"
	else:
		# Process: Create Database Connection
		# Process: Create File Folder
		arcpy.CreateFolder_management(rootpath, topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder)
		print "Created local path " + rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder

	SDE_StreetsNonArterial_IOT2_ = SDE_StreetsNonArterial_IOTtwo
	Engineering_SDE_StreetsNonArterial_IOT2 = Engineering_SDE_StreetsNonArterial_IOTtwo 
	TrfCol_2036A0001Z = metricmoniker + "_" + trafCol_Num
	TrfCol_2036A0001Z__6_ = TrfCol_2036A0001Z
	TrfCol_2036A0001Z2 = secondmetricmoniker + "_" + trafCol_Num
	TrfCol_2036A0001Z2__6_ = TrfCol_2036A0001Z2
	TrfCol_2036A0001Z_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + metricmoniker + "_" + trafCol_Num + ".xls"
	TrfCol_2036A0001Z2_xls = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + secondmetricmoniker + "_" + trafCol_Num + ".xls"
	TrfCol_2036A0001Z__2_ = metricmoniker + "_" + trafCol_Num
	TrfCol_2036A0001Z__5_ = TrfCol_2036A0001Z__2_
	TrfCol_2036A0001Z_xls__2_ = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + metricmoniker + "_" + trafCol_Num + ".xls"
	TrfCol_2036A0001Z__3_ = metricmoniker + "_" + trafCol_Num
	TrfCol_2036A0001Z__4_ = TrfCol_2036A0001Z__3_
	TrfCol_2036A0001Z_xls__3_ = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + metricmoniker + "_" + trafCol_Num + ".xls"
	Shapefiles = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder
	Shapefiles2 = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + shapefolder
	Shapefiles__2_ = Shapefiles
	Shapefiles__3_ = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder
	Shapefiles__4_ = Shapefiles__3_
	Shapefiles__5_ = rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + metric + "\\" + shapefolder
	Shapefiles__6_ = Shapefiles__5_

	try:
		# Process: Make Feature Layer (4)
		arcpy.MakeFeatureLayer_management(Collisions_TPD__2_, TrfCol_2036A0001Z__2_, "", "", "")

		# Process: Make Feature Layer (2)
		arcpy.MakeFeatureLayer_management(Engineering_SDE_StreetsNonArterial_IOT2, SDE_StreetsNonArterial_IOT2_, "CityProjec = '" + trafCol_Num + "'", "", "OBJECTID OBJECTID VISIBLE NONE;ST_WIDTH ST_WIDTH VISIBLE NONE;ST_Name ST_Name VISIBLE NONE;ZONE ZONE VISIBLE NONE;Street_Typ Street_Typ VISIBLE NONE;FUNCTIONAL FUNCTIONAL VISIBLE NONE;CURB CURB VISIBLE NONE;SW_WIDTH SW_WIDTH VISIBLE NONE;MasterInde MasterInde VISIBLE NONE;MapReferen MapReferen VISIBLE NONE;CityProjec CityProjec VISIBLE NONE;OrdinanceR OrdinanceR VISIBLE NONE;Year Year VISIBLE NONE;DistrictID DistrictID VISIBLE NONE;ZoneID ZoneID VISIBLE NONE;CategoryDe CategoryDe VISIBLE NONE;BudgetedCo BudgetedCo VISIBLE NONE;CurrentSta CurrentSta VISIBLE NONE;DesignStar DesignStar VISIBLE NONE;Engineer Engineer VISIBLE NONE;Contractor Contractor VISIBLE NONE;PhoneConta PhoneConta VISIBLE NONE;EmailConta EmailConta VISIBLE NONE;TargetComp TargetComp VISIBLE NONE;Completed Completed VISIBLE NONE;Comments Comments VISIBLE NONE;SUBDIVISIO SUBDIVISIO VISIBLE NONE;TypeofFund TypeofFund VISIBLE NONE;LocationDe LocationDe VISIBLE NONE;ConstStartDate ConstStartDate VISIBLE NONE;LASTUPDATE LASTUPDATE VISIBLE NONE;LASTEDITOR LASTEDITOR VISIBLE NONE;SHAPE SHAPE VISIBLE NONE;SHAPE.STLength() SHAPE.STLength() VISIBLE NONE")
		print "Found " + trafCol_Num + " in Non-arterials."
		
		# Process: Select Layer By Location (2)
		arcpy.SelectLayerByLocation_management(TrfCol_2036A0001Z__2_, "INTERSECT", SDE_StreetsNonArterial_IOT2_, nonartbuffer, "NEW_SELECTION", "NOT_INVERT")
		
		resultSSOs = arcpy.GetCount_management(TrfCol_2036A0001Z__2_)
		count = int(resultSSOs.getOutput(0))
		print str(count) + " SSOs in " + trafCol_Num
		
		if count > 0:
		
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
			
			arcpy.TableToExcel_conversion(TrfCol_2036A0001Z__6_, TrfCol_2036A0001Z_xls, "NAME", "CODE")
			print "Made Excel file for " + trafCol_Num
			# Process: Feature Class To Shapefile (multiple)
			arcpy.FeatureClassToShapefile_conversion(TrfCol_2036A0001Z__6_, Shapefiles)
			print "Made shapefile for " + trafCol_Num
		else:
			print "No SSOs located nearby"
	except:
		print "Couldn't find " + trafCol_Num + " in Non-arterials."
	
	del Engineering_SDE_StreetsNonArterial_IOT2
	del SDE_StreetsNonArterial_IOT2_
	
	Engineering_SDE_StreetsNonArterial_IOT2 = Engineering_SDE_StreetsNonArterial_IOTtwo
	SDE_StreetsNonArterial_IOT2_ = SDE_StreetsNonArterial_IOTtwo
	
	try:
		# Process: Make Feature Layer (5)
		arcpy.MakeFeatureLayer_management(Collisions_TPD__7_, TrfCol_2036A0001Z2, "", "", "")

		# Process: Make Feature Layer
		arcpy.MakeFeatureLayer_management(Engineering_SDE_StreetsNonArterial_IOT2, SDE_StreetsNonArterial_IOT2_, "CityProjec = '" + trafCol_Num + "'", "", "OBJECTID OBJECTID VISIBLE NONE;TypeofFund TypeofFund VISIBLE NONE;MasterInde MasterInde VISIBLE NONE;OrdinanceR OrdinanceR VISIBLE NONE;Year Year VISIBLE NONE;ZoneID ZoneID VISIBLE NONE;CategoryDe CategoryDe VISIBLE NONE;LocationDe LocationDe VISIBLE NONE;BudgetedCo BudgetedCo VISIBLE NONE;CurrentSta CurrentSta VISIBLE NONE;DesignStar DesignStar VISIBLE NONE;Engineer Engineer VISIBLE NONE;Contractor Contractor VISIBLE NONE;PhoneConta PhoneConta VISIBLE NONE;TargetComp TargetComp VISIBLE NONE;Completed Completed VISIBLE NONE;Comments Comments VISIBLE NONE;CityProjec CityProjec VISIBLE NONE;MapReferen MapReferen VISIBLE NONE;DistrictID DistrictID VISIBLE NONE;ConstStartDate ConstStartDate VISIBLE NONE;EmailConta EmailConta VISIBLE NONE;LASTUPDATE LASTUPDATE VISIBLE NONE;LASTEDITOR LASTEDITOR VISIBLE NONE;SHAPE SHAPE VISIBLE NONE;SHAPE.STLength() SHAPE.STLength() VISIBLE NONE")
		print "Found " + trafCol_Num + " in Arterials."
		
		# Process: Select Layer By Location
		arcpy.SelectLayerByLocation_management(TrfCol_2036A0001Z2, "INTERSECT", SDE_StreetsNonArterial_IOT2_, nonartbuffer, "NEW_SELECTION", "NOT_INVERT")

		# Process: Table To Excel
		arcpy.TableToExcel_conversion(TrfCol_2036A0001Z2__6_, TrfCol_2036A0001Z2_xls, "NAME", "CODE")
		print "Made " + secondmetricmoniker + " Excel file for " + trafCol_Num

		# Process: Feature Class To Shapefile (multiple)
		arcpy.FeatureClassToShapefile_conversion(TrfCol_2036A0001Z2__6_, Shapefiles2)
		print "Made " + secondmetricmoniker + " shapefile for " + trafCol_Num
	except:
		print "Couldn't find " + trafCol_Num + " in Bridges."
	del Engineering_SDE_StreetsNonArterial_IOT2
	del SDE_StreetsNonArterial_IOT2_
	
	
for trafCol_Num in trafCol_Array:
	mxd = arcpy.mapping.MapDocument(mxdpath)
	ddp = mxd.dataDrivenPages
	indexLayer = ddp.indexLayer
	
	arcpy.SelectLayerByAttribute_management(indexLayer, "NEW_SELECTION", "CityProject = '" + trafCol_Num + "'")
	
	print "Exporting " + secondmetricmoniker + "_"  + trafCol_Num + ".pdf"
	ddp.exportToPDF(rootpath + topfolder + secondfolder + "\\" + trafCol_Num + "\\" + secondmetric + "\\" + secondmetricmoniker + "_"  + trafCol_Num + ".pdf", "SELECTED")
	print "Exported " + secondmetricmoniker + "_"  + trafCol_Num + ".pdf"
	
	del mxd
	del ddp
	del indexLayer



print "Done."