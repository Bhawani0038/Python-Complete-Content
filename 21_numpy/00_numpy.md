# NumPy Notes for Data Science & Data Analysis

## 1. What is NumPy?

**NumPy (Numerical Python)** is a Python library used for:

* Numerical calculations
* Working with arrays
* Mathematical/statistical operations
* Fast operations on large datasets
* Supporting libraries like **Pandas, Scikit-learn, Matplotlib**

```python
import numpy as np
```

---

## 2. NumPy Array

The main object in NumPy is the **ndarray**.

```python
arr = np.array([10, 20, 30, 40, 50])
```

Unlike a Python list, NumPy arrays are designed for **fast numerical operations**.

### Important properties

```python
arr.ndim     # Number of dimensions
arr.shape    # Size of each dimension
arr.size     # Total number of elements
arr.dtype    # Data type
```

Example:

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

Output:

```text
1
(5,)
5
int64
```

---

# 3. 1D and 2D Arrays

### 1D Array

```python
arr = np.array([10, 20, 30, 40])
```

Shape:

```text
(4,)
```

### 2D Array

Commonly used for **dataset-like numerical data**.

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

Shape:

```text
(2, 3)
```

Meaning:

```text
2 rows × 3 columns
```

---

# 4. Creating Arrays

### `arange()`

Useful for generating numerical sequences.

```python
np.arange(1, 11)
```

Output:

```text
[1 2 3 4 5 6 7 8 9 10]
```

With step:

```python
np.arange(0, 10, 2)
```

Output:

```text
[0 2 4 6 8]
```

### `linspace()`

Creates evenly spaced values between two numbers.

```python
np.linspace(0, 100, 5)
```

Output:

```text
[  0.  25.  50.  75. 100.]
```

Useful in:

* Data visualization
* Numerical analysis
* ML calculations

---

# 5. Important Array Operations

NumPy allows calculations on the **whole array at once**.

```python
marks = np.array([50, 60, 70, 80])

marks + 5
```

Output:

```text
[55 65 75 85]
```

Other operations:

```python
marks * 2
marks / 2
marks - 10
```

This is called **vectorized operation**.

---

# 6. Statistical Functions

These are especially important for **Data Science and Data Analysis**.

```python
data = np.array([10, 20, 30, 40, 50])
```

### Mean

```python
np.mean(data)
```

### Median

```python
np.median(data)
```

### Standard Deviation

```python
np.std(data)
```

### Variance

```python
np.var(data)
```

### Minimum

```python
np.min(data)
```

### Maximum

```python
np.max(data)
```

### Sum

```python
np.sum(data)
```

### Percentile

```python
np.percentile(data, 75)
```

These functions are frequently used during **EDA and statistical analysis**.

---

# 7. Axis — Very Important for Data Analysis

Consider:

```python
data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

### Column-wise calculation

```python
np.mean(data, axis=0)
```

Output:

```text
[25. 35. 45.]
```

### Row-wise calculation

```python
np.mean(data, axis=1)
```

Output:

```text
[20. 50.]
```

Remember:

| Axis     | Works Across | Common Meaning |
| -------- | ------------ | -------------- |
| `axis=0` | Rows         | Column-wise    |
| `axis=1` | Columns      | Row-wise       |

---

# 8. Indexing

```python
data = np.array([10, 20, 30, 40, 50])
```

```python
data[0]
```

Output:

```text
10
```

```python
data[-1]
```

Output:

```text
50
```

---

# 9. Slicing

```python
data[1:4]
```

Output:

```text
[20 30 40]
```

For 2D data:

```python
data[:, 0]
```

Selects the **first column**.

```python
data[0, :]
```

Selects the **first row**.

---

# 10. Boolean Filtering

Very useful in **data analysis**.

```python
data = np.array([10, 25, 40, 15, 60])
```

```python
data[data > 30]
```

Output:

```text
[40 60]
```

Multiple conditions:

```python
data[(data > 20) & (data < 60)]
```

Output:

```text
[25 40]
```

---

# 11. Handling Missing Values

NumPy represents missing numerical values using `NaN`.

```python
data = np.array([10, 20, np.nan, 40])
```

Check missing values:

```python
np.isnan(data)
```

Output:

```text
[False False True False]
```

Count missing values:

```python
np.isnan(data).sum()
```

Output:

```text
1
```

Useful functions:

```python
np.nanmean(data)
np.nanmedian(data)
np.nansum(data)
np.nanmax(data)
np.nanmin(data)
```

These ignore `NaN` values.

---

# 12. Reshaping

Changing the structure without changing the data.

```python
data = np.array([1, 2, 3, 4, 5, 6])
```

```python
data.reshape(2, 3)
```

Result:

```text
[[1 2 3]
 [4 5 6]]
