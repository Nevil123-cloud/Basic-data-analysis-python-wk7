import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    # Load the Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target

    # Display the first few rows
    print("First few rows of the dataset:")
    print(df.head())

    # Explore the structure of the dataset
    print("\nData types and missing values:")
    print(df.info())
    print("\nMissing values:")
    print(df.isnull().sum())

    # Clean the dataset (if any missing values)
    df.fillna(df.mean(), inplace=True)

except Exception as e:
    print(f"Error loading dataset: {e}")

# Task 2: Basic Data Analysis
# Compute basic statistics
print("\nBasic statistics of numerical columns:")
print(df.describe())

# Group by species and compute mean of numerical columns
grouped = df.groupby('species').mean()
print("\nMean of numerical columns grouped by species:")
print(grouped)

# Task 3: Data Visualization
# Bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='sepal length (cm)', data=df)
plt.title('Average Sepal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length (cm)')
plt.legend(title='Species')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal length (cm)'], bins=10, kde=True)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='species', data=df)
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend(title='Species')
plt.show()

# Indicate completion
print("Data analysis and visualizations completed successfully.")
