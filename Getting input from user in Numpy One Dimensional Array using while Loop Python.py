# Getting input from user in Numpy One Dimensional Array using while Loop Python

from numpy import *

n=int(input("Enter no. of elements ::"))
a=zeros(n,dtype=int)
print(a)

i=0
while i<n:
    x=int(input("Enter element::"))
    a[i]=x
    i=i+1
print("End of input while loop")

print("Show array elements ::")
i=0
while i<n:
    print(a[i],end=" ")
    i=i+1
print("\nEnd of display while loop")

print(type(a))