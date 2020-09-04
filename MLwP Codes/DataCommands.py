# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:23:41 2020

@author: myousuf
"""

# Load library
import pandas as pd
import collections
import numpy as np

# Number of Columns want to display
pd.set_option('display.max_columns', 6)
pd.set_option('display.max_rows', 226)
# Create URL
url = 'https://tinyurl.com/titanic-csv'

# Load data as a dataframe
dataframe = pd.read_csv(url)

# Show first 5 rows
df=dataframe.head(12)

# Print first two names uppercased
for name in dataframe['Name'][0:5]:
    print(name.upper())



# Describe the data set
ds=dataframe.describe()

# Show first 4 rows
fr=dataframe.iloc[1:5]

# Set index and search by index
dataframe = dataframe.set_index(dataframe['Name'])

# Show row by given name
name=dataframe.loc['Allison, Mrs Hudson JC (Bessie Waldo Daniels)']

# Show top two rows where column 'sex' is 'female'
sex=dataframe[dataframe['Sex'] == 'female'].head(2)


# Filter rows by sex and age and display first FOUR rows
age=dataframe[(dataframe['Sex'] == 'female') & (dataframe['Age'] >= 60)].head(4)


# Replace values female by Woman, show 12 rows
replace=dataframe['Sex'].replace("female", "Woman").head(12)

# Replace "female" and "male with "Woman" and "Man"
replace2=dataframe['Sex'].replace(["female", "male"], ["Woman", "Man"]).head(12)

# Replace values, show 12 rows
value=dataframe.replace(1, "One").head(12)

# Rename column header name, show 5 rows
header=dataframe.rename(columns={'PClass': 'Passenger Class'}).head(5)

# Rename more column headers, show 5 rows
header2=dataframe.rename(columns={'PClass': 'Passenger Class', 'Sex': 'Gender'}).head(2)

# Create dictionary of Colums headers
column_names = collections.defaultdict(str)

# Create keys
for name in dataframe.columns:
    column_names[name]

# Show dictionary
column_names


# Calculate statistics 
#print('Maximum age:', dataframe['Age'].max())
#print('Minimum age:', dataframe['Age'].min())
#print('Mean of ages:', dataframe['Age'].mean())
#print('Sum of ages:', dataframe['Age'].sum())
#print('Count ages:', dataframe['Age'].count())
#print('SD of age:', dataframe['Age'].std())
#print('mode age:', dataframe['Age'].mode())
#print('Kurtosis of ages:', dataframe['Age'].kurt())
#print('Skew of ages:', dataframe['Age'].skew())
#print('standard error of mean of ages:', dataframe['Age'].sem())
#print('median ages:', dataframe['Age'].median())


# Show counts
counts=dataframe.count()

# Select unique values
unique=dataframe['Sex'].unique()

# Show counts
counts2=dataframe['Sex'].value_counts()


# Show counts
counts3=dataframe['PClass'].value_counts()

# Show number of unique values
unique2=dataframe['PClass'].nunique(12)

# Attempt to replace values with NaN
replace3=dataframe['Sex'].replace('male', np.nan)



## Select missing values, show two rows
missing=dataframe[dataframe['Age'].isnull()].head()


# Load data, set missing values
dataframe = pd.read_csv(url, na_values=[np.nan, 'NONE', -999])

# Delete a column
drop=dataframe.drop('Age', axis=1).head(12)

# Drop more columns
drop2=dataframe.drop(['Age', 'Sex'], axis=1).head(2)


# Drop a column if it has no name
drop3=dataframe.drop(dataframe.columns[2], axis=1).head(2)

# Delete rows, show first two rows of output
deletrow=dataframe[dataframe['Sex'] != 'male'].head(12)

# Delete row, show first two rows of output
deletrow2=dataframe[dataframe['Name'] != 'Allison, Miss Helen Loraine'].head(12)

# Delete row, show first two rows of output
deletrow3=dataframe[dataframe.index != 3].head(5)

# Drop duplicates, show first 12 rows of output
drop4=dataframe.drop_duplicates().head(12)


# Show number of rows dropped (there is no duplicate row)
#print("Number Of Rows In The Original DataFrame:", len(dataframe))
#print("Number Of Rows After Deduping:", len(dataframe.drop_duplicates()))

# Drop duplicates (only two rows left)
drop5=dataframe.drop_duplicates(subset=['Sex']).head(12)

# Drop duplicates but keep last
drop6=dataframe.drop_duplicates(subset=['Sex'], keep='last')

# Group rows by the values of the column 'Sex', calculate mean
# of each group
group=dataframe.groupby('Sex').mean()


# Group rows by sex
group2=dataframe.groupby('Sex')

# Group rows, count rows
group3=dataframe.groupby('Survived')['Name'].count()

# Group rows, calculate mean
group4=dataframe.groupby(['Sex','Survived'])['Age'].mean()

