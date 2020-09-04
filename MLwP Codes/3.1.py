# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:23:41 2020

@author: myousuf
"""

# Load library
import pandas as pd

# Create DataFrame
dataframe = pd.DataFrame()

# Add columns
dataframe['Name'] = ['Jacky Jackson', 'Steven Stevenson']
dataframe['Age'] = [38, 25]
dataframe['Driver'] = [True, False]

# Show DataFrame
dataframe
# Create row
new_person = pd.Series(['Molly Mooney', 40, True], index=['Name','Age','Driver'])

# Append row
nd=dataframe.append(new_person, ignore_index=True)
print(nd)
