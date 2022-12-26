import numpy as np
print("numpy version :" ,np.__version__)

# -------------------------------------------------------
# Question : Create a 1D array of numbers from 0 to 9
# Output : #> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Solution
X = np.arange(10)
#------------------------------------------------------------
# Question : Create a 3×3 numpy array of all True’s

# Solution
np.full((3,3), True, dtype=bool)

#or
np.full((9), True, dtype=bool).reshape(3,3)

#or
np.ones((3,3), dtype=bool)

#or
np.ones((9), dtype=bool).reshape(3,3)

# -------------------------------------------------
# Question : Extract all odd numbers from array
# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: array([1, 3, 5, 7, 9])

#Solution

arr = np.arange(10)

out=arr[arr%2 == 1]

# --------------------------------
# Question: Replace all odd numbers in arr with -1
# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])

# Solution

arr = np.arange(10)

arr[arr%2 == 1] = -1
# print(arr)


# ----------------------------------------------
# Question: Replace all odd numbers in arr with -1 without changing arr
# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: out
# array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])
# arr
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Solution

arr = np.arange(10)

out = arr.copy()

out[out%2 == 1] = -1

print('Modified Array')
print(out)
print('\nOriginal Array')
print(arr)

# --------------------------------------------
# Question: Convert a 1D array to a 2D array with 2 rows
# input: np.arange(10)
# output array([[0, 1, 2, 3, 4],
#               [5, 6, 7, 8, 9]])

# Solution

arr = np.arange(10)
arr.reshape(2,5)

# Another solution
arr = np.arange(10)
arr.reshape(2, -1)   # Setting to -1 automatically decides the number of cols


# -----------------------------------------------
# Question: Stack arrays a and b vertically
# input: a = np.arange(10).reshape(2,-1)
#        b = np.repeat(1, 10).reshape(2,-1)

# output: array([[0, 1, 2, 3, 4],
#                [5, 6, 7, 8, 9],
#                [1, 1, 1, 1, 1],
#                [1, 1, 1, 1, 1]])

# Solution

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

np.vstack([a,b])

# -----------------------------------
# Question: Stack the arrays a and b horizontally.

# Input: a = np.arange(10).reshape(2,-1)
#        b = np.repeat(1, 10).reshape(2,-1)
# Output: array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
#                [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])


# Solution:
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

np.hstack([a,b])
# -----------------------------------------
# Question: Create the following pattern without hardcoding. Use only numpy functions and the below input array a.

# Input: a = np.array([1,2,3])
# Output: array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])


# Solution

a = np.array([1,2,3])
np.r_[np.repeat(a, 3), np.tile(a, 3)]

#other solution
np.hstack((np.repeat(a, 3), np.tile(a, 3)))
# ------------------------------------------
# Question: Get the common items between a and b

# Input: a = np.array([1,2,3,2,3,4,3,4,5,6])
#        b = np.array([7,2,10,2,7,4,9,4,9,8])

# Output: array([2, 4])


# Solution:
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)

# -----------------------------------------------
# Question: From array a remove all items present in array b

# Input: a = np.array([1,2,3,4,5])
#        b = np.array([5,6,7,8,9])

# Output: array([1,2,3,4])


# Solution
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

np.setdiff1d(a,b)

# -----------------------------------------------
# Question: Get the positions where elements of a and b match

# Input: a = np.array([1,2,3,2,3,4,3,4,5,6])
#        b = np.array([7,2,10,2,7,4,9,4,9,8])

# Output: (array([1, 3, 5, 7]),)


# Solution

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

np.where(a == b)
# ------------------------------------------

# Question: Get all items between 5 and 10 from a.

# Input: a = np.array([2, 6, 1, 9, 10, 3, 27])
# Output: (array([6, 9, 10]),)


# Solution

a = np.array([2, 6, 1, 9, 10, 3, 27])
x = a[(a >= 5) & (a <= 10)
# -----------------------------------------------