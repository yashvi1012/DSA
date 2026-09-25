#1.import array
import array
a=array.array('i',[10,20,30,40,50])
for i in range(5):
    print(a[i])

#2.import array as ar
import array as ar
a=ar.array('i',[10,20,30,40,50])
for i in range(5):
    print(a[i])

#3.from array import *
from array import *
a=array('i',[10,20,30,40,50])
for i in range(5):
    print(a[i])

#4.append()
from array import *
a=array('i',[1,2,3,4,5,6,7,8,9,10])
a.append(11)
print(a)

#5.insert()
from array import *
a=array('i',[1,2,3,4,5,6,7,8,9,10])
a.insert(0,100)
print(a)

#6.pop()
from array import *
a=array('i',[1,2,3,4,5,6,7,8,9,10])
a.pop()
print(a)

#7.pop(0)
from array import *
a=array('i',[1,2,3,4,5,6,7,8,9,10])
a.pop(0)
print(a)

#8.remove(2)
from array import *
a=array('i',[1,2,3,4,5,6,7,8,9,10])
a.remove(2)
print(a)

#9.reverse()
from array import *
a=array('i',[1,2,3,4,5,6,7,8,9,10])
a.reverse()
print(a)

#10.count(2)
from array import *
a=array('i',[1,2,3,4,5,6,7,8,9,10])
a.count(2)
print(a)
