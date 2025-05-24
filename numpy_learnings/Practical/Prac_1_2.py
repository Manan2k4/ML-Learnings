import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

row_sums = arr.sum(axis = 1)
print("Row sums: ", row_sums)

col_means = arr.mean(axis=0)
print("Column means: ", col_means)

# -----------------------------------------------

A = np.array([[3,1], [1,2]])
b = np.array([9,8])

x = np.linalg.solve(A, b)
print("Solution x: ", x)