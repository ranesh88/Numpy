# Getting input from user in Numpy One Dimensional Array using for Loop Python

from numpy import *

n=int(input("Enter number of elements::"))
a=zeros(n,dtype=int)
print("Print the zeroes array ::",a)

print("Taking input in one dimensional numpy array::")

for i in range(n):
    x=int(input("Enter elements::"))
    a[i]=x
print("End of for loop")

for i in range (len(a)):
    print(a[i])

print(a)

print("Taking input in list::")
list1=[]
for i in range(n):
    list1.append(int(input("Enter elements::")))
print("End of for loop")

print(list1)


from array import *
print("Taking input in 1D array::")

num=array("i",[])
nn=int(input("How many elements want to insert ?"))
for i in range(nn):
    num.append(int(input("Enter elements::")))

print(*num)
