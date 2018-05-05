# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 20:15:32 2018
schedul for human and robot
没有考虑人对智能体的信任关系 
@author: robot
"""

import copy
import math 
import humanAndRobotClass as hr
import numpy as np
import matplotlib.pyplot as plt
import drawHumAndRob as mydraw
from enum import Enum,auto
import random
random.seed(1)

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


humDrawLstx = []
humDrawLsty = []

for i in range(hr.g_humNum):
    humDrawLstx.append([])
    humDrawLsty.append([])


robLst = []
humLst = []
#事件发生时刻
happenTimeLst  = []
#事件结束时刻
endTimeLst = []

    
    
for i in range(hr.g_robNum):
    robot = hr.Robot(len(robLst))
    robot.controlHumID =  int(i / 3.0)
    robot.randEventTime()
    robot.displayRobot()
    robLst.append(copy.deepcopy(robot))
#    
    happenTimeLst.append(robot.eventHappenTime)
    endTimeLst.append(robot.eventEndTime)
    

for i in range(hr.g_humNum):
    human = hr.Human()
    human.displayHuman()
    human.saveDataInside()
    humLst.append(copy.deepcopy(human))    
#    humLst[i].saveData(humDrawLstx[i],humDrawLsty[i])
    


for eventNum in range(100):
     res = findEventRob(happenTimeLst,endTimeLst)     
     robID = res['Index']
     rob = robLst[robID]
     eventType = res['Type']

#     controlHumID = robLst[robID].controlHumID
#     
     print("[event]__robID = ",robID)
#     print("controlHumID = ",controlHumID)
     if(eventType == EventMode.happen.value):
#         print('happen type')
         #decide the control human id
         DeValLst  = []
         for unit in humLst:
             if(unit.cWorkLoad<=0):
                 DeValLst.append(0)
             else:
#                 print('[happen]_trust = ',unit.trustVal[robID])
#                 print('[happen]_workLoad  = ',unit.cWorkLoad)
#                 DeValLst.append(unit.trustVal[robID]/unit.cWorkLoad*10)
                 DeValLst.append(unit.cWorkLoad*unit.trustVal[robID])
         
         deVal = max(DeValLst)
         controlHumID = DeValLst.index(deVal)
         print('[happen]_controlHumID = ',controlHumID)
         print('[happen]_DeValLst = ',DeValLst)
         print('[happen]_max = ',deVal)

         rob.controlHumID = controlHumID
         hum = humLst[controlHumID]
         hum.changeTime = rob.eventHappenTime
         hum.saveDataInside()
         
         modeDeVal = hum.trustVal[robID]/hum.cWorkLoad*10
         mode = 1
         if(modeDeVal>7):
             #例外管理
             mode  = hr.HumanMode.MBE.value
         else:
             if(modeDeVal<7):
                 #同意管理
                 mode = hr.HumanMode.MBC.value
             else:
                 mode = random.randint(1,2)
         print('mode = ',mode)
         hum.controlMode[robID] = mode
         if(mode == hr.HumanMode.MBE.value):
             #例外管理
             print('[happen]_ MBE')
             hum.cWorkLoad = hum.cWorkLoad -2
         else:
             #同意管理
             print('[happen]_ MBE')

             hum.cWorkLoad = hum.cWorkLoad -3
         happenTimeLst[robID] = math.inf
     else:
#         print('end type')

         controlHumID = rob.controlHumID  
         hum = humLst[controlHumID]
         
         hum.changeTime = rob.eventEndTime
         hum.saveDataInside()
         
         if(hum.controlMode[robID]==hr.HumanMode.MBE.value):
             hum.cWorkLoad = hum.cWorkLoad + 2
         else:
             hum.cWorkLoad = hum.cWorkLoad + 3
         
         rob.randEventTime()
         
#         dur = rob.eventEndTime - rob.eventHappenTime
#         print('dur = ',dur)
         hum.trustVal[robID] = hum.trustVal[robID] + rob.trustChange
         happenTimeLst[robID] = rob.eventHappenTime
         endTimeLst[robID] = rob.eventEndTime
     
#     rob.displayRobot()
     hum.saveDataInside()
    
    
mydraw.AgentWorkLoadTrace(humLst,drawType = hr.DrawType.schedule.value)

