import numpy as np


# index pos:    0 1 2
arr = np.array([1,2,3])

# Accessing data at index pos 1
print(arr[1])

# Accessing data from index 0 to
# index 1 (index 2 always gets excluded)
print(arr[0:2])

# Accessing data from index 1 to last
print(arr[1:])

# Accessing data from 2nd-last element
# to last element
print(arr[-2:])

# ---------------------------------------------------

a = np.array([[1,  2,  3,  4], 
              [5,  6,  7,  8], 
              [9, 10, 11, 12]])

# Print all elements less than 5
print(a[a < 5])

# Print elements with value 5 and up
five_up = (a>=5)
print(a[five_up])

# Print elements divisible by 2
divisible_by_2 = a[a%2 == 0]
print(divisible_by_2)

# Print values between 2 and 11 using '&' operator
c = a[(a>2) & (a<11)]
print(c)

# Print T/F array of array 'a' 
# where a > 5 or a == 5
five_T_or_F = (a > 5) | (a == 5)
print(five_T_or_F)


# Return indexes where the condition gets true
b = np.nonzero(a < 5)
print(b)

# Print values from indexes found in nonzero()
values = a[b]
print(values)

# If target element doesn't exist in array, 
# then returned array of indices will be empty
not_there = np.nonzero(a==42)
print(not_there)

