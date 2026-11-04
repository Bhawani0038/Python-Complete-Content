# NumPy

NumPy (Numerical Python) is the base library for fast numerical work in Python. Pandas, Scikit-learn and Matplotlib are all built on top of it.

```text
NumPy (arrays, calculations) → Pandas (analysis, cleaning) → Scikit-learn (ML)
```

```python
import numpy as np
```

**Roadmap:** Part A covers array basics. Part B uses those basics to build ML calculations (error metrics, scaling, activation functions). Part C is the practice set.

---

# Part A — Array Basics

## 1. The ndarray

The main NumPy object is the **ndarray**: a grid of values of one type, built for fast vectorized math (unlike a Python list).

```python
arr = np.array([[10, 20, 30],
                [40, 50, 60]])

arr.ndim    # 2        -> number of dimensions
arr.shape   # (2, 3)   -> 2 rows x 3 columns
arr.size    # 6        -> total elements
arr.dtype   # int64    -> data type
```

A 1D array of 4 values has shape `(4,)`. A 2D array is the usual form for dataset-like data (rows = records, columns = features).

## 2. Creating Arrays

```python
np.arange(1, 11)        # [1 2 ... 10]       (stop is excluded)
np.arange(0, 10, 2)     # [0 2 4 6 8]        (with step)
np.linspace(0, 100, 5)  # [0. 25. 50. 75. 100.]  (5 evenly spaced values, stop included)
```

Use `arange` when you know the **step**, and `linspace` when you know **how many points** you want (plotting, numerical analysis).

## 3. Vectorized Operations

Operations apply to the whole array at once, with no loop.

```python
marks = np.array([50, 60, 70, 80])
marks + 5     # [55 65 75 85]
marks * 2     # [100 120 140 160]
marks / 2, marks - 10
```

## 4. Statistical Functions

```python
data = np.array([10, 20, 30, 40, 50])

np.mean(data)   
np.median(data)   
np.std(data)   
np.var(data)
np.min(data)    
np.max(data)      
np.sum(data)   
np.percentile(data, 75)
```

Note: `np.std` and `np.var` use the **population** formula by default (`ddof=0`). Pass `ddof=1` for the sample version.

## 5. Axis (very important)

`axis` decides the direction a function works in.

```python
data = np.array([[10, 20, 30],
                 [40, 50, 60]])

np.mean(data, axis=0)   # [25. 35. 45.]  -> column-wise (collapses rows)
np.mean(data, axis=1)   # [20. 50.]      -> row-wise (collapses columns)
```

| Axis | Collapses | Result is |
| --- | --- | --- |
| `axis=0` | rows | one value per column |
| `axis=1` | columns | one value per row |

## 6. Indexing and Slicing

```python
data = np.array([10, 20, 30, 40, 50])
data[0]      # 10
data[-1]     # 50
data[1:4]    # [20 30 40]   (stop excluded)
```

For 2D arrays use `[row, column]`:

```python
data2d[:, 0]   # first column
data2d[0, :]   # first row
```

## 7. Boolean Filtering

A condition creates a True/False mask; the mask selects the matching values.

```python
data = np.array([10, 25, 40, 15, 60])
data[data > 30]                    # [40 60]
data[(data > 20) & (data < 60)]    # [25 40]
```

Use `&` (and), `|` (or), `~` (not), and wrap each condition in parentheses. Python's `and`/`or` will not work here.

## 8. Missing Values (NaN)

```python
data = np.array([10, 20, np.nan, 40])

np.isnan(data)          # [False False True False]
np.isnan(data).sum()    # 1  -> count of missing values
np.nanmean(data)        # ignores NaN (also nanmedian, nansum, nanmax, nanmin)
```

Plain `np.mean(data)` returns `nan` if any value is missing.

## 9. Reshape and Flatten

```python
data = np.array([1, 2, 3, 4, 5, 6])
data.reshape(2, 3)      # [[1 2 3] [4 5 6]]
data.reshape(-1, 2)     # -1 lets NumPy work out that dimension -> shape (3, 2)

np.array([[1, 2], [3, 4]]).flatten()   # [1 2 3 4]
```

Reshape never changes data, so the total number of elements must stay the same (6 → 2×3 or 3×2).

## 10. Combining, Sorting, Unique

```python
np.concatenate([a, b])              # joins arrays; for 2D, axis=0 stacks rows, axis=1 joins columns

np.sort(data)                       # sorted copy
np.argsort(data)                    # indexes that would sort the array (useful for ranking)

np.unique(data)                     # sorted unique values
values, counts = np.unique(data, return_counts=True)   # frequency of each value
```

## 11. Random Numbers

Used for sampling, simulation and test data. Set a seed to get repeatable results.

```python
np.random.seed(42)
np.random.randint(1, 101, 10)     # 10 integers from 1 to 100
np.random.rand(5)                 # 5 floats in [0, 1)
np.random.normal(50, 10, 100)     # 100 values, mean 50, std 10
```

## 12. Priority Guide

| Importance | Topics |
| --- | --- |
| Very high | `ndarray`, `shape`, indexing, slicing, boolean filtering, vectorization, `axis`, `reshape`, statistical functions |
| High | `ndim`, `dtype`, NaN handling, `concatenate`, `unique`, sorting, random numbers |

---

# Part B — NumPy for ML Calculations

These show how ML algorithms work internally. All the error metrics below share the same two arrays, defined once:

