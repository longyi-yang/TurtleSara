# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:17:18 2020

@author: 杨隆一
"""
#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Longyi Yang (longyi.yang@duke.edu)
# Date: 2020/9/22
#--------------------------------------------------------------

# Copy and paste a line of data as the lineString variable value
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"



# Use the split command to parse the items in lineString into a list object
lineData = str.split(lineString)

# Assign variables to specfic items in the list
record_id = lineData[0]             # ARGOS tracking record ID
obs_date = lineData[2]   # Observation date
ob_lc = lineData[4]                 # Observation Location Class
obs_lat = lineData[6]               # Observation Latitude
obs_lon = lineData[7]               # Observation Longitude

# Print information to the use
print ("Record {recordID} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")
