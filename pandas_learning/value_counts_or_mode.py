import pandas as pd
import numpy as np

data = np.random.randint(0, 7, size = 50)
print(data)

s = pd.Series(data)

print(s.value_counts())

data = {"a": [1,2,3,4], "b": ["x","x","y","y"]}

frame = pd.DataFrame(data)

print(frame.value_counts())

s5 = pd.Series([1,1,3,3,3,5,5,7,7,7])

print(s5.mode())

df5 = pd.DataFrame(
    {
        "A": np.random.randint(0, 7, size=50),
        "B": np.random.randint(-10, 15, size=50),
    }
)

print(df5.mode())