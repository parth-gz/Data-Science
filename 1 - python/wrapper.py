# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:58:39 2024

@author: gaikw
"""

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