```python
actual    = np.array([100, 200, 300, 400])
predicted = np.array([110, 190, 320, 380])
error = actual - predicted      # reused below
```

## 13. Regression Error Metrics

| Metric | Formula | NumPy |
| --- | --- | --- |
| **MAE** (average absolute error) | $\frac{1}{n}\sum \lvert y_i-\hat{y}_i\rvert$ | `np.mean(np.abs(error))` |
| **MSE** (average squared error) | $\frac{1}{n}\sum (y_i-\hat{y}_i)^2$ | `np.mean(error ** 2)` |
| **RMSE** | $\sqrt{MSE}$ | `np.sqrt(np.mean(error ** 2))` |
| **Max error** | $\max\lvert y-\hat y\rvert$ | `np.max(np.abs(error))` |

Where $y_i$ = actual value, $\hat{y}_i$ = predicted value, $n$ = number of observations.

- **MSE penalizes large errors more** because errors are squared.
- **RMSE is in the same unit as the target.** If the target is in ₹, MSE is in ₹² but RMSE is in ₹, so it is easier to interpret.

Reusable functions:

```python
def mae(a, p):  return np.mean(np.abs(a - p))
def mse(a, p):  return np.mean((a - p) ** 2)
def rmse(a, p): return np.sqrt(mse(a, p))
```

## 14. R² Score

R² shows how much of the variation in the actual values the predictions explain (1 is perfect; 0 is no better than predicting the mean).

$$
R^2 = 1-\frac{SS_{res}}{SS_{tot}},\quad SS_{res}=\sum(y-\hat y)^2,\quad SS_{tot}=\sum(y-\bar y)^2
$$

```python
ss_res = np.sum((actual - predicted) ** 2)
ss_tot = np.sum((actual - np.mean(actual)) ** 2)
r2 = 1 - ss_res / ss_tot
```

## 15. Feature Scaling

**Min-Max normalisation** rescales values to the range 0–1:

$$
x' = \frac{x-x_{min}}{x_{max}-x_{min}}
$$

**Standardisation (z-score)** gives mean ≈ 0 and standard deviation ≈ 1 ($\mu$ = mean, $\sigma$ = standard deviation):

$$
z = \frac{x-\mu}{\sigma}
$$

```python
data = np.array([10, 20, 30, 40, 50])

normalized   = (data - data.min()) / (data.max() - data.min())   # [0. 0.25 0.5 0.75 1.]
standardized = (data - data.mean()) / data.std()
```

## 16. Activation Functions

**Sigmoid** squashes any value into (0, 1). It is used in logistic regression and neural networks: large negative → near 0, `0` → 0.5, large positive → near 1.

**ReLU** keeps positive values and turns negatives into 0. It is common in neural networks.

$$
\sigma(x)=\frac{1}{1+e^{-x}} \qquad ReLU(x)=\max(0,x)
$$

```python
def sigmoid(x): return 1 / (1 + np.exp(-x))
def relu(x):    return np.maximum(0, x)

sigmoid(np.array([-2, -1, 0, 1, 2]))   # [0.119 0.269 0.5 0.731 0.881]
relu(np.array([-3, -1, 0, 2, 5]))      # [0 0 0 2 5]
```

`np.maximum` compares element by element. `np.max` returns a single largest value, so don't mix them up.

## 17. Classification: Accuracy and `np.where`

Comparing arrays gives a Boolean array. Its mean is the fraction of `True` values, which is exactly accuracy:

$$
Accuracy = \frac{Correct\ Predictions}{Total\ Predictions}
$$

```python
actual    = np.array([1, 0, 1, 1, 0])
predicted = np.array([1, 0, 0, 1, 1])

actual == predicted                 # [True True False True False]
np.mean(actual == predicted)        # 0.6
```

`np.where(condition, value_if_true, value_if_false)` turns probabilities into classes using a threshold:

```python
probabilities = np.array([0.2, 0.7, 0.4, 0.9, 0.6])
np.where(probabilities >= 0.5, 1, 0)    # [0 1 0 1 1]
```

---

# Part C — Practice Set

Use only NumPy.

| No. | Task | Data |
| --: | --- | --- |
| 1 | MAE | `actual=[50,60,70,80,90]`, `predicted=[55,58,72,75,95]` |
| 2 | MSE | same arrays as Q1 |
| 3 | RMSE | `actual=[100,120,150,180]`, `predicted=[110,115,145,170]` |
| 4 | Maximum error | `actual=[100,200,300,400]`, `predicted=[105,180,330,390]` |
| 5 | R² | `actual=[10,20,30,40,50]`, `predicted=[12,18,29,43,48]` |
| 6 | Min-max normalisation | `[25,40,60,80,100]` |
| 7 | Standardisation, then check mean ≈ 0 | `[20,25,30,35,40]` |
| 8 | `sigmoid()` function | `[-5,-2,0,2,5]` |
| 9 | `relu()` function | `[-10,-5,2,7,-3,8]` |
| 10 | Write `mae`, `mse`, `rmse` functions and test all three on one pair of arrays | your own arrays |
| 11 | Classification accuracy | `actual=[1,1,0,1,0,0,1,0]`, `predicted=[1,0,0,1,1,0,1,1]` |
| 12 | Probabilities to classes (threshold 0.5) | `[0.1,0.8,0.45,0.72,0.3,0.95]` |
