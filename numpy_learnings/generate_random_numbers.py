import numpy as np

rng = np.random.default_rng()

randoms = rng.random((3,2))
print(randoms)

print(rng.integers(5, size = (2,4)))

