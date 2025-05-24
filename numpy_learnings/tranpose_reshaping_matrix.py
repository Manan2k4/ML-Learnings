import numpy as np

data = np.array([1,2,3,4,5,6])
a = data.reshape(2,3)
print(a)
b = data.reshape(3,2)
print(b)

arr = np.arange(6).reshape((2, 3))
print(arr)

transpose = arr.T
print(transpose)