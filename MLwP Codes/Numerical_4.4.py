# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 00:15:38 2020

@author: myousuf
"""

# Load libraries
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Create feature matrix
features = np.array([[2, 3],
                     [2, 3],
                     [2, 3]])

# Create PolynomialFeatures object
polynomial_interaction = PolynomialFeatures(degree=2, include_bias=False)

# Create polynomial features
poly=polynomial_interaction.fit_transform(features)
