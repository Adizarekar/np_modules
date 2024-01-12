import numpy as np
import time
import sys

l = range(1000)
print(sys.getsizeof(5)*len(l))

array1 = np.arange(1000)
print(array1.size*array1.itemsize)

l1= range(1000000)
l2 = range(1000000)
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("Python list took time:", (time.time()-start)*1000)

np1 = np.arange(1000000)
np2 = np.arange(1000000)
start = time.time()
result = np1+np2
print("NP list took time:", (time.time()-start)*1000)


