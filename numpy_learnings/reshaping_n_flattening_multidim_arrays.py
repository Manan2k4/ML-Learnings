import numpy as np

x = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8], 
              [9,10,11,12]])

flatten = x.flatten()
print(flatten)

a1 = x.flatten()
a1[0] = 99
print(x)
print(a1)

a2 = x.ravel()
a2[0] = 98
print(x)
print(a2)