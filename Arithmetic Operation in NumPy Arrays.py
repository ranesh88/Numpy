# Arithmetic Operation in NumPy Arrays

import numpy as np

print("1D Array Arithmetic Operation::")
a=np.arange(1,5)
print(a)
print(a+2)
print(a*3)
print(a/2)
print(a-1)
print(a**2)
print(a%2)

print("2D Array Arithmetic Operation::")
a=np.array([[1,2],[3,4]])
print(a)
print(a+2)
print(a*3)
print(a/2)
print(a-1)
print(a**2)
print(a%2)

a=np.array([10,20,30,40])
b=np.arange(1,5)
print(a,b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)

print("2D Array Arithmetic opeartion::")
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,1],[2,1,1]])
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)

print("2D Array Arithmetic opeartion using function::")
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,1],[2,1,1]])
print(a)
print(b)
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
print(np.mod(a,b))
print(np.power(a,b))






