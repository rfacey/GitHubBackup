# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 23:04:58 2020

@author: myousuf
"""

# Load libraries
import pandas as pd
import numpy as np

# Create date range
time_index = pd.date_range('06/06/2017', periods=100000, freq='30S')

# Create DataFrame
dataframe = pd.DataFrame(index=time_index)

# Create column of random values
randomV=dataframe['Sale_Amount'] = np.random.randint(1, 10, 100000)

# Group rows by week, calculate sum per week
group1=dataframe.resample('W').sum()


# Group rows by week, calculate mean per week
group2=dataframe.resample('W').mean()

# Group by month, count rows
group3=dataframe.resample('M').count()


# Print first two names uppercased
for name in dataframe['Name'][0:2]:
    print(name.upper())
