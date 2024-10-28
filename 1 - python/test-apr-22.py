# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 12:51:48 2024

@author: gaikw
"""
#Python function that takes two lists and returns true if they have at least one value in common
flag=0
def func(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                flag=1
    if flag==1:
        return True
print(func([1,2,3],[4,3,5,6]))

#Use list comprehension to construct a new list but add 6 to each item.
lt=[x+6 for x in range(10)]
print(lt)

#Write a Python program to reverse a string
s=input("Enter string:")
s1=s[::-1]
print(s1)

#Write a Python program to iterate over dictionaries using for loops.
d={1:2,2:3,3:4,4:5}
for i in d.keys():
    print(f"{i}:{d[i]}")
    
'''Using dict comprehension and a conditional argument create a dictionary from the current dictionary
where only the key:value pairs with value above 2000 are taken to the new dictionary.'''
d={1:2,2:3000,3:400,4:5000}
d1={x: d[x] for x in d.keys() if d[x]>2000}
print(d1)

'''Open the file data.txt using file operations'''
import pandas as pd
data=pd.read_csv("data.txt")
print(data)

'''Define a array ,data = array([11, 22, 33, 44, 55]) find 0 th index 4 th index data'''
import numpy as np
data = np.array([11, 22, 33, 44, 55])
print(data[0],data[4])

'''Write a Python program to filter a list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list=[x for x in lst if x%2==0]
even_list
odd_list=[x for x in lst if x%2==1]
odd_list

'''Write a Pandas program to create the specified columns and rows from a given data frame.
name': ['Anna', 'Dinu', Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', ‘venkat', 'Ajay', 'Dhanesh']
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
'''
import pandas as pd
import numpy as np
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
student={'name': ['Anna', 'Dinu', 'Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', 'venkat', 'Ajay', 'Dhanesh'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df=pd.DataFrame(student,index=labels)
df

'''Define a array data = array([11, 22, 33, 44, 55]) and slice it from 1 to 4'''
import numpy as np
data = np.array([11, 22, 33, 44, 55])
print(data[1:4])
