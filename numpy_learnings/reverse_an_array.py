import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

rev_arr = np.flip(arr)

print('Reversed array: ', rev_arr)

# -----------------------------------------

arr_2d = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9,10,11,12]])

rev_2d_arr = np.flip(arr_2d)
print("Reversed 2d Array: ", rev_2d_arr)

reversed_arr_rows = np.flip(arr_2d, axis=0)
print("Reversed the rows: ",reversed_arr_rows)

reversed_arr_cols = np.flip(arr_2d, axis=1)
print("Reversed the cols: ", reversed_arr_cols)

arr_2d[1] = np.flip(arr_2d[1])
print(arr_2d)

arr_2d[:,1] = np.flip(arr_2d[:,1])
print(arr_2d)