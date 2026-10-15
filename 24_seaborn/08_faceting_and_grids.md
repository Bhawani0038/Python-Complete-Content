# Faceting & Plot Grids

Faceting means **splitting one dataset into multiple smaller plots** based on categories.

This is very useful in EDA when you want to compare relationships across groups.

---

## 8.1 What is Faceting?

Suppose we have:

```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

df.head()
```

We may want to see:

> Does the relationship between `total_bill` and `tip` change for different `time`, `sex`, or `smoker` groups?

Instead of creating separate plots manually, Seaborn can create a **grid of plots automatically**.

---

# 8.2 `FacetGrid`

`FacetGrid` creates multiple plots based on categorical columns.

### Basic Example

```python
g = sns.FacetGrid(df, col="time")

g.map_dataframe(
    sns.scatterplot,
    x="total_bill",
    y="tip"
)

plt.show()
```

This creates separate plots for:

* Lunch
* Dinner

Conceptually:

```text
              time
        ┌───────────────┐
        │               │
 Lunch  │   Scatter     │
        │               │
        └───────────────┘

        ┌───────────────┐
        │               │
 Dinner │   Scatter     │
        │               │
        └───────────────┘
```

---

# 8.3 `col`

`col` creates plots **side-by-side**.

Same example as [Basic Example](#basic-example) above.

Equivalent idea:

```text
             time
       Lunch          Dinner
        │               │
        ▼               ▼
    [ Plot 1 ]      [ Plot 2 ]
```

---

# 8.4 `row`

`row` creates plots **vertically**.

```python
g = sns.FacetGrid(df, row="time")

g.map_dataframe(
    sns.scatterplot,
    x="total_bill",
    y="tip"
)

plt.show()
```

Conceptually:

```text
[ Lunch Plot  ]

[ Dinner Plot ]
```

---

# 8.5 `row` + `col`

We can create a 2-dimensional grid.

```python
g = sns.FacetGrid(
    df,
    row="sex",
    col="time"
)

g.map_dataframe(
    sns.scatterplot,
    x="total_bill",
    y="tip"
)

plt.show()
```

Now:

```text
                 time
             Lunch       Dinner

Male        [ Plot ]    [ Plot ]

Female      [ Plot ]    [ Plot ]
```

This is extremely useful for comparing multiple groups.

---

# 8.6 Adding `hue`

`hue` adds another categorical dimension using colors.

```python
g = sns.FacetGrid(
    df,
    row="sex",
    col="time",
    hue="smoker"
)

g.map_dataframe(
    sns.scatterplot,
    x="total_bill",
    y="tip"
)

g.add_legend()

plt.show()
```

Now we are analyzing:

```text
sex
 ├── Male
 │    ├── Lunch
 │    └── Dinner
 │
 └── Female
      ├── Lunch
      └── Dinner

Inside each plot:
    smoker → color
```

This is a **multidimensional EDA visualization**.

---

# 8.7 `margin_titles=True`

Makes row and column labels easier to read.

```python
g = sns.FacetGrid(
    df,
    row="sex",
    col="time",
    hue="smoker",
    margin_titles=True
)

g.map_dataframe(
    sns.scatterplot,
    x="total_bill",
    y="tip"
)

g.add_legend()

plt.show()
```

---

# 8.8 Customizing FacetGrid

### Axis labels

```python
g.set_axis_labels(
    "Total Bill",
    "Tip"
)
```

### Titles

```python
g.set_titles(
    row_template="{row_name}",
    col_template="{col_name}"
)
```

### Add legend

```python
g.add_legend()
```

Complete example:

```python
g = sns.FacetGrid(
    df,
    row="sex",
    col="time",
    hue="smoker",
    margin_titles=True
)

g.map_dataframe(
    sns.scatterplot,
    x="total_bill",
    y="tip"
)

g.set_axis_labels("Total Bill", "Tip")
g.add_legend()

plt.show()
```

---

# 8.9 `map()` vs `map_dataframe()`

### `map()`

Used with column names:

```python
g.map(
    sns.scatterplot,
    "total_bill",
    "tip"
)
```

### `map_dataframe()`

Works naturally with Seaborn functions using:

```python
x="total_bill"
y="tip"
```

Example:

```python
g.map_dataframe(
    sns.scatterplot,
    x="total_bill",
    y="tip"
)
```

For modern Seaborn code, `map_dataframe()` is often convenient when working with named DataFrame columns.

---

# 8.10 `PairGrid`

`PairGrid` is used to create a **grid of relationships between multiple numerical variables**.

Example:

```python
df = sns.load_dataset("penguins")

g = sns.PairGrid(
    df,
    vars=["bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
)

g.map(sns.scatterplot)

plt.show()
```

You get relationships like:

```text
                 bill_length
                      │
       ┌──────────────┼──────────────┐
       │              │              │
       ▼              ▼              ▼

bill_length      bill_depth    flipper_length
```

---

# 8.11 Different Plots on Diagonal and Off-Diagonal

This is where `PairGrid` becomes powerful.

```python
g = sns.PairGrid(
    df,
    vars=[
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm"
    ]
)

g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)

plt.show()
```

Result:

```text
              X1          X2          X3

X1          Histogram   Scatter     Scatter

X2          Scatter     Histogram   Scatter

X3          Scatter     Scatter     Histogram
```

So:

* Diagonal → distribution
* Off-diagonal → relationship

---

# 8.12 Using `hue` with PairGrid

```python
g = sns.PairGrid(
    df,
    vars=[
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm"
    ],
    hue="species"
)

g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)

g.add_legend()

plt.show()
```

Now different penguin species are shown using different colors.

---

# 8.13 `PairGrid` vs `pairplot()`

`pairplot()` is the **simpler interface**.

```python
sns.pairplot(
    df,
    hue="species"
)
```

`PairGrid` gives more control.

```python
g = sns.PairGrid(
    df,
    hue="species"
)

g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)

g.add_legend()
```

### Difference

| Feature             | `pairplot()` | `PairGrid`   |
| ------------------- | ------------ | ------------ |
| Easy to use         | ✅            | Medium       |
| Automatic grid      | ✅            | ✅            |
| Custom diagonal     | Limited      | ✅            |
| Custom off-diagonal | Limited      | ✅            |
| Full control        | Medium       | High         |
| Best for            | Quick EDA    | Advanced EDA |

---

# 8.14 FacetGrid vs PairGrid

| Feature                 | `FacetGrid`      | `PairGrid`            |
| ----------------------- | ---------------- | --------------------- |
| Main purpose            | Compare groups   | Compare variables     |
| Uses categories         | ✅                | Optional              |
| Uses multiple variables | Possible         | Main purpose          |
| `row` / `col`           | ✅                | Not the main concept  |
| Pairwise relationships  | ❌                | ✅                     |
| EDA usage               | Group comparison | Multivariate analysis |

### Easy Mental Model

```text
FacetGrid
    ↓
"Split my data into groups"

PairGrid
    ↓
"Compare my variables with each other"
```

---

# 8.15 Practical EDA Example

Suppose we have a customer dataset:

```python
df = pd.DataFrame({
    "age": [22, 25, 28, 35, 40, 45],
    "income": [30, 35, 42, 60, 75, 90],
    "spending_score": [80, 75, 70, 55, 40, 30],
    "gender": ["F", "M", "F", "M", "F", "M"]
})
```

### Group comparison

```python
g = sns.FacetGrid(
    df,
    col="gender"
)

g.map_dataframe(
    sns.scatterplot,
    x="income",
    y="spending_score"
)

plt.show()
```

Question answered:

> Does the income vs spending relationship look different across genders?

### Variable relationship

```python
sns.pairplot(
    df,
    hue="gender"
)

plt.show()
```

Question answered:

> How are age, income and spending score related to each other?

---

# 8.16 Important Functions

| Function            | Purpose                            |
| ------------------- | ---------------------------------- |
| `FacetGrid()`       | Create grid based on categories    |
| `map()`             | Apply plotting function            |
| `map_dataframe()`   | Apply plot using DataFrame columns |
| `set_axis_labels()` | Set axis labels                    |
| `set_titles()`      | Customize facet titles             |
| `add_legend()`      | Add legend                         |
| `PairGrid()`        | Create pairwise variable grid      |
| `map_diag()`        | Plot diagonal                      |
| `map_offdiag()`     | Plot off-diagonal                  |
| `pairplot()`        | Easy PairGrid interface            |

### Key takeaway

```text
FacetGrid
    ↓
Categorical groups
    ↓
Multiple plots
    ↓
Compare groups

PairGrid
    ↓
Multiple numerical variables
    ↓
Pairwise plots
    ↓
Understand relationships
```

#
