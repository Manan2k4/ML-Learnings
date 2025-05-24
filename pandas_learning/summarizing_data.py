import numpy as np
import pandas as pd

series = pd.Series(np.random.randn(1000))

series[::2] = np.nan

series.describe()