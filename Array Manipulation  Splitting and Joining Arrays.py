# Array Manipulation | Splitting and Joining Arrays

import numpy as np

#help(np.concatenate)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
#print(a.shape)
#print(b.shape)
#print(np.concatenate((a, b), axis=0))
#print(np.concatenate((a, b), axis=1))
#print(np.concatenate((a,b.T),axis=1))


x=np.arange(6)
y=np.arange(5)
z=np.arange(4)
#print(np.concatenate((x,y,z)))

a=np.arange(1,5)
b=np.arange(6)
c=np.zeros(10)
#print(np.concatenate((a,b),out=c))
#print(np.concatenate((a,b),dtype=int))

p=np.arange(5)
q=np.array([[1,2],[3,4]])
#print(np.concatenate((p,q)))

#vstack()

#help(np.vstack)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
#print(np.vstack((a,b)))

x = np.array([[1], [2], [3]])
y = np.array([[4], [5], [6]])
#print(np.vstack((x,y)))

a=np.arange(6)
n=np.arange(5)
c=np.arange(6)
#print(np.vstack((a,n)))ValueError: all the input array dimensions except for the concatenation axis must match exactly,
                                   #but along dimension 1, the array

#print(np.vstack((a,c)))

p=np.array([[1,2],[3,4]])
q=np.array([[5,6]])
#print(np.vstack((p,q)))

#hstack
#help(np.hstack)

a = np.array((1,2,3))
b = np.array((4,5,6))
#print(np.hstack((a,b)))

a = np.array([[1],[2],[3]])
b = np.array([[4],[5],[6]])
#print(np.hstack((a,b)))

x=np.arange(6)
y=np.arange(6)
#print(np.hstack((x,y)))

p=np.array([[1,2],[3,4]])
q=np.array([[5,6]])
#print(np.hstack((p,q.T)))

#split()
#help(np.split)

x = np.arange(9)
#print(np.split(x, 3))
#print(np.split(x, 4))

x = np.arange(8.0)
#print(np.split(x, [3, 5, 6, 10]))

a=np.arange(1,10)
#print(np.split(a,3))

a=np.arange(1,17).reshape(8,2)
#print(a)
#print(np.split(a,4))
#print(np.vsplit(a,4))
#print(np.hsplit(a,2))

b=np.arange(1,13).reshape(2,6)
print(b)
#print(np.hsplit(b,3))
print(np.split(b,3,axis=1))






