#Series:
'''Similar to lists in python
The series object also has a few more bits of data including an index and a name'''
import pandas as pd
songs=pd.Series([145,34,234,32],name='counts')
songs.index

#the index can be string based as well
songs2=pd.Series([145,34,234,32],name='counts',index=['paul','john','george','ringo'])

#NaN value
#Not a Number
f1=pd.read_csv('age.csv')
f1

###############################################################################

#the series object behaves similarly to a Numpy array
import numpy as np
numpy_ser=np.array([145,34,234,32])
songs[1]
numpy_ser[1]


songs.mean()
numpy_ser.mean()

###############################################################################

#The Pandas series data structure provides support for basic CRUD(create, read, update, delete)
george=pd.Series([10,5,3,11],index=['1968','1969','1970','1970'],name='george_songs')
george

#reading data from series
george['1969']
george['1970']
print(type(george)) #type=series
#series can be iterated too
for item in george:
    print(item)
    
george['1970']=69
george