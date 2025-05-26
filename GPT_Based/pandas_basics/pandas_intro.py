import pandas as pd

# Load and save CSV
df = pd.read_csv('Database_Tables.csv')
df.to_csv('output.csv', index=False)

# Inspect data
df.head()
df.info()
df.describe()

# Handle missing values
df.isnull()
# df.dropna(inplace=True)
df.fillna(0, inplace=True)