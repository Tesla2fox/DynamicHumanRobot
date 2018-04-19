# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 20:15:32 2018

@author: robot
"""

import copy
import humanAndRobot as hr


g_robotNum = 15
g_humanNum = 5


robotList = []
humanList = []

for i in range(g_robotNum):
    robot = hr.Robot()
    robotList.append(copy.deepcopy(robot))

for i in range(g_humanNum):
    human = hr.Human()
    humanList.append(copy.deepcopy(human))

