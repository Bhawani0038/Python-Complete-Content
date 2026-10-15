# Regression Plots

Regression plots are useful for understanding the **relationship between numerical variables** and visualizing a fitted regression line.

They are particularly useful during:

* Exploratory Data Analysis
* Correlation analysis
* Linear regression preparation
* Feature vs target analysis
* Checking whether a linear relationship exists

We will use the `tips` dataset.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")
```

---

# 1. `regplot()`

The simplest regression plot:

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

It produces:

```text
              •
           •
        •     /
      •      /
   •       /
 •       /
──────────────
```

The line represents a fitted **linear regression model**.

Conceptually:

```text
tip = β₀ + β₁(total_bill)
```

So we are asking:

> Is there a linear relationship between total bill and tip?

---

# 2. Scatter Plot + Regression Line

You can think of `regplot()` as combining:

```text
Scatter Plot
     +
Regression Line
     +
Confidence Interval
```

For example:

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Total Bill vs Tip")

plt.show()
```

---

# 3. Confidence Interval

By default, Seaborn displays a confidence interval around the regression line.

You can control it with `ci`.

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip",
    ci=95
)

plt.show()
```

This represents a **95% confidence interval** around the estimated regression relationship.

You can change it:

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip",
    ci=68
)

plt.show()
```

Or remove it:

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip",
    ci=None
)

plt.show()
```

---

# 4. `scatter_kws`

You can customize the underlying scatter points using `scatter_kws`.

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip",
    scatter_kws={"s": 50}
)

plt.show()
```

For example, transparency:

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip",
    scatter_kws={"alpha": 0.5}
)

plt.show()
```

---

# 5. `line_kws`

You can customize the regression line using `line_kws`.

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip",
    line_kws={"linewidth": 3}
)

plt.show()
```

---

# 6. Polynomial Regression

`regplot()` can also fit polynomial relationships using `order`.

Linear:

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip",
    order=1
)

plt.show()
```

Polynomial:

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip",
    order=2
)

plt.show()
```

The model becomes conceptually:

```text
y = β₀ + β₁x + β₂x²
```

For degree 3:

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip",
    order=3
)

plt.show()
```

Conceptually:

```text
y = β₀ + β₁x + β₂x² + β₃x³
```

This is useful when the relationship isn't approximately linear.

---

# 7. `logistic=True`

`regplot()` can also visualize a logistic relationship.

For example, create a binary variable:

```python
df["smoker_binary"] = (
    df["smoker"] == "Yes"
).astype(int)
```

Now:

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="smoker_binary",
    logistic=True
)

plt.show()
```

The fitted curve represents a logistic relationship rather than ordinary linear regression.

This can be useful for visualizing relationships involving a binary target.

---

# 8. `lmplot()`

`lmplot()` is another important Seaborn regression function.

Basic usage:

```python
sns.lmplot(
    data=df,
    x="total_bill",
    y="tip"
)
```

It produces a regression plot similar to:

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip"
)
```

But there is an important difference:

* `regplot()` → axes-level
* `lmplot()` → figure-level

This makes `lmplot()` particularly useful when working with **facets**.

---

# 9. Regression by Category Using `hue`

One of the most useful `lmplot()` features is `hue`.

```python
sns.lmplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex"
)

plt.show()
```

Now separate regression relationships are estimated for:

```text
Male
Female
```

This allows us to ask:

> Is the relationship between bill and tip different for males and females?

---

# 10. Regression by `col`

We can create separate regression plots for each category.

```python
sns.lmplot(
    data=df,
    x="total_bill",
    y="tip",
    col="time"
)

plt.show()
```

This creates separate plots for:

```text
Lunch
Dinner
```

---

# 11. `hue` + `col`

We can combine both:

```python
sns.lmplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex",
    col="time"
)

plt.show()
```

Now the visualization has multiple dimensions:

```text
X       → total_bill
Y       → tip
Color   → sex
Panels  → time
```

This is one of the powerful features of Seaborn's figure-level functions.

---

# 12. `scatterplot()` vs `regplot()`

Compare:

### Scatter plot

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)
```

Shows:

```text
Individual observations
```

### Regression plot

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip"
)
```

Shows:

```text
Individual observations
+
Regression relationship
```

---

# 13. `regplot()` vs `lmplot()`

| Feature               | `regplot()`  | `lmplot()`             |
| --------------------- | ------------ | ---------------------- |
| Regression line       | Yes          | Yes                    |
| Scatter points        | Yes          | Yes                    |
| Polynomial regression | Yes          | Yes                    |
| `hue`                 | Not directly | Yes                    |
| `row` / `col`         | No           | Yes                    |
| Function level        | Axes-level   | Figure-level           |
| Best for              | Single plot  | Multiple/faceted plots |

---

# 14. Practical Data Science Example

Suppose we have a house-price dataset:

```python
house_df = pd.DataFrame({
    "sqft_area": [850, 950, 1100, 1200, 1350, 1450, 1550, 1700],
    "price_lakh": [32, 38, 45, 48, 55, 62, 68, 76]
})
```

We can visualize the relationship:

```python
sns.regplot(
    data=house_df,
    x="sqft_area",
    y="price_lakh"
)

plt.xlabel("Area (sqft)")
plt.ylabel("Price (Lakh)")
plt.title("House Area vs Price")

plt.show()
```

This helps answer:

> Does house price approximately increase linearly with area?

---

# 15. Regression Visualization Before ML

A practical ML workflow can use Seaborn like this:

```text
Dataset
   ↓
EDA
   ↓
Scatter Plot
   ↓
Regression Plot
   ↓
Check relationship
   ↓
Feature Engineering
   ↓
Train ML Model
```

For example:

```python
sns.regplot(
    data=house_df,
    x="sqft_area",
    y="price_lakh"
)

plt.show()
```

If the observations roughly follow a straight-line pattern, **linear regression may be a reasonable model to investigate**.

However, the plot alone does not prove that linear regression is the best model.

---

# 16. Important Regression Parameters

| Parameter     | Purpose                           |
| ------------- | --------------------------------- |
| `x`           | Independent variable              |
| `y`           | Dependent variable                |
| `data`        | DataFrame                         |
| `ci`          | Confidence interval               |
| `order`       | Polynomial degree                 |
| `logistic`    | Logistic regression visualization |
| `scatter_kws` | Customize points                  |
| `line_kws`    | Customize regression line         |
| `hue`         | Separate groups                   |
| `col`         | Separate panels                   |
| `row`         | Separate rows                     |

---

## Regression Plot Mental Model

```text
Numerical X + Numerical Y
          ↓
     scatterplot()
          ↓
Need regression relationship?
          ↓
       regplot()
          ↓
Need categories?
          ↓
       lmplot()
          ↓
     ┌────┴────┐
     ↓         ↓
   hue       row/col
     ↓         ↓
Compare     Faceted
groups      plots
```
