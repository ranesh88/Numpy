# Two Dimensional Numpy Array using array Function in Python

from numpy import *

a=array([ [10,20,30,40],
          [50,60,70,80.0]  ])
print(a,dtype)

print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[0][3])

print()
print(a[1][0])
print(a[1][1])
print(a[1][2])
print(a[1][3])

print(a.dtype)

name=array([ ["raj","Sonam","Ankit","Neha"],
             ["Lenovo","HP","Dell","Asus"] ])
print(name,dtype)

print(name[0][0])
print(name[0][1])
print(name[0][2])
print(name[0][3])

print(name[1][0])
print(name[1][1])
print(name[1][2])
print(name[1][3])

print(name.dtype)