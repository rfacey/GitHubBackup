# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:02:30 2020

@author: myousuf
"""
import numpy as np
import matplotlib.pyplot as plt
# Load scikit-learn's datasets
# Load library
from sklearn.datasets import make_blobs

# Generate feature matrix and target vector
features, target = make_blobs(n_samples = 100,
n_features = 2,
centers = 3,
cluster_std = 0.5,
shuffle = True,
random_state = 1)

# View feature matrix and target vector
print('Feature Matrix\n', features[:3])
print('Target Vector\n', target[:3])

# View scatterplot
plt.scatter(features[:,0], features[:,1], c=target)
plt.show()
