import numpy as np

arr = np.array([2,1,5,3,7,4,6,8])

# Sort in ascending
print(np.sort(arr))

# Concatenation of a and b
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
ab = np.concatenate((a,b))

print(ab)

x = np.array([[1,2], [3,4]])
y = np.array([[5,6]])
xy = np.concatenate((x,y), axis=0)

print(xy)