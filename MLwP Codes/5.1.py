# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 22:32:55 2020

@author: myousuf
"""

# Import libraries
import array
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer

# Create feature
feature = np.array([["Texas"], ["California"],["Texas"],["Delaware"], ["Texas"]])

# Create one-hot encoder
one_hot = LabelBinarizer()

# One-hot encode feature
one_hot.fit_transform(feature)
#We can use the classes_ method to output the classes:
# View feature classes
one_hot.classes_
#If we want to reverse the one-hot encoding, we can use inverse_transform:
# Reverse one-hot encoding
one_hot.inverse_transform(one_hot.transform(feature))
array(['Texas', 'California', 'Texas', 'Delaware', 'Texas'],       
      dtype='<U10')
#We can even use pandas to one-hot encode the feature:
# Import library
#import pandas as pd

# Create dummy variables from feature
#pd.get_dummies(feature[:,0])
