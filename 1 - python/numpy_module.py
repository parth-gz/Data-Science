#Array in Numpy
#Create ndarray
import numpy as np
arr=np.array([10,20,30])
print(arr)

#Create multidimentional array
arr=np.array([[10,20,30],[40,50,60]])
print(arr)

#use ndmin param to specify how many minimum dimensions you 
#wanted to create an array with minimum  dimension
arr=np.array([10,20,30,40],ndmin=3)
print(arr)

#change the datatype
# dtype parameter
arr=np.array([10,20,30],dtype=complex)
print(arr)

#Get dimension of array
arr=np.array([[10,20,30],[40,50,60],[15,26,37]],ndmin=3)
print(arr.ndmin)
print(arr)

#Get datatype of array
arr=np.array([10,20,30])
print(arr.dtype)

#Get shape and size of array

arr=np.array([[10,20,30],[40,50,60]])
print(arr.size)   #Gives number of elements
print(arr.shape)

#Convert int to float
arr=np.array([[10,20,30],[40,50,60]],dtype="float")
print(arr)

#Create Sequence of integers using arrange()
#from 0 to 20 with step 3
arr=np.arange(0,20,3)
print(arr)

#Access single element using index
arr=np.arange(11)
print(arr)
print(arr[2])
print(arr[-2])

#Access elements of multidimensional array
arr=np.array([[10,20,30,90,80],[40,50,30,50,60]])
print(arr[1,2])
print(arr[0,0])
print(arr[-1,-3])
print(arr[1,-1])  

#Access array elements using slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]
print(x)

x=arr[-2:3:-1]
print(x)

####################################################################################
#Integer array indexing
import numpy as np
arr=np.arange(35).reshape(5,7)
print(arr)

#Boolean array indexing
arr=np.arange(12).reshape(3,4)
arr
rows=np.array([False,True,True])  #0th row not included
wanted_rows=arr[rows,:]
wanted_rows

cols=np.array([False,True,False,True]) #0th and 2nd cols not included
wanted_cols=arr[:,cols]
wanted_cols

#convert array
array=np.array(list)
print(array)

#ndarray shape
#Shape
arr=np.array([[1,2,3],[5,5,7]])
print(arr.shape)

#Resize the array
arr.shape=(3,2)
print(arr)
arr.reshape(3,2)

#Arithmetic operations
arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,2,3,4])

#add array
addition=np.add(arr1,arr2)
addition
#subtract arr
sub=np.subtract(arr1,arr2)
sub
#np.multiply, np.division, np.reciprocal
################################################################################
#Power
pow=np.power(arr1,3)
pow

arr1=np.array([1,2,3])
arr2=np.array([3,2,1])
pow1=np.power(arr1,arr2)
pow1

#Mod function
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([3,2,1])
arr1.dtype
mod_arr=np.mod(arr1,arr2)
mod_arr

###############################################################################
#create zero array
from numpy import zeros
a=zeros([3,4])
print(a)

from numpy import ones
b=ones(5)
print(b)

#Create array with vstack(vertical stack)
import numpy as np
a1=np.array([1,2,3])
a2=np.array([3,4,5])
a3=np.vstack((a1,a2))
print(a3)

#hstack
a4=np.hstack((a1,a2))
print(a4)

#index row in 2D array
import numpy as np
data=np.array([[1,2,3],[3,4,5],[5,6,7]])
print(data[0,])
print(data[-2,])

x,y=data[:,:-1], data[:,-1]
x
y

##############################################################################3
#Broadcast a scalar to 1D array
import numpy as np
a=np.array([1,2,3])
b=4
c=a+b
print(c)

################################################################################
#L1 Norm
'''Vector L1 norm
The L1 norm is calculated as the sum of the absolute vector values,
where the absolute value of the scalar uses the notation |a1|
In effect, the norm is the calculation of Manhattan distance from the origin of vector space 
||v||1=|a1|+|a2|+|a3|'''
import numpy as np
a=np.array([1,2,3])
l1=np.linalg.norm(a,1)
print(l1)

#L2 norm
'''Take the square root of the sum of squares of the vector values
eg. a=[1,2,3]
norm=√(1+4+9)'''
a=np.array([4,5,6])
l2=np.linalg.norm(a)
print(l2)

#Inner product and outer product of matrices
#if u and v are column matrices of any size, transpose(u).v is called inner product
#u.transpose(v) is called outer product

#Triangular matrices
m=np.array([[1,2,3],[3,4,5],[5,6,7]])
upper=np.triu(m)
lower=np.tril(m)
print("Upper Triangular Matrix:")
print(upper)
print("Lower Triangular Matrix:")
print(lower)
#Diagonal matrix
d=np.diag(m)
print(d)
D=np.diag(d)
print(D)
#Identity Matrix
I=np.identity(3)
print(I)

#Orthogonal Matrix
import numpy as np
q=np.array([[1,0],[0,-1]])
print(q)
#inverse equivalence
v=np.linalg.inv(q)
print(v)
#Identity equivalence
I=q.dot(q.T)
print(I)
##############################################################################
#Transpose of a matrix
import numpy as np
m=np.array([[1,2,3],[3,4,5],[5,6,7]])
C=m.T
C
##############################################################################
#Inverse matrix
import numpy as np
m=np.array([[1,2,3],[3,4,5],[5,6,7]])
a=np.array([[1,2],[3,4]])
n=np.linalg.inv(a)
n
I=a.dot(n)
I

