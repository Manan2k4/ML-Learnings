import numpy as np

arr = np.array([[10,20,30], [40,50,60]])
print("Row-wise sum: ", np.sum(arr, axis=1))
print("Col-wise mean: ", np.mean(arr, axis=0))