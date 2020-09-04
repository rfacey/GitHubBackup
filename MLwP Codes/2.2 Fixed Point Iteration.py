# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:02:30 2020

@author: myousuf
"""
import numpy as np
import matplotlib.pyplot as plt
# Load scikit-learn's datasets
# Load library
from sklearn.datasets import make_regression

# Generate features matrix, target vector, and the true coefficients
features, target, coefficients = make_regression(n_samples = 100,
n_features = 3,
n_informative = 3,
n_targets = 1,
noise = 0.0,
coef = True,
random_state = 1)

# View feature matrix and target vector
print('Feature Matrix\n', features[:5])
print('Target Vector\n', target[:5])
#import matplotlib.pyplot as plt

# View scatterplot
plt.scatter(features[:,0], features[:,1], c=target)
plt.show()
