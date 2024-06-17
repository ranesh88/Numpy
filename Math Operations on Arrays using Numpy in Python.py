# Math Operations on Arrays using Numpy in Python

from numpy import *
a=array([101,102,103,104,105])
b=array([301,302,303,304,305])
sum=a+b
print("Display of a::",a)
print("Display of b::",b)
print("Addition of a + b =",sum)
c=a+5
print(c)
sub=b-a
print("Subtraction from b to a = ",sub)
mul=a*5
print(mul)
div=a/5
print("Division by 5 result =",div)

for i in sum:
    print(i)
print("End of for loop....")