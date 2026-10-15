# Multivariate Visualization

In this part, we will learn how to visualize relationships between **multiple numerical variables at once**.

Main functions:

```text
pairplot()
jointplot()
heatmap()
```

These are especially useful during **EDA before machine learning**.

---

# 1. `pairplot()`

Suppose our dataset has several numerical columns:

```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")

df.head()
```

Select numerical columns:

```python
sns.pairplot(
    df
)

plt.show()
```

`pairplot()` creates a grid showing relationships between multiple variables.

Conceptually:

```text
             bill   tip   size
        ┌─────────┬──────┬──────┐
bill    │   KDE   │  •   │  •   │
        ├─────────┼──────┼──────┤
tip     │    •    │ KDE  │  •   │
        ├─────────┼──────┼──────┤
size    │    •    │  •   │ KDE  │
        └─────────┴──────┴──────┘
```

The diagonal generally shows the distribution of each variable, while the off-diagonal cells show relationships between pairs.

---

# 2. `pairplot()` with Specific Columns

It is usually better to select the columns you actually need.

```python
sns.pairplot(
    df[
        [
            "bill_length_mm",
            "bill_depth_mm",
            "flipper_length_mm",
            "body_mass_g"
        ]
    ]
)

plt.show()
```

This avoids creating unnecessarily large visualizations.

---

# 3. `pairplot()` with `hue`

One of the most useful features is `hue`.

```python
sns.pairplot(
    df,
    hue="species"
)

plt.show()
```

Now the observations are separated by penguin species.

Conceptually:

```text
Numerical variables
        ↓
   pairwise plots
        ↓
     species
        ↓
Different groups
```

This helps identify whether groups have visibly different distributions or relationships.

---

# 4. `vars`

Instead of using every numerical column:

```python
sns.pairplot(
    df,
    vars=[
        "bill_length_mm",
        "bill_depth_mm",
        "body_mass_g"
    ],
    hue="species"
)

plt.show()
```

This is preferable for larger datasets.

---

# 5. `x_vars` and `y_vars`

You can control which variables appear on the X and Y axes.

```python
sns.pairplot(
    df,
    x_vars=["bill_length_mm", "bill_depth_mm"],
    y_vars=["body_mass_g"],
    hue="species"
)

plt.show()
```

This is useful when you only want to investigate selected feature-target relationships.

---

# 6. `diag_kind`

You can control what appears on the diagonal.

Histogram:

```python
sns.pairplot(
    df,
    hue="species",
    diag_kind="hist"
)

plt.show()
```

KDE:

```python
sns.pairplot(
    df,
    hue="species",
    diag_kind="kde"
)

plt.show()
```

---

# 7. `kind`

You can choose the type of relationship plot.

```python
sns.pairplot(
    df,
    kind="scatter"
)

plt.show()
```

Regression:

```python
sns.pairplot(
    df,
    kind="reg"
)

plt.show()
```

`kind="reg"` adds regression lines to the pairwise relationships.

---

# 8. When to Use `pairplot()`

`pairplot()` is useful when you have:

```text
Dataset
   ↓
Multiple numerical features
   ↓
Want quick visual EDA
   ↓
pairplot()
```

For example, in a house-price dataset:

```text
sqft_area
bedrooms
floors
distance
price
```

You could quickly inspect:

```text
sqft_area ↔ price
bedrooms  ↔ price
floors    ↔ price
distance  ↔ price
```

This can help identify potentially useful relationships before modeling.

---

# 9. `jointplot()`

`jointplot()` focuses on the relationship between **two variables**.

```python
sns.jointplot(
    data=df,
    x="bill_length_mm",
    y="body_mass_g"
)

plt.show()
```

It provides:

```text
          Y distribution
               │
               │
       • • •   │
     • • • •   │
   • • • • •   │
───────────────┼────── X distribution
```

So we get:

```text
Center → relationship between X and Y
Edges  → individual distributions
```

---

# 10. `jointplot()` with KDE

```python
sns.jointplot(
    data=df,
    x="bill_length_mm",
    y="body_mass_g",
    kind="kde"
)

plt.show()
```

This displays the density of the two-dimensional relationship.

---

# 11. `jointplot()` with Regression

```python
sns.jointplot(
    data=df,
    x="bill_length_mm",
    y="body_mass_g",
    kind="reg"
)

plt.show()
```

This combines:

```text
Scatter
+
Regression line
+
Marginal distributions
```

This is useful when investigating a specific feature relationship.

---

# 12. `jointplot()` with Hexbin

For datasets with many observations:

```python
sns.jointplot(
    data=df,
    x="bill_length_mm",
    y="body_mass_g",
    kind="hex"
)

plt.show()
```

