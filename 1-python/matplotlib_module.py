# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:53:47 2024

@author: gaikw
"""
import matplotlib.pyplot as plt
X=range(-25,26)
Y=[x**3 for x in X]
plt.plot(X, Y)
plt.show()

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("sample graph")
plt.show()

x1=[10,20,30]
y1=[20,40,10]
x2=[10,20,30]
y2=[40,10,30]
plt.plot(x1,y1,label='line1')
plt.plot(x2,y2,label='line2')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

################################################################################
#Markers
X=[1,4,5,6,7]
Y=[2,6,3,6,3]
#plotting the points
plt.plot(X,Y,color='red', linestyle='dashdot', linewidth=3,marker='o',markerfacecolor='blue',markersize=12)
plt.ylim(1,8)
plt.xlim(1,8)
###############################################################################
'''Write a python program to to display a bar chart of popularity of programming languages'''
import matplotlib.pyplot as plt
x=['python','Javascript','Java','PHP','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of programming languages\n"+"Worldwide, oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
#Turn on the grids
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

#Horizontal bar graph
import matplotlib.pyplot as plt
x=['python','Javascript','Java','PHP','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
plt.barh(x_pos,popularity,color='red') #changed bar to barh
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of programming languages\n"+"Worldwide, oct 2017 compared to a year ago")
plt.yticks(x_pos,x) #Changed xticks to yticks
#Turn on the grids
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

#multicolored bars
plt.bar(x_pos,popularity,color='red blue green black cyan yellow'.split(" "))

#############################################################################
#Histogram
import matplotlib.pyplot as plt
blood_sugar=[118,120,134,102,145,123,111,130,145,102,100,80,69,90]
plt.hist(blood_sugar,rwidth=0.5,bins=4)

'''Histogram showing normal, pre-diabetic and diabetic patients distribution
80-100: normal
100-125: pre diabetic
125 onwards: diabetic'''
plt.xlabel("Sugar level")
plt.ylabel("Number of patients")
plt.title("blood sugar charts")
plt.hist(blood_sugar,bins=[80,100,125,150],rwidth=0.95,color='red')

#Boxplot
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(20)
data=np.random.normal(100,20,200)
fig=plt.figure(figsize=(10,7))
plt.boxplot(data)
plt.show()

data1=np.random.normal(100,10,200)
data2=np.random.normal(90,20,200)
data3=np.random.normal(80,30,200)
data4=np.random.normal(70,40,200)
data=[data1,data2,data3,data4]
fig=plt.figure(figsize=(10,7))
ax=fig.add_axes([0,0,1,1])
bp=ax.boxplot(data)










