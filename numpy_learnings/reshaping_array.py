import numpy as np

a = np.arange(6)
print(a)

# np.reshape(no_of_rows, no_of_columns)
b = a.reshape(3,2)
print(b)

# Convert a 1D array to a 2D array
# as 1 row and 6 columns
c = np.reshape(a, shape=(1,6), order='C')
print(c)