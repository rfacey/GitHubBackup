# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 23:44:03 2020

@author: myousuf
"""

# Load libraries
import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.datasets import make_blobs

# Create simulated data
features, _ = make_blobs(n_samples = 10,
                         n_features = 2,
                         centers = 1,
                         random_state = 1)

# Replace the first observation's values with extreme values
features[0,0] = 10000
features[0,1] = 10000

# Create detector
outlier_detector = EllipticEnvelope(contamination=0.2)

# Fit detector
of=outlier_detector.fit(features)

# Predict outliers
ol=outlier_detector.predict(features)
##########################################################
# Create one feature
feature = features[:,0]

# Create a function to return index of outliers
def indicies_of_outliers(x):
    q1, q3 = np.percentile(x, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (iqr * 1.5)
    upper_bound = q3 + (iqr * 1.5)
    return np.where((x > upper_bound) | (x < lower_bound))

# Run function
ans=indicies_of_outliers(feature)

