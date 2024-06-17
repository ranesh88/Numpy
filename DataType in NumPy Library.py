# DataType in NumPy Library

import numpy as np

a = np.zeros(5)
print(a.dtype)

b=np.zeros(6,dtype=np.int8)
print(b.dtype)

x=np.float32(1)
print(x.dtype)

a=np.array([1,2,3],dtype='f')
print(a.dtype)

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

print(np.float64(newarr))