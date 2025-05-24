import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

arr1 = a[3:8]
print(arr1)

a1 = np.array([[1,1],
               [2,2]])
a2 = np.array([[3,3],
               [4,4]])

# Print arrays into structure: a1
#                              a2
print(np.vstack((a1,a2)))

# Print arrays into structure: a1 a2
print(np.hstack((a1,a2)))

# print 1D array from 1 to 25 and reshape 
# into 2 rows and 12 cols
x = np.arange(1, 25).reshape(2, 12)
print(x)

# divide the x into 3 equal parts vertically
hsplit = np.hsplit(x, 3)
print(hsplit)

u_hsplit = np.hsplit(x, (3,4))
print(u_hsplit)

ab = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b1 = ab[0, :]
print(b1)

b1[0] = 99
print(b1)

print(a)