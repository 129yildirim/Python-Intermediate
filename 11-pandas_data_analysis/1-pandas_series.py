import pandas as pd
import numpy as np


numbers = [20, 30, 40, 50, 60, 90]


pandas_series = pd.Series()
print('empty serie:\t', pandas_series)

pandas_series = pd.Series(numbers)
print('numbers serie:\n', pandas_series)

letters= ['a', 'b', 'c', 'd', 54]

pandas_series = pd.Series(letters)
print('letters serie:\n', pandas_series)

pandas_series = pd.Series(7)
print('scalar serie:\n', pandas_series)

pandas_series = pd.Series(8, [0, 1, 4 ,3])
print('scalars serie:\n', pandas_series)

pandas_series = pd.Series(numbers, ['a', 'b', 'c', 'd', 'e', 'f'])
print('scalars serie:\n', pandas_series)

dicti = {'a':10, 'b':20, 'c':30, 'y':90}

pandas_series = pd.Series(dicti)
print('dict pandas:\n', pandas_series)

randints = np.random.randint(10, 60, 6)

pandas_series = pd.Series(randints)
print('randint pandas:\n', pandas_series)

pandas_series = pd.Series([10, 20, 30, 40], ['a', 'b', 'c', 'd'])
print('first el of serie:\n', pandas_series[0])
print('first el of serie:\n', pandas_series['a'])
print('two el of serie:\n', pandas_series[['a', 'c']] )

print('dim of serie:\t', pandas_series.ndim)
print('type of serie:\t', pandas_series.dtype)
print('shape of serie:\t', pandas_series.shape)
print('sum of serie:\t', pandas_series.sum())
print('max of serie:\t', pandas_series.max())
print('min of serie:\t', pandas_series.min())
print('sum of two serie:\n', pandas_series + pandas_series)
print('elements > 30:\n', pandas_series>30)

