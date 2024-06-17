# Creating Numpy Arrays Using (power, diff, cross, and sort)

import numpy as np

#power()

a=np.array([1,2,3,4])
b=np.array([[[1,2],[3,4]],[[4,5],[6,7]]])
p1=np.power(a,[2])
p2=np.power(b,[3])
p3=np.power(a,[2,3,4,5])
#print(a)
#print(b)
#print(p1)
#print(p2)
#print(p3)

#Diff

a1=np.array([1,5,8,3])
a2=np.array([[2,7],[3,5]])
a3=np.array([4,5,6,8])
#print(a1)
#print(a2)
d1=np.diff(a1)
#print(d1)
d2=np.diff(a2)
#print(d2)
d3=np.diff((a1,a3),axis=0)
#print(d3)
d4=np.diff((a1,a3),axis=1)
#print(d4)

#cross()
a1=np.array([1,5])
a2=np.array([2,8])
c=np.cross(a1,a2)
#print(a1)
#print(a2)
#print(c)
# declare vectors
x = [[1, 2], [3, 4]]
y = [[5, 6], [7, 8]]

# find cross product of
# two given vectors
result = np.cross(x, y)

# show the result
#print(result)

#sort()
a1=np.array([10,14,28,2])
a2=np.array([20,7,9,5])
print(a1)
print(a2)

s1=np.sort((a1,a2),axis=0)
print(s1)
s2=np.sort((a1,a2),axis=1)
print(s2)