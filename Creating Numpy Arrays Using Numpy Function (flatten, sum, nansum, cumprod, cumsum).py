# Creating Numpy Arrays Using Numpy Function (flatten, sum, nansum, cumprod, cumsum

import numpy as np

#flatten()

n1=[2,4,6,8]
n2=[1,3,5,7]
n=np.array([n1,n2])
#print(n)
#print(n.flatten("C"))
#print(n.flatten("F"))

a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
n=np.array([a,b])
#print(n)
#print(n.flatten("C"))
#print(n.flatten("F"))

#sum()

n1=[2,4,6,8]
n2=[1,3,5,7]
n=np.array([n1,n2])
#print(n)
#print(n.sum(axis=0))
#print(n.sum(axis=1))

#2D Array
a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
n=np.array([a,b])
#print(n)
#print(n.sum(axis=0))
#print(n.sum(axis=1))

#nansum()

n1=[2,4,6,np.nan]
n2=[1,3,5,7]
n=np.array([n1,n2])
#print(n)
#print(np.nansum(n,axis=0))
#print(np.nansum(n,axis=1))

#2D Array
a=[[1,np.nan],[3,4]]
b=[[5,6],[np.nan,8]]
n=np.array([a,b])
print(n)
print(np.nansum(n,axis=0))
print(np.nansum(n,axis=1))







