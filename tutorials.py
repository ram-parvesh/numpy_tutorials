import os
import numpy as np
from numpy import *
squares = [x**2 for x in range(10)]         # python list
cubes = tuple(x**3 for x in range(10))      # python tuple
evens = {x for x in range(10) if x%2 == 0}  # python set

rand_arr = np.random.random((5,3))   # 5 rows and 3 column with random value

arr = np.arange(10)      # input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr%2 == 1] = -1     # output: array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])

arr.reshape(2,5)  == arr.reshape(2, -1)  #both are same 

arr = np.arange(10).reshape(2,-1)

# Get all items between 5 and 10 from a.
a = np.array([2, 6, 1, 9, 10, 3, 27])
x = a[(a >= 5) & (a <= 10)]

A = np.array([x**2 for x in range(1, 11)]).reshape(2, 5)

print(A, end='\n\n')
print('A[0]\t\t', A[0])
print('A[-1]\t\t', A[-1])
print('A[0][0]\t\t', A[0][0])
print('A[-1][-1]\t', A[-1][-1])

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
# a block from the original array
out = A[1:4, 1:4]
# strides
out = A[::2, ::2]

A = np.array([1,2,3,4,5])
out = A[::] # lower, upper, step all take the default values
out = A[::2] # step is 2, lower and upper defaults to the beginning and end of the 
out = A[:3] # first three elements
out = A[3:] # elements from index 3
out = A[-1] # the last element in the array
out = A[-3:] # the last three elements

# slicing NumPy arrays
cubes = np.arange(1, 13).reshape(4, 3)**3 # cubes of 1-12

print(cubes[:,:], end='\n\n')         # all rows, all cols
print('First Column:\t', cubes[:, 0]) # first col
print('Last Column:\t', cubes[:, -1]) # last col
print('First Row:\t', cubes[0, :])    # first row
print('Last Row:\t', cubes[-1, :])    # last row

# Advanced: using ... for axis completion
A = np.arange(125).reshape(5, 5, 5) + 1

print('A[0, ...] == A[0, :, :]', end='\n\n')
print(A[0, ...], '\n\n', A[0, :, :])       #both are same


v = np.array([1,2,3])
v.shape    #output (3,)
# make a column matrix of the vector v
v[:, newaxis]  #output array([[1],
                           #  [2],
                           #  [3]])
# column matrix
v[:,newaxis].shape       #output (3,1)
# column matrix
v[newaxis,:].shape       #output (1,3)