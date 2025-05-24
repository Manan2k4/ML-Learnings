import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "one": pd.Series(np.random.randn(3), index = ["a", "b", "c"]),
        "two": pd.Series(np.random.randn(4), index = ["a", "b", "c", "d"]),
        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
    }
)

print(df,"\n")

row = df.iloc[1]
print(row,"\n")
column = df["two"]
print(column,"\n")

print(df.sub(row, axis="columns"),'\n')