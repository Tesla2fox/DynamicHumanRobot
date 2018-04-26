# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 20:14:13 2018

@author: robot
"""

"""
manage_by_consent = MBC
manage_by_exception = MBE

假设，同意管理是占用操作员的2个工作负荷
例外管理是占用操作员的3个工作负荷



"""
from random import uniform
import random
import copy


from enum import Enum,auto
class RobotMode(Enum):
    MBC = auto()
    MBE = auto()
    NONE = auto()
    
class HumanMode(Enum):
    MBC = auto()
    MBE = auto()
    NONE = auto()

class RobotEvent(Enum):
    #  coverage search task
    cTaskAllocation = auto()
    cPlan = auto()
    # scout task
    sTaskAllocation = auto()
    sPlan = auto()
    # attack task
    aTaskAllocation = auto()
    aPlan = auto()
    #
    NONE = auto()

class Robot:
    def __init__(self,i = 0):
        self.mode = RobotMode.NONE.value
        self.index = i
        self.changeTime = 0
        self.eventType = RobotEvent.NONE.value
        self.controlHumID = -1
    def displayRobot(self):
        print('[Robot] ',self.index,' mode = ',self.mode
              ,' humID = ',self.controlHumID)
    def randEventTime(self):
        if(self.eventType%2):
            print('是奇数事件')
            if 
        else:
            print('是偶数事件')
                
            
        

class Human:
    def __init__(self,i = 0):
        self.mode  = HumanMode.MBE.value
        self.index = i
        #cworkLoad 表示当前工作负荷
        self.cWorkload = random.randint(7,10)
        self.maxWorkLoad = self.cWorkload
        self.changeTime = 0
        self.cTimeLst = []
        self.cworkLoadLst = []
    def displayHuman(self):
        print('[Human] ',self.index,' mode = ',self.mode)
    def saveDataInside(self):
        self.cTimeLst.append(copy.copy(self.changeTime))
        self.cworkLoadLst.append(copy.copy(self.cworkload))
#    def saveData(self,lstx = [],lsty = []):
#        lstx.append(copy.copy(self.changeTime))
#        lsty.append(copy.copy(self.workload))
            

        
        

    