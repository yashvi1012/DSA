#single dimensional
from numpy import *
arr1=array([1,2,3,4,5])
print(arr1)

#two dimensional
from numpy import *
arr2=array([[1,2,3],[4,5,6]])
print(arr2)

#three dimensional
from numpy import *
arr3=array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3)

#ndim attribute
arr1=array([1,2,3,4,5])
print(arr1.ndim)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.ndim)

arr3=array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr3.ndim)


#shape attribute
arr1=array([1,2,3,4,5])
print(arr1.shape)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.shape)

arr3=array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr3.shape)


#size attribute
arr1=array([1,2,3,4,5])
print(arr1.size)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.size)

arr3=array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr3.size)

#itemsize attribute
arr1=array([1,2,3,4,5])
print(arr1.itemsize)

arr2=array([[1.1,2.2,3.3],[4.4,5.5,6.6]])
print(arr2.itemsize)

#dtype attribute
arr1=array([1,2,3,4,5])
print(arr1.dtype)

arr2=array([[1.1,2.2,3.3],[4.4,5.5,6.6]])
print(arr2.dtype)

#nbytes attributes
arr1=array([1,2,3,4,5])
print(arr1.nbytes)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.nbytes)

