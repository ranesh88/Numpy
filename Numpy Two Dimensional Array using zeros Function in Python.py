# Numpy Two Dimensional Array using zeros Function in Python

from numpy import *
a=zeros((3,2))
print(a)

print("a[0][0]=",a[0][0])
print("a[0][1]=",a[0][1])

print("a[1][0]=",a[1][0])
print("a[1][1]=",a[1][1])

print("a[2][0]=",a[2][0])
print("a[2][1]=",a[2][1])

print("Accessing element without index using for loop::")

for row in a :
    for col in row:
        print(col)
    print()

z=zeros((3,3),dtype=int)
print(z)
nn=len(z)
print("No. of rows in the zeros array ::=",nn)
print("z[0]=",z[0])
print("No. of columns in z[0]=",len(z[0]))
print("z[1]=",z[1])
print("No.of columns in z[1]=",len(z[1]))
print("z[2]=",z[2])
print("No.of columns in z[2]=",len(z[2]))

print("Accessing element with index using for loop::")

for row in range(nn):
    for col in range(len(z[row])):
        print("Index",row,col,"=",z[row][col])
    print("End of row",row)


print("Accessing element using while loop::")
a=zeros((3,3),dtype=int)

n=len(a)
row=0
while row < n:
    col=0
    while col < len(a[row]):
        print("Index",row,col,"=",a[row][col])
        col=col+1
    print("End of row", row)
    row=row+1

