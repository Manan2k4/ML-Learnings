from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle

# Sample data
data = pd.DataFrame({
    'age': [22,25,47,52],
    'salary': [30000,35000,80000,90000],
    'buy': [0,0,1,1]
})

X = data[['age', 'salary']]
y = data['buy']

model = LogisticRegression()
model.fit(X, y)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model,f)