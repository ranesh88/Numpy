# Accessing One Dimensional Numpy Array using for Loop in Python

from numpy import *
stu_roll=array([101,102,103,104,105])
print("Display the array =",stu_roll)
print("Data type of the array = ",stu_roll.dtype)
length=len(stu_roll)
print("Length of the array",length)

print("Accessing element of the array without index by for loop::")
for i in stu_roll:
    print(i)
print("End of for loop.")



stu_roll[1]=110


print("Accessing element of the array with index by for loop::")
for i in range(length):
    print("Index",i,"=",stu_roll[i])
print("End of for loop")