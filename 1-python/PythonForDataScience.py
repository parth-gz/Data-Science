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

#Delete 
#del statement appears to have problems with duplicate indexes
s=pd.Series([2,3,4],index=[1,2,2])
del s[1]
s
del s[2]
s
###############################################################################
import pandas as pd
songs_66=pd.Series([3.0,None,12.0,4.0],index=['george','ringo','john','paul'],name='counts')
songs_66.dtypes
#dtype=('float64')
pd.to_numeric(songs_66.apply(str))
#there will be error
pd.to_numeric(songs_66.astype(str),errors='coerce')
songs_66.dtypes

#dealing with none
#the fillna() method will replace them with a given value
songs_66=pd.Series([3.0,None,12.0,4.0],index=['george','ringo','john','paul'],name='counts')
songs_66.dtypes
songs_66.fillna(-1)
songs_66=songs_66.astype(int)
songs_66.dtypes

#drop null values
songs_66=songs_66.dropna()
songs_66

##################################################################################
#append,combine 2 series
songs_69=pd.Series([7,6,32,45],index=['Ram','Sham','Ghanshyam','Krishna'],name='counts')
songs=pd.concat([songs_66,songs_69])
songs

##################################################################################

#plotting series
import matplotlib.pyplot as plt
fig=plt.Figure()
songs.plot()
plt.legend()

fig=plt.Figure()
songs.plot(kind='bar')
plt.legend()

##################################################################################

import numpy as np
data=pd.Series(np.random.randn(500),name='500_random')
fig=plt.Figure()
ax=fig.add_subplot(111)
data.hist()

##################################################################################
#Creating pandas dataframe
#create using lists
import pandas as pd
tech=[['Spark',200000,'30days'],['pandas',20000,'40days']]
df=pd.DataFrame(tech)
print(df)

##################################################################################

column_names=['courses','fee','duration']
row_label=['a','b']
df=pd.DataFrame(tech,columns=column_names,index=row_label)
print(df)

import pandas as pd
tech={'courses':"Spark PySpark Hadoop Python Pandas Oracle Java".split(" "),'Fee':[20000,25000,36000,22000,24000,21000,22000],'Duration':"30days,40days,35days,40days,60days,50days,55days".split(','),'Discount':[11.8,23.7,21.4,15.7,13.5,12.5,25.4,]}
df=pd.DataFrame(tech)
print(df)
print(df.dtypes)
df2=df.convert_dtypes()
print(df2.dtypes)
df=df.astype(str)
df=df.astype({'Fee':int,'Discount':float})

#convert datatype of all columns
tech={'courses':"Spark PySpark Hadoop Python Pandas Oracle Java".split(" "),'Fee':[20000,25000,36000,22000,24000,21000,22000],'Duration':"30days,40days,35days,40days,60days,50days,55days".split(','),'Discount':[11.8,23.7,21.4,15.7,13.5,12.5,25.4,]}
df=pd.DataFrame(tech)
cols=['Fee','Discount']
df[cols]=df[cols].astype('float')
df.dtypes

#ignores error
df=df.astype({'Fee':int,'courses':int},errors='ignore')
df.dtypes

#converts feed columns to numeric type
df=df.astype(str)
print(df.dtypes)
df['Fee']=pd.to_numeric(df['Fee'])
df.dtypes
df['Fee']=pd.to_numeric(df['Discount'])
df.dtypes

##################################################################################
#convert dataframe to csv
df.to_csv("file1.csv")

df=pd.read_csv('file1.csv')
print(df)

import pandas as pd
import numpy as np
tech={'courses':"Spark PySpark Hadoop  Python Pandas Oracle Java".split(" "),'Fee':[20000,25000,36000,np.nan,22000,24000,21000,22000],'Duration':"30days,40days,35days,,40days,60days,50days,55days".split(','),'Discount':[11.8,23.7,21.4,None,15.7,13.5,12.5,25.4,]}
row_labels="r0 r1 r2 r3 r4 r5 r6 r7".split(" ")

df=pd.DataFrame(tech,index=row_labels,columns=['Courses','Fee','Duration','Discount'])

##################################################################################

df.shape
df.size
df.columns
df.columns.values
df.index
df.dtypes
df.info
##################################################################################
#Accessing one column
df['courses']
#Accessing multiple columns
cols=['courses','Fee']
df[cols]
#accessing rows
df[5:7]   #dataframe[starting row index:end row index, starting col index:end col index]
df[::-1]
df[6:]
df[:6]
df[1:5,0:]
#Access certain rows from a column
df['Duration'][:4]
#subtracting specific value from a column
df['Fee']-=500
df['Fee']
df.astype({'Fee':int})
#describe a dataframe
#describe a dataframe for all numeric columns
df.describe()
######################################################################
#rename
df=pd.DataFrame(tech,index=row_labels)
df.columns='A B C D'.split(' ')
df
#rename using rename() method
df2=df.rename({'A':'a1','B':'b1'},axis=1)  #axis=0 for rows and 1 for columns
df2=df.rename({'A':'c1','B':'c2'},axis='columns')
df2=df.rename(columns={'A':'a2','B':'b2'})
df2=df.rename({'r1':'Row1','r2':'Row2'},axis=0)
df2=df.rename({'r1':'row1','r2':'row2'},axis='rows')
df2=df.rename(index={'r3':'Row3','r4':'Row4'})
df2

######################################################################
#Drop dataframe rows and columns
df=pd.DataFrame(tech,index=row_labels)
#drop rows by labels
df1=df.drop(['r1','r2'])
df1
#drop by position/index
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,4]])
df1
#delete rows by index range
df1=df.drop(df.index[2:])
df1
#when you have default indexes for rows
df=pd.DataFrame(tech)
df1=df.drop(0)
df1
#delete multiple rows
df1=df.drop([1,4],axis=0)
df1
df1=df.drop(range(0,4))
df1
