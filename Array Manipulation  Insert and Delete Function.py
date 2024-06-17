#Array Manipulation | Insert and Delete Function

import numpy as np

#help(np.insert)

a = np.array([[1, 1], [2, 2], [3, 3]])
#print(a)
#print(np.insert(a,1,5))


x = np.arange(8).reshape(2, 4)
#print(x)
idx = (1, 3)
#print(np.insert(x, idx, 999, axis=1))

a=np.arange(1,11)
#print(a)
#print(np.insert(a,1,50))
#print(a)
#print(np.insert(a,1,50.5))
#print(np.insert(a,(1,3,7),55))

a=np.array([[1,2],[3,4]])
#print(a)
#print(np.insert(a,1,23))
#print(np.insert(a,1,23,axis=0))
#print(np.insert(a,1,23,axis=1))
#print(np.insert(a,1,[40,50],axis=1))
#print(np.insert(a,1,[40,50,60],axis=0))
#ValueError: could not broadcast input array from shape (1,3) into shape (1,2)


#help(np.append)
a=np.arange(1,11)
#print(np.append(a,3452))
a=np.array([[1,2],[3,4]])
#print(np.append(a,[[40,50]]))
#print(np.append(a,[[40,50]],axis=0))
#print(np.append(a,[[40,50]],axis=1))
#ValueError: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size
#print(np.append(a,[[40],[50]],axis=1))

#delete()
#help(np.delete)

a=np.arange(1,11)
print(a)
print(np.delete(a,2))
print(a)
a=np.array([[1,2],[3,4]])
print(a)
print(np.delete(a,2))
print(np.delete(a,1,axis=0))
print(np.delete(a,1,axis=1))


