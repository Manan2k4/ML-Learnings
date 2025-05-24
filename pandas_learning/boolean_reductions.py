import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "one": pd.Series(np.random.randn(3), index = ["a", "b", "c"]),
        "two": pd.Series(np.random.randn(4), index = ["a", "b", "c", "d"]),
        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
    }
)

df2 = df.copy()

print((df>0).all(), "\n")

print((df>0).any(), "\n")

print((df>0).any().any(), "\n")

print(df.empty, "\n")

print(pd.DataFrame(columns=list("ABC")).empty)