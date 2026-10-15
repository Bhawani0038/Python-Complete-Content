# Categorical Plots

Categorical plots are used when one or more variables contain **categories**, such as:

```text
Gender      → Male / Female
Smoker      → Yes / No
Day         → Thur / Fri / Sat / Sun
Department  → Sales / HR / IT
```

We will continue with the `tips` dataset.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")
```

---

# 1. `countplot()`

`countplot()` counts how many observations belong to each category.

For example, count customers by day:

```python
sns.countplot(
    data=df,
    x="day"
)

plt.show()
```

Conceptually:

```text
Day
│
│       █
│       █
│   █   █   █
│   █   █   █   █
└──────────────────
   Thur Fri Sat Sun
```

### When to use

Use `countplot()` when you want to answer:

> How many records belong to each category?

Examples:

```python
sns.countplot(data=df, x="sex")
```

```python
sns.countplot(data=df, x="smoker")
```

```python
sns.countplot(data=df, x="time")
```

---

# 2. `countplot()` with `hue`

We can further divide each category using another categorical variable.

```python
sns.countplot(
    data=df,
    x="day",
    hue="sex"
)

plt.show()
```

Now we can compare:

```text
Day
 ↓
Male vs Female
```

Another example:

```python
sns.countplot(
    data=df,
    x="day",
    hue="smoker"
)

plt.show()
```

This answers:

> How many smokers and non-smokers visited on each day?

---

# 3. Horizontal Countplot

Instead of:

```python
sns.countplot(
    data=df,
    x="day"
)
```

use:

```python
sns.countplot(
    data=df,
    y="day"
)

plt.show()
```

This is especially useful when category names are long.

---

# 4. `barplot()`

`barplot()` is different from `countplot()`.

It is generally used to show an **aggregate numerical value for each category**.

For example, average bill by day:

```python
sns.barplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.show()
```

By default, Seaborn estimates the mean of `total_bill` for each day.

Conceptually:

```text
Day       Average Bill
----------------------
Thur      ███████
Fri       █████
Sat       █████████
Sun       ████████
```

---

# 5. `barplot()` with `hue`

```python
sns.barplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex"
)

plt.show()
```

Now we can compare the average bill for males and females on each day.

---

# 6. `countplot()` vs `barplot()`

This distinction is extremely important.

| Function                           | Purpose                            |
| ---------------------------------- | ---------------------------------- |
| `countplot()`                      | Counts observations                |
| `barplot()`                        | Shows an aggregate numerical value |
| `countplot(x="day")`               | Number of records per day          |
| `barplot(x="day", y="total_bill")` | Average bill per day               |

Example:

```python
sns.countplot(data=df, x="day")
```

means:

> How many customers came on each day?

While:

```python
sns.barplot(
    data=df,
    x="day",
    y="total_bill"
)
```

means:

> What is the average bill for each day?

---

# 7. Custom Aggregation with `estimator`

By default, `barplot()` uses the **mean**.

We can change the aggregation.

For example, median:

```python
sns.barplot(
    data=df,
    x="day",
    y="total_bill",
    estimator="median"
)

plt.show()
```

Other aggregation functions can also be supplied.

For example:

```python
import numpy as np

sns.barplot(
    data=df,
    x="day",
    y="total_bill",
    estimator=np.sum
)

plt.show()
```

Now the bars represent the **total bill** instead of the average bill.

---

# 8. `boxplot()`

A box plot is extremely useful for understanding:

* Median
* Quartiles
* Spread
* Outliers

```python
sns.boxplot(
    data=df,
    y="total_bill"
)

plt.show()
```

Basic structure:

```text
        │
        │     ← Upper whisker
     ┌─────┐
     │     │
     │ ─── │ ← Median
     │     │
     └─────┘
        │
        │     ← Lower whisker
        •     ← Possible outlier
```

---

# 9. Boxplot by Category

Compare total bills across days:

```python
sns.boxplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.show()
```

This is much more informative than a simple bar chart when you want to understand **variation**.

---

# 10. Boxplot with `hue`

```python
sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex"
)

plt.show()
```

Now we can compare the distribution of bills across:

```text
Day
 ↓
Sex
 ↓
Total Bill
```

---

# 11. Why Boxplots Are Important in Data Science

Suppose you have:

```text
Salary
25000
28000
30000
32000
35000
38000
40000
250000
```

The value `250000` may be an outlier.

A boxplot can make this easier to identify.

```python
sns.boxplot(
    data=df,
    y="salary"
)

plt.show()
```

This is particularly useful during **outlier detection in EDA**.

---

# 12. `violinplot()`

A violin plot combines ideas from:

* Boxplot
* KDE/distribution

Example:

```python
sns.violinplot(
    data=df,
    y="total_bill"
)

plt.show()
```

By category:

```python
sns.violinplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.show()
```

The width of the violin represents the approximate **density of observations**.

---

# 13. Violinplot with `hue`

```python
sns.violinplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex"
)

plt.show()
```

This lets us compare distributions across multiple categories.

---

# 14. Boxplot vs Violinplot

| Plot           | Best for                                |
| -------------- | --------------------------------------- |
| `boxplot()`    | Median, quartiles, outliers             |
| `violinplot()` | Distribution shape + summary statistics |
| `barplot()`    | Aggregated numerical value              |
| `countplot()`  | Category frequency                      |

A practical rule:

```text
Want COUNT?
    ↓
countplot()

Want AVERAGE / AGGREGATE?
    ↓
barplot()

Want OUTLIERS + QUARTILES?
    ↓
boxplot()

Want DISTRIBUTION SHAPE?
    ↓
violinplot()
```

---

# 15. Real EDA Example

Suppose we want to analyze restaurant data.

### Question 1: Which day has the most customers?

Same example as [1. `countplot()`](#1-countplot) above.

### Question 2: Which day has the highest average bill?

Same example as [4. `barplot()`](#4-barplot) above.

### Question 3: Which day has more variation in bills?

Same example as [9. Boxplot by Category](#9-boxplot-by-category) above.

### Question 4: What does the bill distribution look like?

Same example as [12. `violinplot()`](#12-violinplot) above.

---

# 16. Important Categorical Functions

```text
Categorical Data
       │
       ├── countplot()
       │       └── Count categories
       │
       ├── barplot()
       │       └── Aggregate numerical values
       │
       ├── boxplot()
       │       └── Quartiles + outliers
       │
       └── violinplot()
               └── Distribution + summary
```

### Quick reference

| Function       | X        | Y       | Main Purpose          |
| -------------- | -------- | ------- | --------------------- |
| `countplot()`  | Category | —       | Frequency             |
| `barplot()`    | Category | Numeric | Aggregate             |
| `boxplot()`    | Category | Numeric | Distribution/outliers |
| `violinplot()` | Category | Numeric | Distribution shape    |
