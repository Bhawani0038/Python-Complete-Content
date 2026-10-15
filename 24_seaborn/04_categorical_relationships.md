# Categorical Relationship Plots

In Part 3, we learned how to compare categories using `countplot()`, `barplot()`, `boxplot()`, and `violinplot()`.

Now we will learn how to show **individual observations inside categories**.

We will continue with:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")
```

---

# 1. `stripplot()`

`stripplot()` displays individual observations for each category.

```python
sns.stripplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.show()
```

Instead of showing only an average or box, we can see the **actual observations**.

Conceptually:

```text
total_bill
   |
30 |       •
   |   •   • •
20 | • • • • •
   | • • • • •
10 | • • • •
   +----------------
      Thur Fri Sat Sun
```

This is useful when you want to understand:

> How are individual observations distributed within each category?

---

# 2. `stripplot()` with `hue`

```python
sns.stripplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex"
)

plt.show()
```

Now each observation is additionally categorized by `sex`.

```text
Day
 ↓
Individual bills
 ↓
Male / Female
```

---

# 3. Avoiding Overlap with `jitter`

When many observations have similar values, points can overlap.

```python
sns.stripplot(
    data=df,
    x="day",
    y="total_bill",
    jitter=True
)

plt.show()
```

`jitter=True` slightly spreads the points horizontally so that overlapping observations become easier to see.

---

# 4. `swarmplot()`

`swarmplot()` also displays individual observations, but it attempts to position points so they don't overlap.

```python
sns.swarmplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.show()
```

This can make the distribution of individual observations easier to inspect.

---

# 5. `stripplot()` vs `swarmplot()`

| Feature                       | `stripplot()`         | `swarmplot()`                    |
| ----------------------------- | --------------------- | -------------------------------- |
| Shows individual observations | Yes                   | Yes                              |
| Handles overlapping points    | Jitter                | Automatically positions points   |
| Speed                         | Generally faster      | Can be slower for large datasets |
| Good for                      | Large/simple datasets | Detailed distribution            |
| Shows exact observations      | Yes                   | Yes                              |

For a small/medium dataset, `swarmplot()` can be very useful.

---

# 6. Boxplot + Stripplot

A very useful EDA combination is:

```python
sns.boxplot(
    data=df,
    x="day",
    y="total_bill"
)

sns.stripplot(
    data=df,
    x="day",
    y="total_bill",
    color="black"
)

plt.show()
```

This gives us both:

```text
Boxplot
   ↓
Median + quartiles + outliers

Stripplot
   ↓
Individual observations
```

This combination is particularly useful when teaching or analyzing a dataset because you can see both the **statistical summary and raw observations**.

---

# 7. Boxplot + Swarmplot

Another useful combination:

```python
sns.boxplot(
    data=df,
    x="day",
    y="total_bill"
)

sns.swarmplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.show()
```

Now we see:

```text
Distribution
    +
Actual observations
```

---

# 8. `catplot()`

`catplot()` is a **figure-level categorical plotting function**.

It provides a common interface for several categorical plots.

For example:

```python
sns.catplot(
    data=df,
    x="day",
    y="total_bill",
    kind="box"
)

plt.show()
```

Equivalent conceptually to:

```python
sns.boxplot(
    data=df,
    x="day",
    y="total_bill"
)
```

But `catplot()` becomes especially useful when creating multiple categorical plots using faceting.

---

# 9. `catplot()` with `kind`

You can change the type of categorical plot using `kind`.

### Count

```python
sns.catplot(
    data=df,
    x="day",
    kind="count"
)

plt.show()
```

### Bar

```python
sns.catplot(
    data=df,
    x="day",
    y="total_bill",
    kind="bar"
)

plt.show()
```

### Box

Same example as [8. `catplot()`](#8-catplot) above.

### Violin

```python
sns.catplot(
    data=df,
    x="day",
    y="total_bill",
    kind="violin"
)

