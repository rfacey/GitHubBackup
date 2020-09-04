# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:36:11 2020

@author: myousuf
"""

# Load libraries
import numpy as np
from sklearn.preprocessing import Binarizer

# Create feature
age = np.array([[6],
                [120],
                [20],
                [36],
                [65]])

# Create binarizer
binarizer = Binarizer(18)

# Transform feature
bin=binarizer.fit_transform(age)
#Second, we can break up numerical features according to multiple thresholds:
# Bin feature
dig=np.digitize(age, bins=[18,30, 68], right=True)

#dig2=np.digitize(age,bins=[10,30,64], right=True)