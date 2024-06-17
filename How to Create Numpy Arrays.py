import numpy as np

#Create Numpy Arrays
arr=np.array([[1,2,3,4,5],[3,4,5,6,7],[1,3,5,7,8]])
#print(arr)
#print(type(arr))

#Slicing Operation in NumPy 1D Arrays

arr=np.array([10,20,30,40,50])
#print(arr[2::2])

#Slicing Operation in NumPy 2D Arrays

arr=np.array([[10,20,30,40,50],[60,70,80,90,100]])
#print(arr[0:2,1:3])
#print(arr[1,2::2])

arr=np.array([[10,20,30,40,50],[60,70,80,90,100],[101,102,103,104,105]])
#print(arr[2,2:])

arr=np.array([[10,20,30,40,50],[60,70,80,90,100],[101,102,103,104,105]])
#print(arr)

#Numpy Attributes
arr=np.array([[10,20,30,40,50],[60,70,80,90,100],[101,102,103,104,105]])
#print(np.shape(arr))
#print(np.size(arr))
#print(np.ndim(arr))
print(arr.dtype)


