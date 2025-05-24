import numpy as np
import pandas as pd

dates = pd.date_range("20130101", periods = 6)

df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list("ABCD"))
print(df,"\n")

print(df.at[pd.Timestamp("2013-01-02"), "B"],"\n")
print(df.iat[1,1],"\n")
print(df.loc["2013-01-03"],"\n")
print(df.loc["2013-01-03", "C"],"\n")
print(df.iloc[2],"\n")
print(df.iloc[2,2],"\n")

# Selection by label
print(df.loc[dates[0]],"\n")
