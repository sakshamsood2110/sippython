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
dict1 = {1:'Ramesh', 2:'Suesh', 3:'Priyanka'}
dict1
type(dict1)

#%%
#Set - ordered collection of simple items, immutable
set1 = (['India', 'Pakistan', 'England', 'Australia'])
set1
type(set1)

#%%
#Strings

str1 = 'Python Programming'
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