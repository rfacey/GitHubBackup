# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 23:04:50 2020

@author: myousuf
"""

# Load libraries
import numpy as np
from sklearn.preprocessing import Normalizer

# Create feature matrix
features = np.array([[0.5, 0.5],
                     [1.1, 3.4],
                     [1.5, 20.2],
                     [1.63, 34.4],
                     [10.9, 3.3]])

# Create normalizer
normalizer = Normalizer(norm="l2")

# Transform feature matrix
nor=normalizer.transform(features)

# Transform feature matrix
L1_norm = Normalizer(norm="l1").transform(features)

L2_norm = Normalizer(norm="l2").transform(features)
