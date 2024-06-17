# where Function in Python

from numpy import *

a=array([100,200,300,400,500])
b=array([10,201,30,40,50])

c=where(a>b,a,b)

print("a = ",a)
print("b = ",b)
print("After applying where function a>b :")
print(c)

a=array([101,12,300,4,500])
b=array([100,20,30,400,50])
c=where(a>b,a,b)
print(c)