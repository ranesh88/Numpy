# Accessing One Dimensional Numpy Array using while Loop in Python
from numpy import *
stu_roll=array([101,102,103,104,105])
print("Display the array = ",stu_roll)
length=len(stu_roll)
print("Length of the array is =",length)
print("Data type of the array is =",stu_roll.dtype)

print("Accessing element of the array without index by while loop::")
index=0
while index<len(stu_roll):
    print(stu_roll[index])
    index+=1
print("End of while loop.")

print("Accessing element of the array with index using while loop::")
i=0
length=len(stu_roll)
while i<length:
    print("Index",i,"=",stu_roll[i])
    i=i+1
print("End of while loop.")