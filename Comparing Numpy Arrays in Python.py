# Comparing Numpy Arrays in Python

from numpy import *

a=array([101,102,103,104,105])
b=array([101,102,103,104,105])

c=a==b
print(c)

a=array([100,200,300,400,500])
b=array([100,20,30,400,500])
c=a==b
print(c)
less=a<b
print(less)
a=array([100,2,300,4,500])
b=array([100,20,30,400,500])
less=a<b
print(less)
a=array([100,2,300,4,500])
b=array([100,20,30,400,500])
more=a>b
print(more)

a=array([100,2,300,4,500])
b=array([100,20,30,400,500])
less_equal=a<=b
print(less_equal)
greater_equal=a>=b
print(greater_equal)
not_equal=a!=b
print(not_equal)

