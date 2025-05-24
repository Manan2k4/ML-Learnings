import numpy as np

data = np.array([1, 2])
ones = np.ones(2, dtype=int)

# [1, 2] + [1, 1] = [2, 3]
#  data  +  ones  =  final
sum = data + ones
print(sum)

# [1, 2] - [1, 1] = [0, 1]
#  data  -  ones  =  final
diff = data - ones
print(diff)

# [1, 2] * [1, 2] = [1, 4]
#  data  *  ones  =  final
prod = data * data
print(prod)

# [1, 2] / [1, 2] = [1., 1.]
#  data  /  ones  =  final
quotient = data / data
print(quotient)

a = np.array([1,2,3,4])
a_sum = a.sum()
print(a_sum)

b = np.array([[1,1], [2,2]])
b_sum = b.sum(axis=0)
print(b_sum)

