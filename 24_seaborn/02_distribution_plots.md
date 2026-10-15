# Distribution Plots

Distribution plots help us understand **how numerical data is spread**.

We will use the `tips` dataset:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")

df.head()
```

---

## 1. `histplot()`

A histogram divides numerical values into intervals called **bins** and shows how many observations fall into each interval.

```python
sns.histplot(data=df, x="total_bill")

plt.show()
```

### With bins

```python
sns.histplot(
    data=df,
    x="total_bill",
    bins=10
)

plt.show()
```

More bins:

```python
sns.histplot(
    data=df,
    x="total_bill",
    bins=20
)

plt.show()
```

### `bins` intuition

```text
bins = 5

Data
 ↓
|----|----|----|----|----|
  1    2    3    4    5
```

* Fewer bins → simpler distribution
* More bins → more detailed distribution
* Too many bins → noisy visualization

---

# 2. Histogram with `hue`

We can compare distributions between categories.

```python
sns.histplot(
    data=df,
    x="total_bill",
    hue="sex"
)

plt.show()
```

Now we can compare:

```text
Total Bill
   ↓
Male distribution
Female distribution
```

---

# 3. Histogram with `kde`

`kde=True` adds a smooth **Kernel Density Estimate** curve.

```python
sns.histplot(
    data=df,
    x="total_bill",
    kde=True
)

plt.show()
```

The histogram shows the actual distribution using bins, while KDE provides a smooth estimate of the underlying distribution.

---

# 4. `stat` Parameter

By default, a histogram represents **count**.

```python
sns.histplot(
    data=df,
    x="total_bill",
    stat="count"
)

plt.show()
```

Other useful values include:

```python
stat="density"
stat="probability"
stat="percent"
stat="frequency"
```

### Probability

```python
sns.histplot(
    data=df,
    x="total_bill",
    stat="probability"
)

plt.show()
```

This represents each bin as a proportion of the observations.

---

# 5. `kdeplot()`

KDE gives a smooth representation of a numerical distribution.

```python
sns.kdeplot(
    data=df,
    x="total_bill"
)

plt.show()
```

This is useful when you want to focus on the **shape of the distribution** rather than individual bins.

---

## 6. KDE with `fill`

```python
sns.kdeplot(
    data=df,
    x="total_bill",
    fill=True
)

plt.show()
```

---

# 7. KDE with `hue`

```python
sns.kdeplot(
    data=df,
    x="total_bill",
    hue="sex"
)

plt.show()
```

This allows us to compare the distributions of `total_bill` for different sexes.

---

# 8. Histogram vs KDE

| Plot                 | Main Purpose                      |
| -------------------- | --------------------------------- |
| `histplot()`         | Frequency/distribution using bins |
| `kdeplot()`          | Smooth distribution estimate      |
| `histplot(kde=True)` | Histogram + KDE                   |

For EDA, a common approach is:

Same example as [3. Histogram with `kde`](#3-histogram-with-kde) above.

---

# 9. `ecdfplot()`

ECDF stands for **Empirical Cumulative Distribution Function**.

```python
sns.ecdfplot(
    data=df,
    x="total_bill"
)

plt.show()
```

It answers questions such as:

> What percentage of customers have a total bill less than or equal to ₹20?

Conceptually:

```text
X-axis → total_bill
Y-axis → cumulative proportion
```

If the curve reaches `0.70` at a particular bill value, approximately **70% of observations are at or below that value**.

---

# 10. `displot()`

`displot()` is a **figure-level function** for distribution visualization.

Histogram:

```python
sns.displot(
    data=df,
    x="total_bill",
    kind="hist"
)

plt.show()
```

KDE:

```python
sns.displot(
    data=df,
    x="total_bill",
    kind="kde"
)

plt.show()
```

ECDF:

```python
sns.displot(
    data=df,
    x="total_bill",
    kind="ecdf"
)

plt.show()
```

So:

```text
displot()
   |
   +-- kind="hist"
   |
   +-- kind="kde"
   |
   +-- kind="ecdf"
```

---

# 11. Distribution by Category

Suppose we want to see the distribution of bills separately for lunch and dinner.

```python
sns.displot(
    data=df,
    x="total_bill",
    col="time",
    kind="hist"
)

plt.show()
```

This creates separate plots:

```text
        Lunch              Dinner
     ┌─────────┐         ┌─────────┐
     │         │         │         │
     │  Hist   │         │  Hist   │
     │         │         │         │
     └─────────┘         └─────────┘
```

This is called **faceting**.

---

# 12. Distribution by `hue`

```python
sns.displot(
    data=df,
    x="total_bill",
    hue="time",
    kind="kde"
)

plt.show()
```

Now the distributions are separated by:

```text
time
 ├── Lunch
 └── Dinner
```

---

# 13. Practical EDA Example

Suppose we want to understand customer bills.

### Step 1 — Basic distribution

Same example as [3. Histogram with `kde`](#3-histogram-with-kde) above.

### Step 2 — Compare smokers

```python
sns.histplot(
    data=df,
    x="total_bill",
    hue="smoker",
    kde=True
)

plt.show()
```

### Step 3 — Compare lunch/dinner

Same example as [11. Distribution by Category](#11-distribution-by-category) above.

This progression is useful during **Exploratory Data Analysis**.

---

# 14. Important Distribution Functions

| Function         | Use                             |
| ---------------- | ------------------------------- |
| `sns.histplot()` | Histogram                       |
| `sns.kdeplot()`  | KDE distribution                |
| `sns.ecdfplot()` | Cumulative distribution         |
| `sns.displot()`  | Figure-level distribution plots |

### Remember

```text
Numerical Data
      ↓
Distribution
      ↓
 ┌──────────────┐
 │              │
Histogram      KDE
 │              │
Frequency      Shape
```

---

## What we covered

```text
histplot()
    ↓
bins
    ↓
hue
    ↓
kde=True
    ↓
stat
    ↓
kdeplot()
    ↓
ecdfplot()
    ↓
displot()
    ↓
Faceting with col
```
