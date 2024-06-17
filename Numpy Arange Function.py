# Numpy Arange Function | Creating NumPy Arrays

import numpy as np

#help(np.arange)

#print(np.arange(0, 5, 0.5, dtype=int))
#print(np.arange(-3, 3, 0.5, dtype=int))
#In such cases, the use of `numpy.linspace` should be preferred.

#power = 40
#modulo = 10000
#x1 = [(n ** power) % modulo for n in range(8)]
#x2 = [(n ** power) % modulo for n in np.arange(8)]
#print(x1)
#print(x2)

#print(np.arange(1,10))
#print(np.arange(3.0))
#print(np.arange(1,10,2))
#print(np.arange(5,dtype='complex'))
#print(np.arange(1,10,2,dtype=float))
print(np.arange(1,10,2,float))
