# Array Manipulation | reshape and resize

import numpy as np

#reshape () fuction
x=np.arange(10)
print(x.shape)

y=np.reshape(x,(2,5))
print(y)
print(y.shape)


a = np.arange(6).reshape((3, 2))
print(a)

print(np.reshape(a, (2, 3)))

m = np.array([[1,2,3], [4,5,6]])
print(m)
print(np.reshape(m, 6))


p=np.arange(10)
print(p)
q=np.reshape(p,(5,2))
print(q)
print(q.shape)
r=np.reshape(p,(5,2),order='F')
print(r)
print(p.size)
print(q.size)

#z=np.reshape(p,(4,3))
#print(z) ValueError: cannot reshape array of size 10 into shape (4,3)

a=np.arange(20)
print(a.reshape((4,5)))

#resize() function
a=np.arange(10)
print(a)
print(np.resize(a,(2,5)))

b=np.arange(6)
print(b)
print(np.resize(b,(5,2)))
print(b.resize((5,2)))
print(b)


