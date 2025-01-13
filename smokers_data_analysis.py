import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: load data:
data = pd.read_csv("file_path")


df = pd.DataFrame(data)

# Step 2: Data Cleaning
# Check for missing values
df.isnull().sum()  # No missing values in this generated dataset

# Step 3: Data Exploration
# Summary statistics
print("\nSummary Statistics:\n", df.describe())

# Distribution of age
sns.histplot(df['age'], kde=True, bins=20, color='blue')
plt.title("Age Distribution of Smokers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Smoking habits by gender
sns.boxplot(data=df, x='sex', y='cigarettes_per_day', palette='Set2')
plt.title("Smoking Habits by Gender")
plt.xlabel("Gender")
plt.ylabel("Cigarettes per Day")
plt.show()

# Smoking habits by country
plt.figure(figsize=(12, 6))
sns.barplot(
    data=df.groupby('country')['cigarettes_per_day'].mean().reset_index(),
    x='country', y='cigarettes_per_day', palette='viridis'
)
plt.title("Average Cigarettes per Day by Country")
plt.xlabel("Country")
plt.ylabel("Average Cigarettes per Day")
plt.xticks(rotation=45)
plt.show()

# Smoking preference for weekdays vs weekends
smoking_days_count = df['smoking_days'].value_counts()
sns.barplot(x=smoking_days_count.index, y=smoking_days_count.values, palette='pastel')
plt.title("Smoking Days Preference")
plt.xlabel("Smoking Days")
plt.ylabel("Count")
plt.show()

# Step 4: Correlation Analysis
correlation_matrix = df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.show()
