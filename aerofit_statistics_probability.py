# Importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Load the dataset
df = pd.read_csv('https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/001/125/origin')

# Display basic statistics and information about the dataset
print(df.describe(include='all'))
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Display the first few rows of the dataset
print(df.head())

# Detect and handle outliers using IQR
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)
print(df[outliers != True])

# Replace infinite values with NaN and categorize income
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df['Income category'] = pd.cut(df['Income'], bins=3, labels=['low', 'medium', 'high'])

# Display frequency counts for different products
print(df['Product'].value_counts())

# Filter data by MaritalStatus and Gender and display counts
print(df[df['MaritalStatus'] == 'Single']['Product'].value_counts())
print(df[df['MaritalStatus'] == 'Partnered']['Product'].value_counts())
print(df[df['Gender'] == 'Male']['Product'].value_counts())
print(df[df['Gender'] == 'Female']['Product'].value_counts())

# Analyze Fitness by Gender and MaritalStatus
print(pd.crosstab(index=df['Gender'], columns=df['Fitness'], normalize=True, margins=True))
print(pd.crosstab(index=df['MaritalStatus'], columns=df['Fitness'], normalize=True, margins=True))

# Visualize Usage by Age Category
df['age_category'] = pd.cut(df['Age'], bins=[18, 26, 33, 40, 48], labels=['Teenage', 'Adult', 'Mid Thirties', 'Forties'])
fig, ax = plt.subplots(1, 1, figsize=(20, 5))
sns.boxplot(data=df, x='age_category', y='Usage', hue='Product', ax=ax)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Age Category', fontsize=20)
plt.ylabel('Usage', fontsize=20)
plt.grid()
plt.show()

# Analyze Usage by Age
print(pd.crosstab(index=df['Usage'], columns=df['Age'], normalize=True, margins=True))
fig, ax = plt.subplots(1, 1, figsize=(15, 5))
sns.barplot(data=df, x='Age', y='Usage', ax=ax)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Age', fontsize=20)
plt.ylabel('Usage', fontsize=20)
plt.legend(['Age', 'Usage'], loc='upper right', frameon=False, fontsize=15)
plt.grid()
plt.show()

# Analyze Usage by Product and Gender
print(pd.crosstab(index=df['Product'], columns=df['Gender'], normalize=True, margins=True))

# Analyze Usage by Miles and Gender
s = pd.crosstab(index=df['Miles'], columns=df['Gender'], normalize=True, margins=True))
print(s.head(15))
print(s.tail(5))

# Analyze Usage by Education
e = pd.crosstab(index=df['Education'], columns=df['Usage'], normalize=False, margins=True)
print(e)
e.plot.bar(rot=0)
plt.show()

# Filter data by Gender
males = df[df['Gender'] == 'Male']
females = df[df['Gender'] == 'Female']

# Analyze products for married individuals
married = df[df['MaritalStatus'] == 'Partnered']
use_m = married[married['Usage'] > 0]
use_m_sorted = use_m.sort_values(by='Usage', ascending=False)
tredmills = use_m.groupby(by='Product').agg('value_counts')
product = pd.DataFrame(tredmills).reset_index()

# Categorize income
def categorize_income(x):
    return 'Capable' if x > 2 * 2500 else 'Not capable'

product['Income category'] = product['Income'].apply(categorize_income)
print(product[product['Income category'] == 'Capable'])
