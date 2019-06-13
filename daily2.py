# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:53:11 2019

@author: Saksham
"""

list1 = [1,2,3,4,5]
list1
type(list1)



list2 = ['a','c','d','e']

#%%
#tuple - multiple type of objects, immutable
tuple1 = (1,2,'a','b')
tuple1
type(tuple1)

#%%
#Dictionary - key-value pairs
dict1 = {1:'Saksham', 2:'Shashiraj', 3:'Deepesh'}
dict1
type(dict1)

#%%
#Set - ordered collection of simple items, immutable
set1 = (['India', 'Nepal', 'Afghanistan', 'Australia'])
set1
type(set1)

#%%
#Strings

str1 = 'Python coding with Spyder IDE'
type(str1)

#%%
#sequence - tuple and list are used
list1
for i in list1:
    print(i)
tuple1
for i in tuple1:
    print(i)
for i in range(1,10,2):
    print(i, end=' ')
    
    #%%
#frozen set- accepts iterable object as input parameter.
tupleFZ1 = (9,8,7,6,5,4,3,2,1) 
type(tupleFZ1)  

# converting tuple to frozenset 
frozenset1 = frozenset(tupleFZ1) 
frozenset1
type(frozenset1)

dict1
frozenset2 = frozenset(dict1)
type(frozenset2)
frozenset2
#keys of dictionary made as frozen set

#%%
#zip - map the similar index of multiple containers 
# initializing lists 
name = [ "Priya", "Harsh", "Hunny", "Akshay" ] 
rollno = [ 6, 7, 8, 3] 
marks = [ 80, 55, 66, 78 ] 
# using zip() to map values 
mapped = zip(name, rollno, marks) 
# converting values to print as set 
mapped = set(mapped) 
mapped
namez, rollnoz, marksz = zip(*mapped)
namez


#%%
#numpy - array - same data type
import numpy as np
np1 = np.arange(1,20)
np1
type(np1)
np
np2 = np.array([ 80, 95, 55, 75 ])
np2
np.sort(np2)
type(np2)
np3 = np.array([[2,6],[5,1]])
np3
np3.shape
type(np3)

#%%
#pandas - dataframe, excel like
#https://mode.com/python-tutorial/pandas-dataframe/
import pandas as pd
pd
df1 = pd.DataFrame({'rollno':[1,2,3,4], 'name': [ "Priya", "Harsh", "Hunny", "Akshay" ], 'marks':[ 85, 65, 70, 90 ], 'gender':['F','M','M','M']})
df1
type(df1) 

df1.columns
df1.describe
df1.dtypes
df1.shape
df1.groupby('gender').size()
df1.groupby('gender')['marks'].mean()
df1.groupby('gender').aggregate({'marks': [np.mean, 'max']})

#%%
#Graphs https://python-graph-gallery.com/
import matplotlib.pyplot as plt
#https://matplotlib.org/
df1.groupby('gender').size().plot(kind='bar')

#https://seaborn.pydata.org/index.html
import seaborn as sns
# sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
sns.pairplot(iris)


#%%
#Load Inbuilt Datasets
import statsmodels.api as sm
#https://vincentarelbundock.github.io/Rdatasets/datasets.html
mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
mtcars.data.head()

#%%
#Load from Excel/ CSV and export to
data = mtcars.data
data.head()

data.to_csv('exportcsv1.csv')
data.to_excel('exportexcel1.xlsx','sheet1', header=False)

#load from CSV and Excel
data2a = pd.read_csv('exportcsv1.csv')
data2a.head()

data2b = pd.read_excel('exportexcel1.xlsx','sheet1')
data2b.head()
