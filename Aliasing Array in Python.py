# Aliasing Array in Python

from numpy import *

a=array([10,20,30,40,50])
b=a
print("b=",b,"id of b=",id(b))
print("a=",a,"id of a=",id(a))