import numpy as np
import pandas as pd

series = pd.Series(np.random.randn(1000))

series[::2] = np.nan

frame = pd.DataFrame(np.random.randn(1000,5), columns=["a", "b", "c", "d", "e"])

frame.iloc[::2] = np.nan

# try:
#     print(frame.describe())
# except Exception as e:
#     print("Error: ", e)

print(frame.describe(include="all"))