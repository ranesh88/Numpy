# One Dimensional Numpy Array using array Function

from numpy import *
stu_roll=array([101,102,103,104,105])
print("Show the array = ",stu_roll)
print("Type of the array =",type(stu_roll))
print("Data type of the array = ",stu_roll.dtype)
print("value of index 0 =",stu_roll[0])

#Accessing 1D array elements ::
print("Accessing array elements with for loop::")
length=len(stu_roll)
print("Length of the array is =",length)
for i in range(length):
    print("index",i,"=",stu_roll[i])
print("End of for loop.")

# Modifying 1d array ::
print("Modifying 1D array element::")
stu_roll[1]=110
print(stu_roll)
for i in range(length):
    print("index",i,"=",stu_roll[i])
print("End of for loop.")

#Explicit conversion of data type in the array
stu_roll=array([101,102,103,104,105],dtype=float)
print(stu_roll)
print("Data type of the array = ",stu_roll.dtype)

for i in range(length):
    print("index",i,"=",stu_roll[i])
print("End of for loop.")

#Implicit conversion of data type in array ::
emp_sal=array([10100,10002,10300.25,10400.50,10000])
print(emp_sal)
print("Data type of the array = ",emp_sal.dtype)

for i in range(length):
    print("index",i,"=",emp_sal[i])
print("End of for loop.")

char_array=array(['a','b','c','d','e'])
print(char_array)
print("Data type of the array = ",char_array.dtype)

name=array(["Rahul","Sonam","Raj","Ankit","Mohan"])
print(name)
print("Data type of the array = ",name.dtype)