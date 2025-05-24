# Copy
# it copies an array into another variable,
# any changes on original array will not affect copy

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42

# print(arr)
# print(x)

# ------------------------------------

# View
# It just returns what contains in original array,
# any changes on original array changes the view

# import numpy as np

# arr = np.array([1,2,3,4,5])
# x = arr.view()
# arr[0] = 42

# print(arr)
# print(x)

# -------------------------------------

# Make changes in View

# import numpy as np

# arr = np.array([1,2,3,4,5])
# x = arr.view()
# x[0] = 31

# print(arr)
# print(x)

# -------------------------------------

import numpy as np

arr = np.array([1,2,3,4,5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)