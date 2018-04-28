# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 20:15:32 2018
No schedul for human and robot 
@author: robot
"""

import copy
import math 
import humanAndRobotClass as hr
import numpy as np
import matplotlib.pyplot as plt
import drawHumAndRob as mydraw
from enum import Enum,auto

class EventMode(Enum):
    happen = auto()
    end = auto()
    NONE = auto()




# return dictionary

def findEventRob(happenTimeLst = [], endTimeLst =[]):
    minHappenTime = min(happenTimeLst)
    minHappenIndex = happenTimeLst.index(minHappenTime)
    minEndTime = min(endTimeLst)
    minEndIndex = endTimeLst.index(minEndTime)
    if(minEndTime<minHappenTime):
        return {'Index':minEndIndex,'Type':EventMode.end.value}
    else:
        return {'Index':minHappenIndex,'Type':EventMode.happen.value}
    

"""
function  is upper
"""

g_robNum = 15
g_humNum = 5

humDrawLstx = []
humDrawLsty = []

for i in range(g_humNum):
    humDrawLstx.append([])
    humDrawLsty.append([])


robLst = []
humLst = []
#事件发生时刻
happenTimeLst  = []
#事件结束时刻
endTimeLst = []

    
    


for i in range(g_robNum):
    robot = hr.Robot(len(robLst))
    robot.controlHumID =  int(i / 3.0)
    robot.randEventTime()
    robot.displayRobot()
    robLst.append(copy.deepcopy(robot))
#    
    happenTimeLst.append(robot.eventHappenTime)
    endTimeLst.append(robot.eventEndTime)
    

for i in range(g_humNum):
    human = hr.Human()
    human.displayHuman()
    human.saveDataInside()
    humLst.append(copy.deepcopy(human))    
#    humLst[i].saveData(humDrawLstx[i],humDrawLsty[i])
    


for eventNum in range(100):
     res = findEventRob(happenTimeLst,endTimeLst)
     robID = res['Index']
     controlHumID = robLst[robID].controlHumID
     rob = robLst[robID]
     eventType = res['Type']
     hum = humLst[controlHumID]
#     print("robID = ",robID)
#     print("controlHumID = ",controlHumID)
     if(eventType == EventMode.happen.value):
#         print('happen type')
         hum.changeTime = rob.eventHappenTime
         hum.saveDataInside()
         humLst[controlHumID].cWorkLoad = humLst[controlHumID].cWorkLoad - 3
         if(controlHumID ==0):
             print("[happen] cWorkLoad = ",humLst[controlHumID].cWorkLoad)
         happenTimeLst[robID] = math.inf
     else:
#         print('end type')
         hum.changeTime = rob.eventEndTime
         hum.saveDataInside()

         humLst[controlHumID].cWorkLoad = humLst[controlHumID].cWorkLoad + 3
         
         if(controlHumID ==0):
             print("[end] cWorkLoad = ",humLst[controlHumID].cWorkLoad)


         rob.randEventTime()
#         dur = rob.eventEndTime - rob.eventHappenTime
#         print('dur = ',dur)
         happenTimeLst[robID] = rob.eventHappenTime
         endTimeLst[robID] = rob.eventEndTime
     
#     rob.displayRobot()
     hum.saveDataInside()
    
    
mydraw.AgentWorkLoadTrace(humLst)

