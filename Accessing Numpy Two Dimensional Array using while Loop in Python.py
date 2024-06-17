# Accessing Numpy Two Dimensional Array using while Loop in Python

from numpy import *

a=array([[10,20,30,40],
         [50,60,70,80] ])

n=len(a)
row=0
while row <n:
    col=0
    while col< len (a[row]):
        print("Index",row,col,"=",a[row][col])
        col=col+1
    row=row+1
    print()