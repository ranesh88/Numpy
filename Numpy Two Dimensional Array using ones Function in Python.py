# Numpy Two Dimensional Array using ones Function in Python

from numpy import *

a=ones((3,3),dtype=int)

print(a)

print("Accessing ones element using for loop with out index::")

for row in a:
    for col in row:
        print(col)
    print()

print("Accessing ones element using for loop with index::")
n=len(a)
for row in range (n):
    for col in range (len(a[row])):
        print("Index",row,col,"=",a[row][col])
    print("End of row",row)

print("Accessing ones element using while loop::")
n=len(a)
row=0
while row <n:
    col=0
    while col<len(a[row]):
        print(a[row][col])
        col=col+1
    print("End of row", row)
    row=row+1
