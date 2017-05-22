#Numpy is the fundamental package for scientific computation in python. It adds support for large, multi-dimensional
#arrays and matrices, along with large collection of high-level mathematical functions to operate on these arrays.
#The program contains some fundamental implementation of numpy packages.

#Convention for numpy use 
import numpy as np

#creating an array 
my_array=np.array([0,1,2,3])

#obtaining information about a numpy array 
print("",my_array.dtype) 
print("",len(my_array))

#Changing the data type of an array to string
str_array=my_array.astype(str)

#printing array elements of my_array and str_array

for i in my_array:
    print(i*4)

for i in str_array:
    print(i*4)


##This was just a python list. Numpy is more useful for multi-dimensional arrays

dim2_array =np.array([[0,1,2,3],[0,1,2,3],[0,1,2,4]])

print(dim2_array.ndim)
print(dim2_array.shape)
print(dim2_array.size)

#Performing some math on array, we can do on whole list or line by line
print(np.mean(dim2_array))
print(np.mean(dim2_array, axis=0))
print(np.mean(dim2_array, axis=1))

#Indexing of numpy array 
print(dim2_array[:])
print(dim2_array[:2])
print(dim2_array[:2,:])
print(dim2_array[:2,:2])
print(dim2_array[0][::-1])

#Adding a more complex array 
dim2_array = np.array([[0.002002020203020,1,2.83893289239832,3.3243283293], [0.32323222,10000000000000,2,3], [0,1,2,300000000000000000000]])

#using numpy ability to save array as a csv file 
np.savetxt('lookatarray.csv', dim2_array)
np.genfromtxt('lookatarray.csv')

#Nas and NANs often used when there is missing data 
arr=np.array([0,7,1,8,np.nan])
print(np.mean(arr))

#You have to make it into masked array in order to do math with nans
arr2=np.ma.masked_array(arr,np.isnan(arr))
print(np.mean(arr2))



