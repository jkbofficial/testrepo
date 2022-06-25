import numpy as np


arr = np.array([2,5,6,8], dtype = int)
print(arr)
# [2 5 6 8]
print(type(arr))
# class 'numpy.ndarray'
print(np.result_type(arr))
# int32


''' Creation of an array with step size 1.33 between 0 - 10 '''
print(np.arange(0, 10, 1.33, dtype=np.float64))
# [ 0.    1.33  2.66  3.99  5.32  6.65  7.98  9.31]
# arange() gives uncertain number of values based on steps
# Hence, we use linspace, which asks for total number of values
''' Creation of an array with total 5 values between 0 - 160 '''
print(np.linspace(0, 160, 5, dtype=np.float64))
# [   0.   40.   80.  120.  160.]


"Matrix Creation"
"Method1:Using array and reshape to convert array into matrix"
a = np.array([9,5,6,7,12,3])
print(a.reshape(2,3))

'''Method2: Using matrix function'''
b =np.matrix([[1,4],[6,8]])
print(b)

'Method 3:using misc function'
d = np.eye(3,dtype=np.int64)
print(d)

e = np.zeros((3,3))
print(e)

f = np.ones((3,3),dtype=np.int64)
print(f)