# Input from User in Numpy Two Dimensional Array using while Loop in Python

from numpy import *

row=int(input("Enter number of rows::"))
col=int(input("Enter number of columns::"))
a=zeros((row,col),dtype=int)
print(a)

print("Taking input in 2D array using while loop::")
r=0
while r<row:
    c=0
    while c<(len(a[r])):
        x=int(input(f"Enter element {[r]}{[c]}="))
        a[r][c]=x
        c=c+1
    print("End of row",r)
    r=r+1
print("End of input while loop")

print("Display 2D array::")
r=0
while r < row:
    c=0
    while c<(len(a[r])):
        print(a[r][c],end=" ")
        c=c+1
    print()
    r=r+1

