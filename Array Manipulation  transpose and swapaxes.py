# Array Manipulation | transpose and swapaxes

import numpy as np

#help(np.transpose)

a = np.array([[1, 2], [3, 4]])
#print(a)
#print(np.transpose(a))
#print(a.T)
#print(np.transpose(a,axes=(1,0)))
#print(np.transpose(a,axes=(0,1)))

b = np.array([1, 2, 3, 4])
#print(b)
#print(np.transpose(b))

c = np.arange(1,11).reshape(5,2)
#print(c)
#print(c.shape)
#print(np.transpose(c))
#rint(np.transpose(c).shape)

#3D Array
x=np.arange(1,25).reshape(2,3,4)
#print(x)
#print(x.shape)
#print(np.transpose(x))
#print(np.transpose(x).shape)

m=np.arange(1,25).reshape(2,3,4)
#print(m)
#print(m.shape)
#print(np.transpose(m,(1,2,0)))
#print(m.transpose())



#swapaxes
a=np.array([[1,2],[3,4]])
#print(a)
#print(np.swapaxes(a,0,1))

b=np.array([[1,2,3]])
#print(b)
#print(b.shape)
#print(np.swapaxes(b,0,1))
#print(np.swapaxes(b,1,0))

c=np.arange(1,25).reshape(2,3,4)
#print(c)
#print(c.shape)
#print(np.swapaxes(c,1,2))
#print(np.swapaxes(c,1,2).shape)
print(c.swapaxes(1,2))