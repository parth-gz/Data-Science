# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:54:09 2024

@author: gaikw
"""

gen =(x for x in range(3))
print(gen)
next(gen)
next(gen)
'''for i in range(0,10,2):
    yield i'''
    
###############################################################################

#Enumerate
lst=["apple","banana","cherry"]
for index,item in enumerate(lst,start=1):
    print(f'{index} {item}')
###############################################################################

#zip function

lst1=['abc','xyz','lmn']
lst2=[123,456,789]
for name,number in zip(lst1,lst2):
    print(name,number)


lst1=['abc','xyz','lmn']
lst2=[123,456,789,321]
for name,number in zip(lst1,lst2):
    print(name,number)
#won't display last data in lst2
#solution
import itertools as it
for name,number in it.zip_longest(lst1,lst2): #show 321 with None
    print(name,number)
#  
for name,number in it.zip_longest(lst1,lst2,fillvalue=0): #show 321 with None
    print(name,number)
    
###############################################################################

#all() function
lst=[1,-2,5,-3,4]
if all(lst):
    print('all values are true')
else:
    print('there are zero values')
#
lst=[1,-2,5,-3,0,4]
if all(lst):
    print('all values are true')
else:
    print('there are zero values')
    
###############################################################################

#any() function
lst=[0,0,0,3,0,0]
if any(lst):
    print('it has some non zero value')
else:
    print('useless')
#
lst=[0,0,0,0,0]
if any(lst):
    print('it has some non zero value')
else:
    print('useless')

###############################################################################

#count() function
import itertools as it
counter=it.count(start=1)  #start=1 (0 by defult)
print(next(counter))

###############################################################################

#cycle() function
import itertools as it
instructions=['eat','code','sleep']
for a in it.cycle(instructions):
    print(a)
    
###############################################################################

#reprat() function
import itertools as it
for msg in it.repeat("Jai Hind", times=5):
    print(msg)
    
###############################################################################
#permutations and combinations

import itertools as it
players=['John','Jani','janardhan','Jaikal']
for i in it.permutations(players,2):
    print(i)
#
import itertools as it
players=['John','Jani','janardhan','Jaikal']
for i in it.combinations(players,2):
    print(i)

###############################################################################

#product()

team1=['Bumrah','pandya','Shami']
team2=['Rohit','Kohli','Dhoni']
for pair in it.product(team1,team2):
    print(pair)
