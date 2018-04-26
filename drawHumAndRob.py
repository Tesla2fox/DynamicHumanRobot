# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 21:05:58 2018

画图函数
@author: robot
"""

import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import copy as cp



def AgentWorkLoadTrace(humLst = []):
    tracel = []
    for i in range(len(humLst)):
        lname = 'human_'
        lname = lname +str(i)
        trace = go.Scatter(x=humLst[i].cTimeLst,
                           y=humLst[i].cworkLoadLst,
                           mode= 'lines+markers',
                           name = lname,
                           line = dict(shape ='vh'))
        tracel.append(cp.copy(trace))
    plotly.offline.plot(tracel,'humStateFig')
    