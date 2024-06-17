# Numpy One Dimensional Array using ones Function in Python

from numpy import *
a=ones(5)

print(a[0])
print(a)

for item in a:
    print(item)
print("End of for loop.")

n=len(a)
i=0
while i<n:
    print(a[i])
    i=i+1
print("End of while loop.")

print("Accessing ones elemet using for loop with index::")
length=len(a)
for i in range(length):
    print("Index",i,"=",a[i])
print("End of index for loop.")

print("Accessing ones element using while loop with index::")
i=0
n=len(a)
while(i<n):
    print("Index",i,"=",a[i])
    i=i+1
print("End of while loop.")