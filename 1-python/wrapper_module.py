# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:28:16 2024

@author: gaikw
"""
from wrapper import time_it
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