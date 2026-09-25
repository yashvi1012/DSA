import numpy
a=numpy.array([1,2,3,4,5,6,7,8,9,10])
print(a)

#creating arrays using array()
from numpy import *
a=array([1,2,3,4,5],int)
print(a)

a=array([1.1,2.2,3.3,4.4,5.5],float)
print(a)

a=array(['a','b','c','d','e'])
print(a)

a=array(['yashvi','hemali','krisha','trisha','prisha'],dtype=str)
print(a)

#creating array using linspace
from numpy import *
a=linspace(1,5,5)
print(a)

a=linspace(0,10,5)
print(a)

#creating array using logspace
from numpy import *
a=logspace(1,5,5)
print(a)

#creating array using arange()
a=arange(1,10,3)
print(a)

a=arange(10)
print(a)

a=arange(5,10)
print(a)

#creating array using zeros() and ones()
a=zeros(5,int)
print(a)

a=ones(5,int)
print(a)
