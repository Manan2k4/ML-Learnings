import numpy as np
import pandas as pd

dates = pd.date_range("20130101", periods = 6)

df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list("ABCD"))
print(df,"\n")

s1 = pd.Series([1,2,3,4,5,6], index = pd.date_range("20130102", periods=6))
print(s1,"\n")

df["F"] = s1

df.at[dates[0], "A"] = 0
df.iat[0,1] = 0

df.loc[:, "D"] = np.array([5] * len(df))
print(df)

df2 = df.copy()
df2[df2 > 0] = -df2

print(df2)