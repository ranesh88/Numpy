# Numpy One Dimensional Array using linspace() Function in Python
from numpy import *

print("Creating Array using linspace () Function")
a=linspace(1,8,5)
print(a)
b=linspace(1,8)
print(b)
c=linspace(1,8,150)
print(c)
d=linspace(1,8,num=5,endpoint=False)
print(d)

print("Accessing with the help of for loop::")
for index in a :
    print(index)
print("End of for loop.")

length=len(a)
for i in range(length):
    print("Index",i,"=",a[i])
print("End of for loop with index")


print("Accessing linspace element with the help of while loop::")
i=0
while i<len(a):
    print("Index",i,"=",a[i])
    i=i+1
print("End of while loop.")