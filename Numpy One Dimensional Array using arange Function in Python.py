# Numpy One Dimensional Array using arange() Function in Python

from numpy import *

a=arange(5)
print(a)
b=arange(5.0)
print(b)
c=arange(1,6)
print(c)
d=arange(1,10,2)
print(d)

print(a[0])

for i in a:
    print(i,end=" ")
print()
n=len(a)
i=0
while i<n:
    print(a[i],end=" ")
    i=i+1


