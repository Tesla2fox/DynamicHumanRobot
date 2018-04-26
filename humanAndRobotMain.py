# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 20:15:32 2018

@author: robot
"""

import copy
import humanAndRobotClass as hr
import numpy as np
import matplotlib.pyplot as plt


g_robNum = 15
g_humNum = 5

humDrawLstx = []
humDrawLsty = []

for i in range(g_humNum):
    humDrawLstx.append([])
    humDrawLsty.append([])


robLst = []
humLst = []

for i in range(g_robotNum):
    robot = hr.Robot(len(robLst))
    robot.controlHumID =  int(i / 3.0)
    robot.randEventTime()
    robot.displayRobot()    
    robLst.append(copy.deepcopy(robot))
    

for i in range(g_humanNum):
    human = hr.Human()
    human.displayHuman()
    humLst.append(copy.deepcopy(human))
    humLst[i].saveData(humDrawLstx[i],humDrawLsty[i])
    
    
#s = np.random.poisson(100)





import random
arrival_rate = 100
arrive_times = []
t = 0
for i in range(arrival_rate):
    t += random.expovariate(arrival_rate)
    arrive_times.append(t)


# Poisson分布
x = np.random.poisson(lam=5, size=10000)  # lam为λ size为k
pillar = 15
a = plt.hist(x, bins=pillar, normed=True, range=[0, pillar], color='g', alpha=0.5)
plt.plot(a[1][0:pillar], a[0], 'r')
plt.grid()
plt.show()
