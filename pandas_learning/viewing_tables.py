import numpy as np
import pandas as pd

dates = pd.date_range("20130101", periods = 6)

df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list("ABCD"))

print(df.head)
print(df.tail(3))

print(df.index)
print(df.columns)

print(df.to_numpy())

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",     # Scalar broadcast applied to all rows
    }
)

print(df2.dtypes)
print(df2.to_numpy())
print(df.describe())
print(df.T)
print(df.sort_index(axis=1, ascending = False))
