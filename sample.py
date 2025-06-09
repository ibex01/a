## **Q1. Dataset Creation and Reading (10 Marks)**

### **(a) Create a CSV file named `iris_subset.csv`**

```csv
# Save this content as iris_subset.csv

SepalLength,SepalWidth,PetalLength,PetalWidth,Class
5.1,3.5,1.4,0.2,setosa
4.9,3.0,1.4,0.2,setosa
4.6,3.1,1.5,0.2,setosa
4.7,3.2,1.3,0.2,setosa
7.0,3.2,4.5,1.5,versicolor
6.4,3.2,4.5,1.5,versicolor
6.9,3.1,4.9,1.5,versicolor
6.3,3.3,6.0,2.5,virginica
7.1,3.0,5.9,2.1,virginica
6.3,2.9,5.6,1.8,virginica
```

---

### **(b) Python Program to Read and Display the CSV File**

```python
import pandas as pd

# Read the CSV file
df = pd.read_csv('iris_subset.csv')

# Display the entire dataset
print(df)
```

---

## **Q2(a). Statistical Analysis and Visualization (6 Marks)**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('iris_subset.csv')

# Calculate standard deviation of numerical features
std_values = df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']].std()
print("Standard Deviations:\n", std_values)

# Scatter plot: Sepal Length vs Sepal Width
plt.scatter(df['SepalLength'], df['SepalWidth'], c='blue', marker='o')
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.grid(True)
plt.show()
```

---

## **Q2(b). KNN Classification (4 Marks)**

```python
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv('iris_subset.csv')

# Features and target
X = df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
y = df['Class']

# Encode class labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# KNN model with k=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y_encoded)

# Predict class for new instance
new_sample = [[6.3, 2.8, 5.1, 1.5]]
predicted_class_index = knn.predict(new_sample)
predicted_class = le.inverse_transform(predicted_class_index)

print("Predicted Class:", predicted_class[0])
```

---
