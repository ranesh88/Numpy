# Numpy One Dimensional Array using logspace() Function in Python

from numpy import *
from math import *
a=logspace(1,3,5)
print(a)
b=logspace(1,3,5,base=12)
print(b)
print(a[0])
print("Accessing logspace element using for loop without index::")
for item in a:
    print(trunc(item))
print("End of for loop.")

print("Accessing logspace element with index using for loop ::")
length=len(a)
for i in range(length):
    print("Index",i,"=",trunc(a[i]))
print("End of for loop with Index")

n=len(a)
i=0
while i<n:
    print(trunc(a[i]))
    i=i+1
print("End of while loop.")