import numpy as np
import pandas as pd

index = pd.date_range("1/1/2000", periods=8)

s = pd.Series(np.random.randn(5), index = ["a", "b", "c", "d", "e"])
df = pd.DataFrame(np.random.randn(8, 3), index = index, columns = ["A", "B", "C"])
print(s,"\n")
print(df,"\n")

# Head(range if any) - Returns 1st 5 result,
# Tail(range if any) - Returns last 5 records
long_series = pd.Series(np.random.randn(1000))
print(long_series.head(),"\n")
print(long_series.tail(3),"\n")

# Print date rows from 0 to 1
print(df[:2])

# Changing case of headings, i.e.
# "A" to "a" and so on 
df.columns = [x.lower() for x in df.columns]
print(df)

# To get actual data inside index or series,
# use .array property
print(s.array)
print(s.index.array)

# Convert a pandas Series to numpy arrays
print(s.to_numpy())
print(np.asarray(s))

ser = pd.Series(pd.date_range("2000", periods=2, tz="CET"))

print(ser.to_numpy(dtype = object), "\n")
print(ser.to_numpy(dtype="datetime64[ns]"),"\n")

print(df.to_numpy())