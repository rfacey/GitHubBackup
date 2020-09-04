# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:02:30 2020

@author: myousuf
"""
import numpy as np
import matplotlib.pyplot as plt
# Load scikit-learn's datasets
from sklearn import datasets

# Load digits dataset
digits = datasets.load_digits()

# Create features matrix
features = digits.data

# Create target vector
target = digits.target

# # Create function that adds 100 to something
add_100 = lambda i: i + 0

# Create vectorized function
vectorized_add_100 = np.vectorize(add_100)

# Apply function to all elements in matrix
FT=vectorized_add_100(features)


# View first observation
features[0]
plt.scatter(FT[:,20],FT[:,10], c=target)
plt.show()
