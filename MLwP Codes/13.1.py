# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 22:38:41 2020

@author: myousuf
"""

# Load libraries
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

# Load data with only two features
boston = load_boston()
features = boston.data[:,0:2]
target = boston.target

# Create linear regression
regression = LinearRegression()

# Fit the linear regression
model = regression.fit(features, target)
