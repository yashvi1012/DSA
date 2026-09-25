#1.array() function
from numpy import *
a=array([1,2,3,4])
print(a)

a=array([[1,2,3,4],[5,6,7,8]])
print(a)

#2.ones() and zeros() function
#ones()
#1D array
a=ones(5,int)
print(a)

#2D array
a=ones((3,4),float)
print(a)

#zeros()
#1D array
a=zeros(5,int)
print(a)

#2D array
a=zeros((3,4),float)
print(a)

#3.eye() function
a=eye(2)
print(a)

a=eye(3)
print(a)

a=eye(4)
print(a)

#4.reshape() function
a=array([1,2,3,4,5,6])
print(a)
b=reshape(a,(2,3))
print(b)

a=array([0,1,2,3,4,5,6,7,8,9,10,11])
print(a)
b=reshape(a,(2,3,2))
print(b)

a=array([0,1,2,3,4,5,6,7,8,9,10,11])
print(a)
b=reshape(a,(3,2,2))
print(b)

