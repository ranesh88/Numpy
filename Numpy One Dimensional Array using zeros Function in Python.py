# Numpy One Dimensional Array using zeros Function in Python

from numpy import *

a=zeros(5)
print(a)

b=zeros(5,dtype=int)
print(b)

for i in a:
    print(i)
print("End of for loop")

n=len(b)
i=0
while i<n:
    print(b[i])
    i=i+1
print("end of while loop.")