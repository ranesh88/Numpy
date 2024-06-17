# any and all Functions in Python
# These are python built in function

from numpy import *

a=array([100,200,300,400,500])
b=array([100,20,30,400,50])
c=a==b
print(a)
print(b)

print("any() function apply on a and b array::")
print(any(c))


d=array([100,200,300,400,500])
e=array([100,200,300,400,500])
f=d==e
print(d)
print(e)
print("all() function apply on d and e array::")
print(all(f))

