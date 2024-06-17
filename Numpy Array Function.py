import numpy as np

#help(np.array)

#print(np.array([1, 2, 3]))
#print(np.array([1, 2, 3.0]))  #Upcasting:

# More than one dimension:

#print(np.array([[1, 2], [3, 4]]))

#Minimum dimensions 2:
#print(np.array([1, 2, 3],ndmin=2))

#Type provided:
#print(np.array([1, 2, 3], dtype=complex))

#Creating an array from sub-classes:
print(np.array(np.mat('1 2 3; 3 4 6;5 6 7')))
