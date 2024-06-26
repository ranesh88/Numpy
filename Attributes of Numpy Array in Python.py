# Attributes of Numpy Array in Python

from numpy import *

a=array([101,102,103,104,105])
b=array([[10,20,30,40],
         [50,60,70,80]])

print(a)
print(b)
print()

#ndim Attribute
print("1D Array ndim::",a.ndim)
print("2D Array ndim::",b.ndim)
print()

#shape Attribute
#For 1D Array shape elements in the row
#For 2D Array shape specifies number of row and column in each row
print("1D Array shape::",a.shape)
print("2D Array shape::",b.shape)
print()

#size attribute
print("1D Array size::",a.size)
print("2D Array size::",b.size)
print()

#itemsize attribute
print("1D Array itemsize::",a.itemsize)
print("2D Array itemsize::",b.itemsize)
print()

#dtype attribute
print("1D Array dtype::",a.dtype)
print("2D Array dtype::",b.dtype)
print()

#nbytes attribute
print("1D Array nbytes::",a.nbytes)
print("2D Array nbytes::",b.nbytes)
print()