```

Important:

```python
6 elements → 2 × 3
```

The total number of elements must remain the same.

---

# 13. Flattening

Convert multidimensional data into 1D.

```python
data.flatten()
```

Example:

```text
[[1 2]
 [3 4]]
```

becomes:

```text
[1 2 3 4]
```

Useful when converting matrix-like data into a single feature/vector.

---

# 14. Combining Arrays

### `concatenate()`

```python
a = np.array([1, 2])
b = np.array([3, 4])

np.concatenate([a, b])
```

Output:

```text
[1 2 3 4]
```

For 2D data, `axis` controls whether rows or columns are combined.

---

# 15. Random Numbers

Important for:

* Sampling
* Simulation
* ML experimentation
* Creating test datasets

```python
np.random.seed(42)

data = np.random.randint(1, 101, 10)
```

Generate random floating-point values:

```python
np.random.rand(5)
```

Generate normally distributed values:

```python
np.random.normal(50, 10, 100)
```

---

# 16. Sorting

```python
data = np.array([50, 20, 80, 10, 40])

np.sort(data)
```

Output:

```text
[10 20 40 50 80]
```

Find indexes that would sort the array:

```python
np.argsort(data)
```

Useful when ranking or ordering numerical data.

---

# 17. Unique Values

Very useful for categorical/numerical analysis.

```python
data = np.array([10, 20, 10, 30, 20, 10])

np.unique(data)
```

Output:

```text
[10 20 30]
```

Frequency:

```python
values, counts = np.unique(data, return_counts=True)
```

---

# 18. Important NumPy Concepts for Data Science

Focus mainly on these:

| Topic                 | Importance |
| --------------------- | ---------- |
| `ndarray`             | Very High  |
| `shape`               | Very High  |
| `ndim`                | High       |
| `dtype`               | High       |
| Indexing              | Very High  |
| Slicing               | Very High  |
| Boolean filtering     | Very High  |
| Vectorization         | Very High  |
| `axis`                | Very High  |
| `reshape()`           | Very High  |
| Statistical functions | Very High  |
| `NaN` handling        | High       |
| `concatenate()`       | High       |
| `unique()`            | High       |
| Sorting               | High       |
| Random numbers        | High       |

### NumPy → Pandas → Scikit-learn relationship

```text
NumPy
  ↓
Numerical Arrays & Calculations
  ↓
Pandas
  ↓
Data Analysis / Data Cleaning
  ↓
Scikit-learn
  ↓
Machine Learning
```

# NumPy Notes — ML Calculations & Functions

These are the **NumPy concepts worth adding after basic arrays**, specifically because they are used to understand how Machine Learning algorithms work internally.

---

## 1. Mean Absolute Error — MAE

### Definition

MAE measures the **average absolute difference** between actual and predicted values.

### Formula

$$
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

Where:

- **$y_i$** = Actual value
- **$\hat{y}_i$** = Predicted value
- **$n$** = Number of observations

### NumPy Implementation

```python
import numpy as np

actual = np.array([100, 200, 300, 400])
predicted = np.array([110, 190, 320, 380])

mae = np.mean(np.abs(actual - predicted))

