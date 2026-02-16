import numpy as np
# ab = [1, 3, 2]

# # 1D array using numpy
# a = np.array([1, 2, 3])

# #2D array using numpy

# arr = np.array([[1, 2, 3],
#               [4, 5, 6]])

# print(arr)

# print(arr.shape, "Shape") # rows, columns
# print(a.ndim)    # number of dimensions
# print(arr.ndim)    # number of dimensions
# print(a.size)    # total elements
# print(a.dtype)   # data type

# print(a+arr, "array sum") #array addition


# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(a + b)   # [5 7 9]
# print(a * b)   # [4 10 18]

# a1 = np.zeros((2,3))   # matrix full of 0
# a2 = np.ones((2,3))    # matrix full of 1
# a3 = np.arange(0,10000)   # like range()
# a4 = np.linspace(0,1,5) # 5 numbers between 0 and 1

# print(a1,a2,a3,a4)


# b1 = np.random.rand(2,2)  # random numbers 0-1
# b2 = np.random.randint(1,10,5)  # random integers
# print(b1, b2)


# a = np.array([[1,2,3],
#               [4,5,6]])

# print(a[0,1])     # 2
# print(a[:,1])     # entire column
# print(a[1,:])     # entire row

# a[a > 3]   # elements greater than 3

# a = np.array([1,2,3])
# print(a + 5)


a = np.array([[1,2],
              [3,4]])

la1 = np.linalg.det(a)     # determinant
la2 = np.linalg.inv(a)     # inverse
la3 = np.dot(a, a)         # matrix multiplication

print(la1, la2, la3)

a = np.arange(6)
print(a.reshape(2,3))


a = np.array([1,2,3,4,5])

m1 = np.mean(a)
m2 = np.std(a)
m3 = np.min(a)
m4 = np.max(a)



# slow
total = 0
for i in range(1000000):
    total += i

print(total )

# fast
nploop = np.sum(np.arange(1000000))

print(nploop)