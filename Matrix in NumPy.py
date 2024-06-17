# Matrix in NumPy
import numpy as  np

a = np.array([[1,2],[3,4]])
b = np.array([[10,20],[30,40]])

print(a)
print(b)

print("Array Addition::")
print(a+b)

print("Array Multiplication::")
print(a*b)

print("Matrix Multiplication::")
print(a.dot(b))

a = np.array([[10, 20, 30], [40, 50, 60]])
print("Original Matrix ::")
print(a)
print("Transpose of Matrix ::")
a = np.array([[10, 20, 30],[40, 50, 60]])
print(np.transpose(a))
print("Transposed Matrix ::")
print(a.transpose())
