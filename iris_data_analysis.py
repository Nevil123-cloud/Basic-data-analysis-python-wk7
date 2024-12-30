import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the Iris dataset
    from sklearn.datasets import load_iris
    iris_data = load_iris()
    iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    iris['species'] = iris_data.target

    # Display the first few rows
    print("First few rows of the dataset:")
    print(iris.head())

    # Explore the structure
    print("\nData types and missing values:")
    print(iris.info())
    print("\nMissing values:")
    print(iris.isnull().sum())

    # Clean the dataset (no missing values in this dataset)
    # If there were missing values, we could fill or drop them
    # iris.fillna(method='ffill', inplace=True)  # Example of filling missing values

except Exception as e:
    print(f"Error loading dataset: {e}")

# Task 2: Basic Data Analysis
# Compute basic statistics
print("\nBasic statistics of numerical columns:")
print(iris.describe())

# Group by species and compute mean of petal length
grouped_data = iris.groupby('species')['petal length (cm)'].mean()
print("\nMean petal length per species:")
print(grouped_data)

# Task 3: Data Visualization
# Set the style for seaborn
sns.set(style="whitegrid")

# Line chart (not applicable for this dataset, so we skip it)
# Bar chart for average petal length per species
plt.figure(figsize=(10, 6))
sns.barplot(x=grouped_data.index, y=grouped_data.values)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.xticks(ticks=[0, 1, 2], labels=iris_data.target_names)
plt.show()

# Histogram of sepal length
plt.figure(figsize=(10, 6))
sns.histplot(iris['sepal length (cm)'], bins=10, kde=True)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot for sepal length vs petal length
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='deep')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species', labels=iris_data.target_names)
plt.show()
