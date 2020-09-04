# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:23:41 2020

@author: myousuf
"""

import pandas as pd
df = pd.read_csv (r'C:\Users\myousuf\Dropbox\MML\MLwP Codes\Att_Math_201_191.csv')
#df = pd.read_excel (r'D:\MY Teaching at KFUPM\Semester 191\Math201-191\Att-Math-201-191.xls', sheet_name='Math201-Sec08')
#print (df)
print(df.head(12))
df.describe()