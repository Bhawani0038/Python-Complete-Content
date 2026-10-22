# Seaborn Module — Part 3: Regression & Multivariate Plots

Parts 1 and 2 looked at single variables and simple pairs. This part moves to **fitted relationships** and to **many variables at once**. These plots are most useful during EDA before machine learning.

> Assumes the imports and `df = sns.load_dataset("tips")` from [Part 1](01_basics_and_relational_plots.md). Multivariate examples use `penguins`.

---

# A. Regression Plots

## 3.1 `regplot()` — Scatter + Fitted Line

```python
sns.regplot(data=df, x="total_bill", y="tip")
plt.show()
```

`regplot()` draws the scatter points from Part 1 plus a fitted **linear regression** line and a shaded **confidence interval** (CI):

```text
tip = β₀ + β₁ × total_bill
```

It answers: *is there a roughly linear relationship between bill and tip?*

Useful parameters:

| Parameter | Effect |
| --- | --- |
| `ci=95` (default) | Width of the confidence band; `ci=None` removes it |
| `order=2` | Fit a polynomial (`y = β₀ + β₁x + β₂x²`); `order=1` is linear |
| `logistic=True` | Fit a logistic curve; `y` must be binary (0/1) |
| `scatter_kws={"alpha": 0.5, "s": 50}` | Style the points |
| `line_kws={"linewidth": 3}` | Style the line |

```python
sns.regplot(
    data=df, x="total_bill", y="tip",
    order=2, ci=None,
    scatter_kws={"alpha": 0.5},
    line_kws={"color": "red"},
)
plt.show()
```

Logistic example (binary target):

```python
df["smoker_binary"] = (df["smoker"] == "Yes").astype(int)
sns.regplot(data=df, x="total_bill", y="smoker_binary", logistic=True)
plt.show()
```

## 3.2 `lmplot()` — Figure-level Regression

`lmplot()` is the figure-level version (see Part 1), so it supports `hue`, `col` and `row`.

```python
sns.lmplot(data=df, x="total_bill", y="tip", hue="sex", col="time")
plt.show()
```

```text
X = total_bill   Y = tip   Colour = sex   Panels = time
```

This fits a separate regression line for each group and answers: *does the bill–tip relationship differ between groups?*

| | `regplot()` | `lmplot()` |
| --- | --- | --- |
| Level | Axes-level (`ax=`) | Figure-level |
| `hue` / `col` / `row` | No (`hue` not supported) | Yes |
| Best for | One plot, custom subplots | Group comparisons |

## 3.3 Interpreting a Regression Plot

A house-price example with explicit values:

```python
house_df = pd.DataFrame({
    "sqft_area":  [850, 950, 1100, 1200, 1350, 1450, 1550, 1700],
    "price_lakh": [32,  38,  45,   48,   55,   62,   68,   76],
})

sns.regplot(data=house_df, x="sqft_area", y="price_lakh")
plt.show()
```

If points follow a rough straight line, **linear regression is worth trying**. The plot does not prove that it is the best model. Also watch for:

- Curved patterns (try `order=2`).
- Outliers that pull the line.
- A band that widens at the ends, which signals less certainty there.

---

# B. Multivariate Plots

## 3.4 `pairplot()` — Many Variables at Once

`pairplot()` creates a grid showing every pair of numeric columns. The diagonal shows each variable's own distribution; the other cells show pairwise scatter plots.

```python
pg = sns.load_dataset("penguins")

sns.pairplot(pg, hue="species")
plt.show()
```

```text
                 bill_length   bill_depth   body_mass
bill_length      [dist]        [scatter]    [scatter]
bill_depth       [scatter]     [dist]       [scatter]
body_mass        [scatter]     [scatter]    [dist]
```

Note: `penguins` contains missing values; `pairplot()` drops incomplete rows automatically.

Key parameters:

| Parameter | Use |
| --- | --- |
| `hue="species"` | Colour groups; shows whether groups separate |
| `vars=[...]` | Choose which columns to include (important for wide data) |
| `x_vars=[...]`, `y_vars=[...]` | Show only selected feature vs target panels |
| `diag_kind="hist"` or `"kde"` | Diagonal plot type |
| `kind="scatter"` or `"reg"` | Off-diagonal plot type; `"reg"` adds regression lines |

```python
sns.pairplot(
    pg,
    vars=["bill_length_mm", "bill_depth_mm", "body_mass_g"],
    hue="species",
    diag_kind="kde",
)
plt.show()
```

Tip: always select columns with `vars`. The grid grows with the square of the number of columns.

## 3.5 `jointplot()` — Two Variables in Depth

`jointplot()` shows one relationship in the centre and each variable's distribution along the edges.

```python
sns.jointplot(data=pg, x="bill_length_mm", y="body_mass_g", hue="species")
plt.show()
```

`kind` changes the centre plot:

| `kind` | Centre plot | Good for |
| --- | --- | --- |
| `"scatter"` (default) | Points | General use |
| `"reg"` | Points + regression line | Checking a linear trend |
| `"kde"` | 2D density contours | Seeing where data concentrates |
| `"hex"` | Hexagonal bins | Dense data with many overlapping points |

(`hue` works with `scatter` and `kde`, not with `reg`.)

**`pairplot()` vs `jointplot()`:** use `pairplot()` for a quick scan across many variables, and `jointplot()` once one pair looks interesting.

## 3.6 Correlation

Correlation measures the strength of a **linear** relationship between two numeric variables, from −1 to +1.

```python
numeric_df = pg.select_dtypes(include="number")
corr = numeric_df.corr()
print(corr.round(2))
```

```text
+1  strong positive linear relationship
 0  little or no linear relationship
-1  strong negative linear relationship
```

Two cautions:

- A value near 0 does not mean "no relationship". A curved relationship can have correlation near 0, so check the scatter plot too.
- Correlation does not prove causation.

## 3.7 `heatmap()` — Visualizing the Correlation Matrix

```python
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
plt.show()
```

| Parameter | Effect |
| --- | --- |
| `annot=True` | Print the value in each cell |
| `fmt=".2f"` | Show 2 decimal places |
| `cmap="coolwarm"` | Diverging colours: blue negative, red positive (suited to values centred on 0) |
| `vmin=-1, vmax=1` | Fix the colour scale to the full correlation range |
| `mask=...` | Hide cells |

A correlation matrix is symmetric (A↔B equals B↔A), so half of it is duplicate. Hide the upper triangle with a mask:

```python
import numpy as np

mask = np.triu(np.ones_like(corr, dtype=bool))      # hides upper triangle AND diagonal
sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
plt.show()
```

Use `np.triu(..., k=1)` if you want to keep the diagonal of 1.0 values visible.

> Heatmaps are good for initial exploration. They should not be the only reason to keep or drop a feature in an ML model.

---

## Recap

```text
Fitted line, one pair          -> regplot()
Fitted lines per group         -> lmplot(hue=, col=)
Quick scan of many variables   -> pairplot()
Detailed look at one pair      -> jointplot()
Numbers for all pairs          -> corr() + heatmap()
```
