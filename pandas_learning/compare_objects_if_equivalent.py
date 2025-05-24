import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "one": pd.Series(np.random.randn(3), index = ["a", "b", "c"]),
        "two": pd.Series(np.random.randn(4), index = ["a", "b", "c", "d"]),
        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
    }
)

print(df+df == df*2, "\n")

print((df+df == df*2).all(), '\n')

print(np.nan == np.nan, '\n')

print((df+df).equals(df*2), '\n')

df1 = pd.DataFrame({"col": ["foo", 0, np.nan]})
df2 = pd.DataFrame({"col": [np.nan, 0, "foo"]}, index=[2,1,0])

print(df1.equals(df2), '\n')

print(df1.equals(df2.sort_index()), '\n')

# -------------------------------------------------------

# Comparing array-like objects

print(pd.Series(["foo", "bar", "baz"]) == "foo", '\n')

print(pd.Index(["foo", "bar", "baz"]) == "foo",'\n')

# Comparing Pandas Series with Pandas Index
print(pd.Series(["foo", "bar", "baz"]) == pd.Index(["foo", "bar", "qux"]), '\n')

# Comparing Pandas Series and with numpy array
print(pd.Series(["foo", "bar", "baz"]) == np.array(["foo", "bar", "qux"]))