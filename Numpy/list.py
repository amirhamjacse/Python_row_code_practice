import numpy as np
ab = [1, 3, 2]

# 1D array using numpy
a = np.array([1, 2, 3])

#2D array using numpy

arr = np.array([[1, 2, 3],
              [4, 5, 6]])

print(arr)

print(arr.shape, "Shape") # rows, columns
print(a.ndim)    # number of dimensions
print(arr.ndim)    # number of dimensions
print(a.size)    # total elements
print(a.dtype)   # data type

print(a+arr, "array sum") #array addition


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a * b)   # [4 10 18]
