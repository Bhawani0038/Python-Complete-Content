# Pandas for Data Science & Data Analysis

## Complete Learning Roadmap

| Module                   | Topics                                                                   |
| ------------------------ | ------------------------------------------------------------------------ |
| 1. Pandas Fundamentals   | Introduction, installation, import, Series, DataFrame                    |
| 2. Creating Data         | Lists, dictionaries, NumPy arrays, CSV, Excel, JSON                      |
| 3. Inspecting Data       | `head()`, `tail()`, `shape`, `columns`, `dtypes`, `info()`, `describe()` |
| 4. Selecting Data        | Columns, rows, `loc`, `iloc`, boolean filtering                          |
| 5. Data Cleaning         | Missing values, duplicates, incorrect values, data types                 |
| 6. Data Transformation   | `apply()`, `map()`, `replace()`, `astype()`, string operations           |
| 7. Sorting & Ranking     | `sort_values()`, `sort_index()`, ranking                                 |
| 8. GroupBy               | `groupby()`, aggregation, multiple aggregations                          |
| 9. Aggregation           | `sum()`, `mean()`, `median()`, `count()`, `min()`, `max()`               |
| 10. Combining Data       | `concat()`, `merge()`, `join()`                                          |
| 11. Reshaping Data       | `pivot()`, `pivot_table()`, `melt()`                                     |
| 12. Date & Time          | `datetime`, date filtering, resampling                                   |
| 13. Text Data            | `str.lower()`, `contains()`, `replace()`, regex                          |
| 14. Categorical Data     | Categories, memory optimization                                          |
| 15. Advanced Indexing    | MultiIndex, hierarchical data                                            |
| 16. Statistical Analysis | Correlation, covariance, distributions                                   |
| 17. Data Analysis        | KPIs, trends, segmentation, outliers                                     |
| 18. Visualization        | Pandas with Matplotlib                                                   |
| 19. Performance          | Vectorization, memory usage, efficient operations                        |
| 20. Real Projects        | Sales, customers, healthcare, finance, e-commerce datasets               |

---

Pandas Fundamentals

## 1. What is Pandas?

**Pandas** is a Python library used for:

* Data manipulation
* Data cleaning
* Data analysis
* Data transformation
* Statistical analysis
* Working with CSV/Excel/JSON data
* Preparing data for Machine Learning
* Exploratory Data Analysis (EDA)

Typical workflow:

```text
Raw Data
   ↓
Pandas
   ↓
Clean Data
   ↓
Transform
   ↓
Analyze
   ↓
Visualize
   ↓
Machine Learning / Reporting
```

---

# 2. Installing Pandas

```bash
pip install pandas
```

Check installation:

```python
import pandas as pd

print(pd.__version__)
```

`pd` is the standard alias used for Pandas.

---

# 3. Pandas Data Structures

Pandas mainly provides two important data structures:

```text
Pandas
│
├── Series
│
└── DataFrame
```

### Series

One-dimensional data:

```text
10
20
30
40
```

### DataFrame

Two-dimensional tabular data:

```text
Name       Age    Salary
Amit       25     35000
Ravi       28     42000
Priya      24     38000
```

---

# 4. Pandas Series

A Series is similar to a single column in an Excel sheet.

```python
import pandas as pd

marks = pd.Series([75, 82, 68, 91, 88])

print(marks)
```

The left side is the **index**.

```text
Index    Value
  0        75
  1        82
  2        68
  3        91
  4        88
```

---

# 5. Accessing Series Values

```python
print(marks[0])
```

Output:

```text
75
```

Multiple values:

```python
print(marks[1:4])
```

Output:

```text
1    82
2    68
3    91
dtype: int64
```

---

# 6. Creating Series with Custom Index

```python
marks = pd.Series(
    [75, 82, 68],
    index=["Amit", "Ravi", "Priya"]
)

print(marks)
```

Output:

```text
Amit     75
Ravi     82
Priya    68
dtype: int64
```

Now:

```python
print(marks["Ravi"])
```

Output:

```text
82
```

---

# 7. DataFrame

A DataFrame is the most important Pandas structure for Data Science.

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Amit", "Ravi", "Priya", "Neha"],
    "age": [25, 28, 24, 27],
    "salary": [35000, 42000, 38000, 45000]
})

print(df)
```

Output:

```text
    name  age  salary
0   Amit   25   35000
1   Ravi   28   42000
2  Priya   24   38000
3   Neha   27   45000
```
# 8. DataFrame Columns

Get all column names:

```python
print(df.columns)
```

Output:

```text
Index(['name', 'age', 'salary'], dtype='object')
```

Select one column:

```python
print(df["name"])
```

Select multiple columns:

```python
print(df[["name", "salary"]])
```

Output:

```text
    name  salary
0   Amit   35000
1   Ravi   42000
2  Priya   38000
3   Neha   45000
```

---

# 9. Basic DataFrame Inspection

Use these commands as a compact first look at a DataFrame:

| Command | Purpose |
| --- | --- |
| `df.head()` / `df.tail()` | Preview first / last rows (`head(10)` shows 10 rows) |
| `df.shape` | Number of rows and columns |
| `df.columns` / `df.index` | Column names / row labels |
| `df.dtypes` / `df.info()` | Data types / structure and non-null counts |
| `df.describe()` | Summary statistics for numeric columns |
| `df.size` / `df.ndim` | Number of values / dimensions |

---
