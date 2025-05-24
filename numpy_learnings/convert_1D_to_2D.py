import numpy as np

a = np.array([1,2,3,4,5,6])
print(a.shape)

# Converting a 1D array with
# n elements into a 2d array
# of 1 row and n columns
a2 = a[np.newaxis, :]
print(a2.shape)

row_vector = a[np.newaxis, :]
print(row_vector.shape)

col_vector = a[:, np.newaxis]
print(col_vector.shape)

# Adding axis at index position 1
b = np.expand_dims(a, axis = 1)
print(b.shape)

# Adding axis at index position 0
c = np.expand_dims(a, axis=0)
print(c.shape)

