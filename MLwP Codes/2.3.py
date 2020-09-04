# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:23:41 2020

@author: myousuf
"""

# Load library
import pandas as pd

# Create URL
url = 'https://tinyurl.com/qpunt8y'

# Load dataset
dataframe = pd.read_csv(url)

# View first two rows
dataframe.head(2)
