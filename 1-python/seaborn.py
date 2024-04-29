# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 08:30:12 2024

@author: gaikw
"""

import seaborn as sns
import pandas as pd
sales=pd.read_excel('sales.xlsx')
cars=pd.read_csv("Cars.csv")
cars.head()
cars.columns
sns.relplot(x='HP',y='MPG',data=cars)
sns.relplot(x='Sales',y='Profit',data=sales)
sns.relplot(x='HP',y='MPG',data=cars,kind='line')
#boxplot
sns.catplot(x='HP',y='MPG',data=cars,kind='box')
#histogram
sns.distplot(cars.HP)

cars1=cars.describe()
sns.catplot(x='HP',y='MPG',data=cars1,kind='box')
sns.relplot(x='VOL',y='MPG',data=cars1,kind='line')

import matplotlib.pyplot as plt
numeric_cars = cars.select_dtypes(include=['int', 'float'])

# Create a boxplot for each column
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
sns.boxplot(data=numeric_cars)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

plt.boxplot(cars.MPG)
sns.distplot(cars.VOL)
plt.boxplot(cars.VOL)
