#Slicing Operation in NumPy Array

import numpy as np

a=np.array([1,2,3,4,5,6,7])
print(a[2:5:1])
print(a[:])
print(a[2::2])

x=np.array([[1,2],[3,4],[5,6]])
print(x[1:,1:])
print(x[-2:,-1:])
print(x[:,:])

b=np.array([[1,2,3,4],[5,6,7,8],[20,30,40,50]])
print(b)
print(b[1:,1:])
print(b[::,::2])

d=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
            [[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
print(d)

print(d[:,:,0:1])

print(d[:,1:,::2])