A hexbin plot groups observations into hexagonal regions.

This can make dense datasets easier to interpret.

---

# 13. `pairplot()` vs `jointplot()`

| Function      | Variables | Main Purpose                      |
| ------------- | --------: | --------------------------------- |
| `pairplot()`  |      Many | Explore many relationships        |
| `jointplot()` |       Two | Deep analysis of one relationship |

Think:

```text
Many variables
     ↓
 pairplot()

Two variables
     ↓
 jointplot()
```

---

# 14. Correlation

Before using a heatmap, calculate correlation.

```python
numeric_df = df.select_dtypes(include="number")

corr = numeric_df.corr()

print(corr)
```

You may get something like:

```text
                    bill_length   bill_depth   body_mass
bill_length             1.00        -0.24        0.59
bill_depth             -0.24         1.00       -0.47
body_mass               0.59        -0.47        1.00
```

Correlation ranges approximately from:

```text
-1  ←────────  0  ────────→  +1
```

Interpretation:

```text
+1 → Strong positive linear relationship
 0 → Little/no linear relationship
-1 → Strong negative linear relationship
```

Correlation measures **linear association**, so a value near zero does not necessarily mean that two variables have no relationship.

---

# 15. `heatmap()`

A heatmap can make a correlation matrix much easier to read.

```python
corr = numeric_df.corr()

sns.heatmap(
    corr
)

plt.show()
```

---

# 16. Display Correlation Values

Use `annot=True`:

```python
sns.heatmap(
    corr,
    annot=True
)

plt.show()
```

Now each cell displays its correlation value.

---

# 17. Format Correlation Values

```python
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f"
)

plt.show()
```

For example:

```text
0.5874 → 0.59
-0.4732 → -0.47
```

This makes the heatmap easier to read.

---

# 18. `cmap`

You can select a color map:

```python
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.show()
```

For correlation matrices, diverging palettes are commonly useful because they visually distinguish negative and positive correlations.

---

# 19. Hide the Diagonal

The correlation matrix is symmetrical:

```text
A ↔ B
B ↔ A
```

So half of the matrix contains duplicate information.

Create a mask:

```python
import numpy as np

mask = np.triu(
    np.ones_like(corr, dtype=bool)
)
```

Then:

```python
sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    fmt=".2f"
)

plt.show()
```

This produces a cleaner correlation heatmap.

---

# 20. Practical ML EDA

Suppose:

```python
house_df = pd.read_csv("house_data.csv")
```

Select numerical columns:

```python
numeric_df = house_df.select_dtypes(
    include="number"
)
```

Calculate correlation:

```python
corr = numeric_df.corr()
```

Visualize:

Same example as [17. Format Correlation Values](#17-format-correlation-values) above.

You can then investigate relationships involving the target:

```text
sqft_area ─────────→ price
bedrooms  ─────────→ price
floors    ─────────→ price
distance  ─────────→ price
```

A correlation matrix is useful for **initial exploration**, but it should not be treated as proof that a feature should or should not be included in an ML model.

---

# 21. Complete EDA Example

A practical sequence:

### Distribution

```python
sns.histplot(
    data=df,
    x="body_mass_g",
    kde=True
)

plt.show()
```

### Individual relationship

```python
sns.scatterplot(
    data=df,
    x="bill_length_mm",
    y="body_mass_g",
    hue="species"
)

plt.show()
```

### Regression relationship

```python
sns.regplot(
    data=df,
    x="bill_length_mm",
    y="body_mass_g"
)

plt.show()
```

### Multiple relationships

Same example as [3. `pairplot()` with `hue`](#3-pairplot-with-hue) above.

### Correlation

```python
numeric_df = df.select_dtypes(include="number")

corr = numeric_df.corr()

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f"
)

plt.show()
```

---

# 22. Quick Reference

| Function      | Purpose                                     |
| ------------- | ------------------------------------------- |
| `pairplot()`  | Relationships among many variables          |
| `jointplot()` | Detailed relationship between two variables |
| `heatmap()`   | Matrix visualization                        |
| `corr()`      | Calculate correlation                       |
| `annot=True`  | Display values in heatmap                   |
| `fmt=".2f"`   | Format displayed numbers                    |
| `mask`        | Hide part of heatmap                        |
| `hue`         | Separate groups                             |

### Mental Model

```text
                    Seaborn EDA
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
  Distribution      Relationships     Correlation
        │                │                │
   histplot()       scatterplot()      corr()
   kdeplot()        regplot()          heatmap()
   displot()        pairplot()
                    jointplot()
```
