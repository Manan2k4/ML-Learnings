import numpy as np
import pandas as pd

s1 = pd.Series(np.random.randn(5))
print(s1)

print(s1.idxmin, s1.idxmax)