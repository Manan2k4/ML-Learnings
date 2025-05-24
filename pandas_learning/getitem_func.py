import pandas as pd
import numpy as np

dates = pd.date_range("20130101", periods=6)
print(dates,"\n")
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list("ABCD"))
print(df,"\n")

print(df["A"],"\n")

print(df[0:3],"\n")
print(df["20130102": "20130104"],"\n")