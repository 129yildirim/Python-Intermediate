import numpy as np


numbers1 = np.random.randint(10, 100, 6)
numbers2 = np.random.randint(10, 100, 6)

print('numbers1:\t', numbers1)
print('numbers2:\t', numbers2)
print('numbers1+10:\t', numbers1+10)
print('sum of them:\t', numbers1 + numbers2)
print('nums1-nums2:\t', numbers1 - numbers2)
print('sine of nums1:\t', np.sin(numbers1)) 
print('cosine nums1:\t', np.cos(numbers1)) 
print('sqrt of nums1:\t', np.sqrt(numbers1))
print('log(base e) nums1:\t', np.log(numbers1))
print('log(base 10) nums1:\t', np.log10(numbers1))
print('log(base 2) nums1:\t', np.log2(numbers1))

numbers1 = numbers1.reshape(2, 3)
numbers2 = numbers2.reshape(2, 3)

print('numbers1:')
print(numbers1)
print('numbers2:')
print(numbers2)

print('vertical stack:')
print(np.vstack((numbers1,numbers2)))
print('horizontal stack:')
print(np.hstack((numbers1,numbers2)))

print('numbers >= 30?:\t') 
print(numbers1 >= 30)# no need the for loops. It automatically checks the items