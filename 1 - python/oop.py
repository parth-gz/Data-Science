# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:17:07 2024

@author: gaikw
"""

class Human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    def do_work(self):
        if self.name=='Tom Cruise':
            print(self.name, "shoots movies")
        elif self.name=='Maria Sharapova':
            print(self.name,"plays tennis")
    def speaks(self):
        if self.name=='Tom Cruise':
            print("I am Ethan Hunt of mission Impossible")
        elif self.name=='Maria Sharapova':
            print("I have won 5 grand slams")
         
tc=Human('Tom Cruise','Shoots Movies')
ms=Human('Maria Sharapova','Plays Tennis')
tc.do_work()
tc.speaks()
ms.do_work()
ms.speaks()

###############################################################################
#Inheritance
#Hierarchical Inheritance
class Vehicle:
    def general_usage(self):
        print('General use: Transportation')
class Car(Vehicle):
    def __init__(self):
        print("I am a car.")
        self.wheel=4
        self.has_roof='Yes'
    def specific_usage(self):
        self.general_usage()
        print('Commute to work, vacation with family')
class Motorcycle(Vehicle):
    def __init__(self):
        print('I am a motorcycle.')
        self.wheel=2
        self.has_roof='No'
    def specific_usage(self):
        self.general_usage()
        print('local commutation, racing')
        
c=Car()
c.specific_usage()
m=Motorcycle()
m.specific_usage()

###############################################################################
#multiple inheritance
#one class derived from more than one base classes

class Father():
    def skills(self):
        print('I like gardening and Programming')
class Mother():
    def skills(self):
        print('I like cooking and art')
        
class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print('I like sports')
        
c=Child()
c.skills()