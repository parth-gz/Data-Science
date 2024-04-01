# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:26:10 2024

@author: parth
"""
#list Comprehension

lst=[num for num in range (0,20)]
print(lst)

#####################

names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)
 
#list comprehesion with if statement\

def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)        

lst=[f"{x}{y}"for x in range (3)for y in range(3)]
print(lst)

#############################################
#Dictionary Comprehension
dict={x:x*x for x in range(3)}
print(dict)


###############################################
#Generator

gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)

gen=(x for x in range(3))
next(gen)
next(gen) #it gives step by step value

###############################
#Function which returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
    
gen=range_even(6) #instead of using for loop we can write our own generator
next(gen)
next(gen)

#########################################
#Chainning Generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
    
'''ele appears to be a placeholder for an element from
an iterable .the asterisk(*) is likely just a character
used to represent a placeholder or a wildcard.
for instance ,if you are iterating over a list of elements
,"ele*" could symbolize any element in that list .its a
generic representation that doesn't correspond to any
specific syntax in python or itertools
'''
  
password=["not-good","give'm-mass","0010=123"]
for password in hide(lengths(password)):
    print(password)
    
    
import string
adjectives=input("Enter the Adjective :")
nouns=input("Enter the Noun :")
#pick the words
import random
number=random.randrange(0,100)
#select a special character
special=random.choice(string.punctuation)
#create the password
password=adjectives+nouns+str(number)+special
print('Your new password is : %s'%password)
for password in hide(lengths(password)):
    print(password,end=" ")

###############################################################################


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

#repeat() function
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

gen=(x for x in range(8))
for num in gen:
    print(num)
    
###############################################################################
import copy as cp
lst=[1,2,3]
lst1=cp.copy(lst)
lst[0]=100
lst
lst1

#shallow copy on two levels
lst=[[1,2,3],[4,5,6]]
lst1=cp.copy(lst)
lst[1][1]=200
lst
lst1

###############################################################################
#deep copy

import copy as cp
lst=[[1,2,3],[4,5,6]]
lst1=cp.deepcopy(lst)
#does not affect the other
lst[0][0]=100
lst
lst1