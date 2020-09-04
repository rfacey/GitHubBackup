# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:23:41 2020

@author: myousuf
"""

# Load library
import pandas as pd

# Create URL
url = 'https://tinyurl.com/titanic-csv'

# Number of Columns want to display
pd.set_option('display.max_columns', 6)
pd.set_option('display.max_rows', 226)


# Load data
dataframe = pd.read_csv(url)

# Create function
def uppercase(x):
    return x.upper()

# Apply function, show two rows
name=dataframe['Name'].apply(uppercase)[0:12]

# Group rows, apply function to groups
name2=dataframe.groupby('Sex').apply(lambda x: x.count())


# Create Data Frame
data_a = {'id': ['1', '2', '3'],
          'first': ['Alex', 'Amy', 'Allen'],
          'last': ['Anderson', 'Ackerman', 'Ali']}
dataframe_a = pd.DataFrame(data_a, columns = ['id', 'first', 'last'])

# Create DataFrame
data_b = {'id': ['4', '5', '6'],
          'first': ['Billy', 'Brian', 'Bran'],
          'last': ['Bonder', 'Black', 'Balwner']}
dataframe_b = pd.DataFrame(data_b, columns = ['id', 'first', 'last'])

# Concatenate DataFrames by rows
name3=pd.concat([dataframe_a, dataframe_b], axis=0)

# Concatenate DataFrames by columns
name4=pd.concat([dataframe_a, dataframe_b], axis=1)

#Alternatively we can use append to add a new row to a DataFrame:
# Create row
row = pd.Series([10, 'Chris', 'Chillon'], index=['id', 'first', 'last'])

# Append row
name5=dataframe_a.append(row, ignore_index=True)

