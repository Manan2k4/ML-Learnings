import numpy as np

A = np.array([[2,3], [3,1]])    # as in 2x+3y, and 3x+y
B = np.array([8,5])     # as in 2x+3y=8 and 3x+y=5

solution = np.linalg.solve(A, B)
print("Solution [x, y]: ", solution)