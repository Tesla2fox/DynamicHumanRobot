# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 20:14:13 2018
猪头 展骄杨
@author: robot
"""

"""
manage_by_consent = MBC
manage_by_exception = MBE
"""
from random import uniform

from enum import Enum,auto
class RobotMode(Enum):
    MBC = auto()
    MBE = auto()
    NONE = auto()
    
class HumanMode(Enum):
    MBC = auto()
    MBE = auto()
    NONE = auto()



class Robot:
    def __init__(self):
        self.mode = RobotMode.NONE.value
    def displayRobot(self):
        print('mode = ',self.mode)


class Human:
    def __init__(self):
        self.mode  = HumanMode.MBE.value
    def displayHuman(self):
        print('mode = ',self.mode)

        

        

    