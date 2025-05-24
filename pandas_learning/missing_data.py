import numpy as np
import pandas as pd

dates = pd.date_range("20130101", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list("ABCD"))
print(df)

s1 = pd.Series([1,2,3,4,5,6], index = pd.date_range("20130102", periods=6))
print(s1,"\n")

df["F"] = s1

df1 = df.reindex(index = dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0]: dates[1], "E"] = 1

print(df1)

print(df1.dropna(how="any"))
print(df1.fillna(value = 5))

print(pd.isna(df1))