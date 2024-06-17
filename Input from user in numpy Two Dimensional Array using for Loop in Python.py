# Input from user in numpy Two Dimensional Array using for Loop in Python

from numpy import *

row=int(input("Enter number of Rows::"))
col=int(input("Enter number of Columns::"))
a=zeros((row,col),dtype=int)
print(a)

print("Taking input in 2D array using for loop::")
for r in range(row):
    for c in range (len(a[r])):
        x=int(input(f"Enter element{[r]}{[c]}="))
        a[r][c]=x
    print("End of row",r)
print("End of input for loop")

print("Display 2D array with index::")

for r in range(row):
    for c in range(len(a[r])):
        print(a[r][c],end=" ")
    print()

print("Display 2D array without index::")
for r in a:
    for c in r:
        print(c,end=" ")
    print()
