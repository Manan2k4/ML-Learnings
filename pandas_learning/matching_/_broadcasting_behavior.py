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
print(df.sub(row, axis=1),'\n')
print(df.sub(column, axis="index"),'\n')
print(df.sub(column, axis=0),'\n')

dfmi = df.copy()
dfmi.index = pd.MultiIndex.from_tuples(
    [(1, "a"), (1, "b"), (1, "c"), (2, "a")], names=["first", "second"]
)

print(dfmi.sub(column, axis=0, level="second"))

s = pd.Series(np.arange(10))