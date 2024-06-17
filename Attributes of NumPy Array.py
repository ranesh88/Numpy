# Attributes of NumPy Array

import numpy as np

a=np.array([1.0,2.2,3,4,5])

print("Dimension of a =",a.ndim)
print("Shape of a =",a.shape)
print("Size of a =",a.size)
print("Datatype of a::",a.dtype)
print("Itemsize of a =",a.itemsize)

b=np.array([[1,2],[3,4]])

print("Dimension of b =",b.ndim)
print("Shape of b =",b.shape)
print("Size of b =",b.size)
print("Datatype of b::",b.dtype)
print("Itemsize of b =",b.itemsize)

c=np.array([[['a','b'],['c','d']],[['e','f'],['g','h']]])

print("Dimension of c =",c.ndim)
print("Shape of c =",c.shape)
print("Size of c =",c.size)
print("Datatype of c::",c.dtype)
print("Itemsize of c =",c.itemsize)