# Broadcasting

import numpy as np

a=np.array([10,20,30])
b=np.array([1,2,3,4])

print("a=",a)
print("b=",b)

print("Shape of a =",np.shape(a))
print("Shape of b =",np.shape(b))

print("Dimension of a =",np.ndim(a))
print("Dimension of b=",np.ndim(b))

#print(a+b)
#ValueError: operands could not be broadcast together with shapes (3,) (4,)

x=np.array([[1,2],[3,4],[5,6]])
y=np.array([10,20])

print("x=",x)
print("y=",y)

print("Shape of x =",np.shape(x))
print("Shape of y =",np.shape(y))

print("Dimension of x =",np.ndim(x))
print("Dimension of y =",np.ndim(y))

print("Output x+y =\n",x+y)


m=np.array([[1,2],[3,4],[5,6]])
n=np.array([10,20,30])

print("m=",m)
print("n=",n)

print("Shape of m =",np.shape(m))
print("Shape of n =",np.shape(n))

print("Dimension of m =",np.ndim(m))
print("Dimension of n =",np.ndim(n))

#print("Output m+n =\n",m+n)
#ValueError: operands could not be broadcast together with shapes (3,2) (3,)


print("2D Arrays with different shapes::")

p=np.array([[1,2],[3,4],[5,6]])
q=np.array([10,20,30])

print("p=",p)
print("q=",q)

print("Shape of p =",np.shape(p))
print("Shape of q =",np.shape(q))

print("Dimension of p =",np.ndim(p))
print("Dimension of q =",np.ndim(q))

#print("Output p+q =\n",p+q)
#ValueError: operands could not be broadcast together with shapes (3,2) (3,)


c=np.array([[1],[2],[3]])
d=np.array([10,20,30])
print("c=",c)
print("d=",d)

print("Shape of c =",np.shape(c))
print("Shape of d =",np.shape(d))

print("Dimension of c =",np.ndim(c))
print("Dimension of d =",np.ndim(d))

print("Output c+d =\n",c+d)