print(mae)
```

### Key NumPy functions

```text
np.abs()
np.mean()
```

### Practice Question

**Q1.** Given:

```python
actual = np.array([50, 60, 70, 80, 90])
predicted = np.array([55, 58, 72, 75, 95])
```

Calculate MAE using only NumPy.

---

# 2. Mean Squared Error — MSE

### Definition

MSE calculates the **average squared difference** between actual and predicted values.

### Formula

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

### NumPy Implementation

```python
mse = np.mean((actual - predicted) ** 2)

print(mse)
```

### Important

MSE gives **more penalty to large errors** because the errors are squared.

### Practice Question

**Q2.** Using the same `actual` and `predicted` arrays, calculate MSE using NumPy.

---

# 3. Root Mean Squared Error — RMSE

### Definition

RMSE is the square root of MSE.

### Formula

$$
RMSE = \sqrt{MSE}
$$

### NumPy Implementation

```python
rmse = np.sqrt(np.mean((actual - predicted) ** 2))

print(rmse)
```

### Why RMSE is useful?

If the target is measured in:

```text
₹
```

then:

```text
MSE  → ₹²
RMSE → ₹
```

So RMSE is easier to interpret because it is in the **same unit as the target**.

### Practice Question

**Q3.** Calculate RMSE for:

```python
actual = np.array([100, 120, 150, 180])
predicted = np.array([110, 115, 145, 170])
```

---

# 4. Maximum Error

Find the largest prediction error.

### Formula

$$
Maximum\ Error = max(|y-\hat y|)
$$

### NumPy

```python
max_error = np.max(np.abs(actual - predicted))
```

### Practice Question

**Q4.** Find the maximum prediction error for:

```python
actual = np.array([100, 200, 300, 400])
predicted = np.array([105, 180, 330, 390])
```

---

# 5. R² Score Using NumPy

R² measures how well predictions explain the variation in actual values.

### Formula

$$
R^2 = 1-\frac{SS_{res}}{SS_{tot}}
$$

Where:

$$
SS_{res}=\sum(y-\hat y)^2
$$

$$
SS_{tot}=\sum(y-\bar y)^2
$$

### NumPy Implementation

```python
actual = np.array([100, 200, 300, 400])
predicted = np.array([110, 190, 310, 390])

ss_res = np.sum((actual - predicted) ** 2)
ss_tot = np.sum((actual - np.mean(actual)) ** 2)

r2 = 1 - (ss_res / ss_tot)

print(r2)
```

### Practice Question

**Q5.** Calculate R² using NumPy for:

```python
actual = np.array([10, 20, 30, 40, 50])
predicted = np.array([12, 18, 29, 43, 48])
```

---

# 6. Min-Max Normalisation

Normalisation converts values into a fixed range, commonly **0 to 1**.

### Formula

$$
x' = \frac{x-x_{min}}{x_{max}-x_{min}}
$$

### NumPy Implementation

```python
data = np.array([10, 20, 30, 40, 50])

normalized = (
    (data - np.min(data)) /
    (np.max(data) - np.min(data))
)

print(normalized)
```

Output:

```text
[0.   0.25 0.5  0.75 1.  ]
```

### Practice Question

**Q6.** Normalize the following data between 0 and 1:

```python
data = np.array([25, 40, 60, 80, 100])
```

---

# 7. Standardisation — Z-Score

Standardisation converts data so that approximately:

```text
Mean = 0
Standard Deviation = 1
```

### Formula

$$
z = \frac{x-\mu}{\sigma}
$$

Where:

- **$x$** = Value
- **$\mu$** = Mean
- **$\sigma$** = Standard deviation

### NumPy Implementation

```python
data = np.array([10, 20, 30, 40, 50])

standardized = (
    (data - np.mean(data)) /
    np.std(data)
)

print(standardized)
```

### Practice Question

**Q7.** Standardise this data using NumPy:

```python
data = np.array([20, 25, 30, 35, 40])
```

Also verify that the resulting mean is approximately `0`.

---

# 8. Creating a Sigmoid Function

Sigmoid is widely used in **Logistic Regression** and neural networks.

### Formula

$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

### NumPy Function

```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
```

Use it:

```python
x = np.array([-2, -1, 0, 1, 2])

