import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and preprocess again
df = pd.read_csv('Titanic-dataset.csv')
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Sex'] = df['Sex'].map({'male':0, 'female':1})

# Add readable labels for plots
df['SexLabel'] = df['Sex'].map({0:'Male', 1:'Female'})

# Plot settings
sns.set(style="whitegrid")

# 1. Survival count
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Survived')
plt.title('Survival count (0=No, 1=Yes)')

# 2. Survival by Sex
plt.figure(figize=(6,4))
sns.countplot(data=df, x='SexLabel', hue='Survived')
plt.title('Survival by gender')

# 3. Survival by passenger class
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Pclass', hue='Survived')
plt.title('Suvival by passenger Class')

# 4. Age distribution of survivors vs non-survivors
plt.figure(figsize=(8,5))
sns.histplot(data=df, x='Age', hue='Survived', kde=True, bins=30)
plt.title('Age distribution: Survived vs Not survived')

plt.show()