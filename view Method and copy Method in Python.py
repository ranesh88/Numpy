# view Method and copy Method in Python

from numpy import *

print("View () method in python")
a=array([10,20,30,40,50])
b=a.view()
print("a =",a)
print("b =",b)
print("id of b =",id(b))
print("id of a =",id(a))
a[0]=300
b[1]=540
print("a =",a)
print("b =",b)
print("id of b =",id(b))
print("id of a =",id(a))

print("copy () method in python")
b=copy(a)
print("a =",a)
print("b =",b)
a[0]=100
b[1]=80
print("a =",a)
print("b =",b)
print("id of b =",id(b))
print("id of a =",id(a))

