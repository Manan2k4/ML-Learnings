import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "one": pd.Series(np.random.randn(3), index = ["a", "b", "c"]),
        "two": pd.Series(np.random.randn(4), index = ["a", "b", "c", "d"]),
        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
    }
)
print(df,'\n')

print(df.mean(0),'\n')

print(df.mean(1),'\n')

print(df.sum(0, skipna = False), '\n')

print(df.sum(axis=1, skipna=True), '\n')

ts_stand = (df - df.mean()) / df.std()
print(ts_stand.std(), '\n')

xs_stand = df.sub(df.mean(1), axis=0).div(df.std(1), axis=0)
print(xs_stand.std(1), '\n')

print(df.cumsum())

