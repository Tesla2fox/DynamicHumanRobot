# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 20:15:32 2018

@author: robot
"""

import copy
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
    minEndIndex = endTimeLst.index(endTimeLst)
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
    happenTimeLst.append()    
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
     robID = res['index']
     controlHumID = robLst[robID].controlHumID
     
    
mydraw.AgentWorkLoadTrace(humLst)
#s = np.random.poisson(100)





#import random
#arrival_rate = 100
#arrive_times = []
#t = 0
#for i in range(arrival_rate):
#    t += random.expovariate(arrival_rate)
#    arrive_times.append(t)
#
#
## Poisson分布
#x = np.random.poisson(lam=5, size=10000)  # lam为λ size为k
#pillar = 15
#a = plt.hist(x, bins=pillar, normed=True, range=[0, pillar], color='g', alpha=0.5)
#plt.plot(a[1][0:pillar], a[0], 'r')
#plt.grid()
#plt.show()
