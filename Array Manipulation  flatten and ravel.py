                   #Array Manipulation | flatten and ravel

import numpy as np

b=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
#print(b)

#flatten()

#help(b.flatten)

#print(b.flatten())

#print(b.flatten(order='C'))

#print(b.flatten(order='F'))

#print(b.flatten(order='K'))

#print(b.flatten(order='A'))

a=np.array([[1,2],[3,4]])

#print(a)

#print(a.flatten())

#print(a.flatten(order='F'))


#ravel()

#help(np.ravel)

x = np.array([[1, 2, 3], [4, 5, 6]])
#print(x)
#print(np.ravel(x))
#print(np.ravel(x, order='F'))

a = np.arange(12).reshape(2,3,2)
#print(a)
#print(np.ravel(a))
#print(a.ravel(order='C'))
#print(a.ravel(order='K'))

c = np.arange(5)[::-1]
#print(c)
#print(c.ravel())
#print(c.ravel(order='F'))


b = np.array([[[1, 2, 3], [4, 5, 6]],[[6,7,8],[9,10,11]]])
print(b)
print(np.ravel(b))
print(np.ravel(b, order='F'))






