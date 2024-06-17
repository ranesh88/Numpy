# Slicing on Two Dimensional Array in Python

from numpy import *

n=array([[10,20,30],
         [40,50,60],
         [70,80,90]])

print("Original array::")
print(n)

print("0th row and all columns::")
a=n[0,:] #0 is only 0th row ,: means all columns in 0th row
         # Left side of , signifies row
for i in a:
    print(i)
print("1st row and all columns::")
a=n[1,:]
for i in a:
    print(i)

print("2nd row and all columns::")
a=n[2,:]
for i in a:
    print(i)

print("0th column and all rows::")
a=n[:,0]  #0 is only 0th column ,: means all rows in 0th column
          # Right side of , signifies column
for i in a:
    print(i)
print("1st column and all rows::")
a=n[:,1]
for i in a:
    print(i)

print("2nd column and all rows::")
a=n[:,2]
for i in a:
    print(i)

n=array([[10,20,30],
         [40,50,60],
         [70,80,90]])

a=n[0:1,0:1]
print(a)

a=n[2:3,2:3]
print(a)

a=n[0:2,1:3]
print(a)

a=n[1:3,1:3]
print(a)

a=n[1:3,0:2]
print(a)


