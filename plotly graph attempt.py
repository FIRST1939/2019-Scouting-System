# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:11:12 2019

@author: Mason
"""
import plotly.express as px
from tkinter import filedialog

fig = px.line(filedialog.askopenfilename(title = 'select MatchList file'), x = 'teamNo', y = 'crossHABLine', title='Team Number vs crossed hab')
fig.show()