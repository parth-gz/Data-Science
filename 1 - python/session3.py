# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:35:35 2024

@author: parth
"""

#Reading files in various formats

import pandas as pd
f1=pd.read_csv('buzzers.csv')
#import os 
with open('buzzers.csv') as raw_data:
    print(raw_data.read())
    
###############################################################################
#read csv data in the form of list

import csv
with open('buzzers.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)
        
#read csv data in the form of dictionary

import csv
with open('buzzers1.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
        
###############################################################################

with open('buzzers1.csv') as raw:
    dictionary={}
    for line in raw:
        key,value=line.split(',')
        dictionary[key]=value
dictionary

###############################################################################
#Decorators
'''A python decorator is a function that takes a function as an argument and returns 
it by adding some functionality'''
#function within a function

def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(number)
    return result
print(f"4+1={plus_one(4)}")

###############################################################################
#Passing function as argument to another function
def plus_one(number):
    result1=number+1
    return result1
def function_call(function):
    result=function(3)
    return result
function_call(plus_one)

###############################################################################

#Function returning another function
def hello_function():
    def say_hi():
        return "hi"
    return say_hi
hello=hello_function()
hello()
'''when you call hello_function() directly, it will return an object, not 'hi'.
Thats why you need to assign it to hello first and then call hello() '''
###############################################################################

#Need for decorators
import time
lst=[1,2,3,4,5,6,7,8,9,10]
def cube(numbers):
    start=time.time()
    result=[]
    for num in numbers:
        result.append(num*num*num)
    end=time.time()
    totalTime=(end-start)*1000
    print(f"Total execution time= {totalTime}")
    return result
array=range(1,1000000)
ct=cube(array)
    
###############################################################################

def say_hi():
    return "Hello there"
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
decorate=uppercase_decorator(say_hi)
decorate()

@uppercase_decorator
def say_hi():
    return 'hello'
say_hi()

###############################################################################

#Applying multiple decorators
def split_string(function):
    def wrapper():
        func=function()
        splitted_string=func.split()
        return splitted_string
    return wrapper
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()


###############################################################################

import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        totalTime=(end-start)*1000
        print(func.__name__+f" took {totalTime} milliseconds")
        return result
    return wrapper
@time_it
def calc_square(numbers):
    result1=[]
    for num in numbers:
        result1.append(num*num)
        return result1
@time_it
def calc_cube(numbers):
    result1=[]
    for num in numbers:
        result1.append(num*num*num)
        return result1
    
lst=range(1,10000000000)
calc_square(lst)
calc_cube(lst)

###############################################################################

