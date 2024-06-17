# Advanced Indexing Operation in NumPy Arrays

import numpy as np

a=np.array([1,2,3,4,5,6,7,8,9,10])
print(a)
index=np.array([1,4,5])
print(a[index])
print(a[[1,4,5]])

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(b[[0,2],[2,0]])
print(b[[1,1,2],[0,2,1]])

#repeated accessing elements
x=np.array([1,2,3,4,5,6,7,8,9,10])
print(x[[1,4,1,4,1,4]])

#Boolean Indexing
m=np.array([[1,-2,3],[4,-2,3]])
print(m)
print(m[m<0])
print(m[m>0])

n=np.array([[1,-2,3],[10,-20,30],[3,4,-4]])
print(n)
print(n[n<0]*2)