plt.show()
```

### Swarm

```python
sns.catplot(
    data=df,
    x="day",
    y="total_bill",
    kind="swarm"
)

plt.show()
```

---

# 10. `catplot()` with `col`

Suppose we want separate plots for lunch and dinner.

```python
sns.catplot(
    data=df,
    x="day",
    y="total_bill",
    col="time",
    kind="box"
)

plt.show()
```

This creates:

```text
              time

       Lunch             Dinner
   ┌─────────────┐   ┌─────────────┐
   │             │   │             │
   │   Boxplots  │   │   Boxplots  │
   │             │   │             │
   └─────────────┘   └─────────────┘
```

---

# 11. `catplot()` with `row`

We can also create plots vertically.

```python
sns.catplot(
    data=df,
    x="day",
    y="total_bill",
    row="time",
    kind="box"
)

plt.show()
```

Now the layout becomes:

```text
Lunch
┌───────────────────┐
│     Boxplots      │
└───────────────────┘

Dinner
┌───────────────────┐
│     Boxplots      │
└───────────────────┘
```

---

# 12. `catplot()` with `hue`

```python
sns.catplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex",
    kind="box"
)

plt.show()
```

This lets us compare:

```text
Day
 ↓
Sex
 ↓
Total bill distribution
```

---

# 13. Controlling Category Order

Suppose the categories appear in an order you don't want.

You can explicitly specify the order:

```python
order = ["Thur", "Fri", "Sat", "Sun"]

sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    order=order
)

plt.show()
```

This is important in production reports because category order should often follow a **business-defined order**, rather than alphabetical order.

---

# 14. Ordering by a Metric

Suppose we want to arrange days based on average bill.

First calculate the order:

```python
order = (
    df.groupby("day")["total_bill"]
      .mean()
      .sort_values()
      .index
)
```

Then:

```python
sns.barplot(
    data=df,
    x="day",
    y="total_bill",
    order=order
)

plt.show()
```

This creates a much more meaningful business visualization:

```text
Lowest average bill
        ↓
        ...
        ↓
Highest average bill
```

---

# 15. `native_scale`

For categorical plots, categorical values are normally positioned on a categorical axis.

With newer Seaborn versions, `native_scale=True` can be useful when the categorical variable is actually numeric or datetime and you want to preserve its native spacing.

Example:

```python
sns.stripplot(
    data=df,
    x="size",
    y="total_bill",
    native_scale=True
)

plt.show()
```

This is useful when treating numeric values as categories would otherwise hide meaningful spacing.

---

# 16. Practical EDA Pattern

A useful workflow for categorical analysis is:

### Step 1 — Count categories

```python
sns.countplot(
    data=df,
    x="day"
)

plt.show()
```

Question:

> How many observations are there in each category?

### Step 2 — Compare averages

```python
sns.barplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.show()
```

Question:

> Which category has the highest average value?

### Step 3 — Examine spread

```python
sns.boxplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.show()
```

Question:

> How much does the value vary?

### Step 4 — Examine individual observations

Same example as [4. `swarmplot()`](#4-swarmplot) above.

Question:

> Where are the actual observations concentrated?

---

# 17. Important Functions

| Function      | Purpose                                           |
| ------------- | ------------------------------------------------- |
| `stripplot()` | Show individual observations                      |
| `swarmplot()` | Show individual observations with reduced overlap |
| `catplot()`   | Figure-level interface for categorical plots      |
| `order`       | Control category order                            |
| `hue`         | Split categories using another variable           |
| `row`         | Create row-wise facets                            |
| `col`         | Create column-wise facets                         |

### Mental Model

```text
Categorical Analysis
        │
        ├── How many?
        │      └── countplot()
        │
        ├── What is the average?
        │      └── barplot()
        │
        ├── What is the spread?
        │      └── boxplot()
        │
        ├── What is the distribution?
        │      └── violinplot()
        │
        └── Where are individual observations?
               ├── stripplot()
               └── swarmplot()
```
