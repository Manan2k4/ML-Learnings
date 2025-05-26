import numpy as np

# ndarray, shapes, and data types
a = np.array([[1,2,3], [4,5,6]])
print(a.shape)      # (2, 3)
print(a.dtype)      # int64

# array creation and basic operations
zeros = np.zeros((2,2))
ones = np.ones((3,1))
identity = np.eye(3)
sum_array = np.add(a, a)

# indexing, slicing, and reshaping
print(a[0, 2])      # 3
sliced = a[:, 1]    #col 1: [2, 5]
reshaped = a.reshape(3, 2)

b = np.array([1,2,3])
print(a + b)