print(sigmoid(x))
```

Approximate output:

```text
[0.119 0.269 0.5   0.731 0.881]
```

### Important observation

```text
x → -∞    sigmoid → 0
x → 0     sigmoid → 0.5
x → +∞    sigmoid → 1
```

### Practice Question

**Q8.** Create a NumPy-based `sigmoid()` function and calculate sigmoid values for:

```python
x = np.array([-5, -2, 0, 2, 5])
```

---

# 9. Creating a ReLU Function

ReLU is widely used in neural networks.

### Formula

$$
ReLU(x)=max(0,x)
$$

### NumPy

```python
def relu(x):
    return np.maximum(0, x)
```

Example:

```python
x = np.array([-3, -1, 0, 2, 5])

print(relu(x))
```

Output:

```text
[0 0 0 2 5]
```

### Practice Question

**Q9.** Create a `relu()` function using NumPy and apply it to:

```python
x = np.array([-10, -5, 2, 7, -3, 8])
```

---

# 10. Mean Squared Error as a Custom Function

Instead of directly calculating MSE every time, create a reusable function.

```python
def mse(actual, predicted):
    return np.mean((actual - predicted) ** 2)
```

Usage:

```python
actual = np.array([100, 200, 300])
predicted = np.array([110, 190, 320])

print(mse(actual, predicted))
```

### Practice Question

**Q10.** Create your own NumPy functions for:

```text
MAE
MSE
RMSE
```

Then test all three using the same actual and predicted arrays.

---

# 11. Binary Classification Accuracy Using NumPy

Suppose:

```python
actual = np.array([1, 0, 1, 1, 0])
predicted = np.array([1, 0, 0, 1, 1])
```

Compare predictions:

```python
actual == predicted
```

Output:

```text
[ True  True False  True False]
```

Calculate accuracy:

```python
accuracy = np.mean(actual == predicted)

print(accuracy)
```

### Formula

$$
Accuracy = \frac{Correct\ Predictions}{Total\ Predictions}
$$

### Practice Question

**Q11.** Calculate classification accuracy using only NumPy:

```python
actual = np.array([1, 1, 0, 1, 0, 0, 1, 0])
predicted = np.array([1, 0, 0, 1, 1, 0, 1, 1])
```

---

# 12. NumPy `where()` — Useful for ML

`np.where()` can be used to convert probabilities into classes.

Suppose Logistic Regression produces:

```python
probabilities = np.array([0.2, 0.7, 0.4, 0.9, 0.6])
```

Use `0.5` as the classification threshold:

```python
predicted = np.where(probabilities >= 0.5, 1, 0)
```

Output:

```text
[0 1 0 1 1]
```

This is the basic idea behind converting **predicted probability → predicted class**.

### Practice Question

**Q12.** Convert these probabilities into binary classes using threshold `0.5`:

```python
probabilities = np.array([0.1, 0.8, 0.45, 0.72, 0.3, 0.95])
```


---

# Recommended NumPy → ML Practice Set



| No. | Question                      | Concept                 |
| --: | ----------------------------- | ----------------------- |
|   1 | Calculate MAE                 | `np.abs()`, `np.mean()` |
|   2 | Calculate MSE                 | Squaring + mean         |
|   3 | Calculate RMSE                | `np.sqrt()`             |
|   4 | Find Maximum Error            | `np.max()`              |
|   5 | Calculate R²                  | `np.sum()`, `np.mean()` |
|   6 | Perform Min-Max Normalisation | `min()`, `max()`        |
|   7 | Perform Standardisation       | Mean + Std              |
|   8 | Create Sigmoid Function       | `np.exp()`              |
|   9 | Create ReLU Function          | `np.maximum()`          |
|  10 | Create MAE/MSE/RMSE Functions | Custom functions        |
|  11 | Calculate Accuracy            | Boolean arrays          |
|  12 | Convert Probability to Class  | `np.where()`            |


