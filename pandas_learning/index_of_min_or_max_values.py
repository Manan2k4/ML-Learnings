import numpy as np
import pandas as pd

s1 = pd.Series(np.random.randn(5))
print(s1)

print("(",s1.idxmin(), ", ", s1.idxmax(), ")")

df1 = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])
print(df1)

print(df1.idxmin(axis=0),'\n')
print(df1.idxmax(axis=1),'\n')

df3 = pd.DataFrame([2,1,1,3,np.nan], columns=["A"], index=list("edcba"))
print(df3,'\n')
print(df3["A"].idxmin(),'\n')