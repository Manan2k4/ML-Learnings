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

df2.loc["a", "three"] = 1.0
print(df)

print(df2)

print(df + df2)

print(df.add(df2, fill_value=0))