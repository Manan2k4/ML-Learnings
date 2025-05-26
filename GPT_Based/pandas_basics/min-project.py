import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# Load data
df = pd.read_csv('Titanic-Dataset.csv')

# Preprocess
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Sex'] = df['Sex'].map({'male':0, 'female':1})
features = df[['Pclass', 'Sex', 'Age']]
target = df['Survived']

# Train & evaluate
X_train, X_test, y_train, y_test = train_test_split(features, target)
clf = LogisticRegression()
clf.fit(X_train, y_train)
print("Score: ", clf.score(X_test, y_test))