# Indexing Operation in NumPy Arrays

import numpy as np

a=np.array([1,2,3,4,5,6,7])
print(a[3])
print(a[-4])

b=np.array([[1,2],[3,4],[5,6]])
print(b[-1])
print(b[-3][-2])

c=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
            [[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
print(c)
print(c[-2][-3][-3])
print(c[0][0][1])

print(c[1][0][3])
print(c[-1][-3][-1])
