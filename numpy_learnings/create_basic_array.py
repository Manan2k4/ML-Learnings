import numpy as np

# Create an entire array filled with 1's 
# with range given at parentheses
ones = np.ones(3)
print(ones)

# Create an entire array filled with 0's 
# with range given at parentheses
zeroes = np.zeros(3)
print(zeroes)

# Creates an empty array with range we give in
# parentheses
arr = np.empty(2)

for i in range(arr.size):
    arr[i] = float(input(f"Enter value {i+1}: "))

print(arr)

# the arange function starts from and goes to how 
# much we give range
arange = np.arange(4)
print(arange)

# np.arange(1st number, last number, step size)
arange_1 = np.arange(2,9,2)
print(arange_1)

# np.linspace(1st number, last number,
# total divisions in the array)
linspace = np.linspace(0, 10, num=5)
print(linspace)

# Specifying data type of the array
# Default: float64
x = np.ones(2, dtype=np.int64)
print(x)