# Accessing Numpy Two Dimensional Array using for Loop in Python

from numpy import *

a=array([ [10,20,30,40],
          [50,60,70,80] ])

print(a,dtype)

print("Accessing 2D array using for loop with out index::")

for row in a:
    for col in row:
        print(col,end=" ")
    print()
print("End of nested for loop.")

a=array([ [10,20,30,40],
          [50,60,70,80] ])

a[1][2]=100

n=len(a)
print("No. of rows in the array = ",n)

print("a[0]=",a[0])
print("Length of a[0]=",len(a[0]))
print("a[1]=",a[1])
print("Length of a[1]=",len(a[1]))

print("Accessing 2D array using for loop with index::")

for row in range(n):
    for col in range(len(a[row])):
        print(a[row][col],end=" ")
    print()
print("End of nested for loop.")
