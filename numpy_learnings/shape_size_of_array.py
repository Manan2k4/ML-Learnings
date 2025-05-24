import numpy as np

# Initializing a 3D array
array_example = np.array([[[0,1,2,3],[4,5,6,7]],
                          [[0,1,2,3],[4,5,6,7]], 
                          [[0,1,2,3],[4,5,6,7]]])

# Return no. of dimensions
ndim = array_example.ndim
print(ndim)

# Print total no. of elements in array
size = array_example.size
print(size)

# return no. of elements at each dimension level
# starting from highest level, i.e.
# at outer dimension:
# we have 3 elements (3 copies of [[0,1,2,3],[4,5,6,7]]),
# at middle dimension:
# we have 2 elements ([[0,1,2,3], [4,5,6,7]]),
# and at last, at inner dimension:
# we have 4 elements([[0,1,2,3]=4 [4,5,6,7]=4])
shape = array_example.shape
print(shape)