# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:27:40 2020

@author: myousuf
"""

# Load library
import pandas as pd

# Create DataFrame
houses = pd.DataFrame()
houses['Price'] = [534433, 392333, 293222, 4322032, 232776]
houses['Bathrooms'] = [2, 3.5, 2, 116, 19]
houses['Square_Feet'] = [1500, 2500, 1500, 48000, 2400]

# Filter observations
houses[houses['Bathrooms'] < 10]
#Second, we can mark them as outliers and include it as a feature:
# Load library
import numpy as np

# Create feature based on boolean condition
houses["Outlier"] = np.where(houses["Bathrooms"] < 10, 0, 1)

# Show data
print(houses)
#Finally, we can transform the feature to dampen the effect of the outlier:
# Log feature
houses["Log_Of_Square_Feet"] = [np.log(x) for x in houses["Square_Feet"]]

# Show data
print(houses)
