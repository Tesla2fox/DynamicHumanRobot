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
import humanAndRobotClass as hr


def AgentWorkLoadTrace(humLst = [], drawType = 0):
#    tracel = []
    if (drawType == hr.DrawType.no_schedule.value):
        filePostfix = '_no_schedule'
    else:
        filePostfix = '_schedule'
        
    for i in range(len(humLst)):
        lname = 'human_'
        lname = lname +str(i)
        for j in range(len(humLst[i].cworkLoadLst)):
            humLst[i].cworkLoadLst[j] = humLst[i].maxWorkLoad -  humLst[i].cworkLoadLst[j]
            
        trace = go.Scatter(x=humLst[i].cTimeLst,
                           y=humLst[i].cworkLoadLst,
                           mode= 'lines+markers',
                           name = lname,
                           line = dict(shape ='v'))
        layout = dict(title = '操作员 '+str(i)+' 工作负荷示意图',
              xaxis = dict(title = '时间'),
              yaxis = dict(title = '操作员工作负荷'),
              )
        lstx =[]
        lsty =[]
        lstx.append(0)
        lsty.append(humLst[i].maxWorkLoad)
        lsty.append(humLst[i].maxWorkLoad)        
        lstx.append(max(humLst[i].cTimeLst))

        maxTrace = go.Scatter(x=lstx,
                           y=lsty,
                           mode= 'lines+markers',
                           name = '操作员的最大工作负荷',
                           line = dict(
                                   color=('rgb(238,29,36)'),
                                   shape ='v',
                                   width = 6))        
        data = []
        data.append(cp.copy(trace))
        data.append(cp.copy(maxTrace))
        fig = dict(data = data ,layout = layout)
        plotly.offline.plot(fig,filename = 'humStateFig'+str(i) + filePostfix)
#        tracel.append(cp.copy(trace))
#    plotly.offline.plot(tracel,'humStateFig')
    