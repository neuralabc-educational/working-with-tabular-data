# -*- coding: utf-8 -*-
"""
Created on Fri May 26 13:44:34 2023
@author: mgardner

Importing data for the Cue Map experiment

"""
import numpy as np
import re
###########OUTLINE######################################
#get the data folder location

#open the data file

#read the header information

#get rat number

#get experiment information

#import data

#look for double pound sign

#for data collection determine the inpokes and outpokes for the duration of each index 
#the index refers to a cue

#loop through all indices in the session and collect data

#save the data
#############################################################3



#get the data folder location
data_folder = 'C:/Data/Cue Map/Pi_021523_Run/Data'

file  = 'CM02-01_23.txt'

#get full path of file
filename = data_folder + '/' + file

#open the data file
with open (filename, 'r') as r:
    f = r.readlines()

#loop through each line in the headers
for line in f:
    
    #determine whether this is header or not
    if line == '##':
        break

    #check for the reward zones
    elif line[:12] == 'Reward Zones':
        reward_zones = [int(s) for s in re.findall(r'\d+', line)]
        continue
    
        #check for Date
    elif
    
        #check for
        



#read the header information

#get rat number

#get experiment information

#import data

#look for double pound sign

#for data collection determine the inpokes and outpokes for the duration of each index 
#the index refers to a cue

#loop through all indices in the session and collect data

#save the data
