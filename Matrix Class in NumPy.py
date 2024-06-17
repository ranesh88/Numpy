# Matrix Class in NumPy

import numpy as np

a = np.matrix("1 2 ;3 4")
print(a)

b = np.matrix([[10,20],[30,40]])
print(b)

print("Matrix Addition ::")
print(a+b)

print("Matrix Multiplication ::")
print(a*b)

print("Transpose of matrix a ::")
print(a.T)

print("Transpose of matrix b ::")
print(b.T)



