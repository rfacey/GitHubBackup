# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 23:04:49 2020

@author: myousuf
"""

# Load libraries
import numpy as np
from sklearn import preprocessing

# Create feature
feature = np.array([[-500.5],
                    [-100.1],
                    [0],
                    [100.1],
                    [900.9]])

# Create scaler
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))

# Scale feature
scaled_feature = minmax_scale.fit_transform(feature)

# Show feature
scaled_feature

####################
# Create scaler
x = np.array([[-1000.1],
              [-200.2],
              [500.5],
              [600.6],
              [9000.9]])

# Create scaler
scaler = preprocessing.StandardScaler()

# Transform the feature
standardized = scaler.fit_transform(x)

print("Mean:", round(standardized.mean()))
print("Standard deviation:", standardized.std())


# Show feature
standardized

# Create scaler
robust_scaler = preprocessing.RobustScaler()

# Transform feature
rs=robust_scaler.fit_transform(x)




