# reshape Function and flatten Method in Python

from numpy import *
a=array([1,2,3,4,5,6])

print("Accessing 1D array elements using for loop::")
for row in a:
    print(row,end=" ")
print("\nEnd of for loop.")

print('reshape () function::')
print('Converting 1D array to 2D array::')

print()
b=reshape(a,(2,3))
print(b)


c=array([1,2,3,4,5,6,7,8,9,10,11,12])
print("Accessing array element using for loop with index::")
n=len(c)
for row in range (n):
    print(c[row],end=" ")
print("\nEnd of for loop.")
print("***************** reshape() method ********************")
print('Converting 1D array to 3D array::')
d=reshape(c,(2,3,2))
print(d)

e=array([[1,2,3],
         [4,5,6]])

print(e)
print("Accessing 2D array using for loop::")
nn=len(e)
for row in range(nn):
    col=0
    for col in range(len(e[row])):
        print(e[row][col])
    print("End of row",row)

print("Convert 2D array to 1D array using reshape() method:: ")
f=reshape(e,(6))
print(f)
print("************** flatten() method ******************")
print("2D array::")
print(e)
print("2D array convert to 1D array by flatten() method ::")
flatten_array=e.flatten()
print(flatten_array)
print("3D array")
print(d)
print("3D array convert to 1D array by flatten() method ::")
flatten_array=d.flatten()
print(flatten_array)