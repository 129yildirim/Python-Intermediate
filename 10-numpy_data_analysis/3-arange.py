import numpy as np

arr1 = np.arange(0,10)
arr2 = arr1 # Reference
arr3 = arr1.copy() # Copy

arr1[0] = 8
print('arr1:\t', arr1)
print('arr2:\t', arr2)
print('arr3:\t', arr3)


