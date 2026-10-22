# Seaborn Module — Part 5: Complete EDA

This final part ties everything together into one workflow. Each plot has already been explained in Parts 1–4, so this file only shows **when to use it and what to look for**.

The goal of EDA is not to make charts. It is to answer questions: What does the data look like? Are there missing values or outliers? Which variables matter? How are they related? Do groups differ?

## 5.1 EDA Workflow

```text
Load -> Understand -> Clean -> Univariate -> Categorical -> Bivariate -> Multivariate -> Correlation -> Insights
```

We use the `tips` dataset throughout.

## 5.2 Step 1 — Load and Understand the Data

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
df = sns.load_dataset("tips")

df.shape
df.dtypes
df.describe()                  # numeric columns
df.describe(include="object")  # text columns (use include=["object", "category"] if needed)
```

In `tips`, `day`, `sex`, `smoker` and `time` may be stored as `category` rather than `object`, so check `df.dtypes` before choosing the `describe` option.

## 5.3 Step 2 — Check Missing Values

```python
df.isnull().sum()
df.isnull().mean() * 100       # percentage missing per column
```

Do this early in every real project. Missing data changes how you plot and model. (`tips` has none, but `penguins` does.)

## 5.4 Step 3 — Univariate Analysis (one variable)

**Numeric:** distribution and outliers.

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.histplot(data=df, x="total_bill", kde=True, ax=axes[0])
sns.boxplot(data=df, x="total_bill", ax=axes[1])
plt.tight_layout()
plt.show()
```

Look at: centre, spread, skew (long tail to one side), and extreme values.

**Categorical:** how balanced are the categories?

```python
df["day"].value_counts()
sns.countplot(data=df, x="day")
plt.show()
```

## 5.5 Step 4 — Category vs Numeric

```python
sns.boxplot(data=df, x="day", y="total_bill")
sns.stripplot(data=df, x="day", y="total_bill", color="black", alpha=0.5)
plt.show()
```

Compare the median, spread and outliers across groups, and use the points to see how many observations support each box. A big difference in group size makes comparisons less reliable.

## 5.6 Step 5 — Bivariate Analysis (two numeric variables)

```python
sns.scatterplot(data=df, x="total_bill", y="tip", hue="time")
plt.show()

sns.regplot(data=df, x="total_bill", y="tip")
plt.show()
```

Look at: direction (positive/negative), strength, curvature, outliers, and whether groups (colours) behave differently.

## 5.7 Step 6 — Multivariate Analysis

```python
sns.pairplot(df, vars=["total_bill", "tip", "size"], hue="time")
plt.show()
```

To check group differences in detail, facet the plot:

```python
sns.lmplot(data=df, x="total_bill", y="tip", col="time", row="sex")
plt.show()
```

## 5.8 Step 7 — Correlation Analysis

```python
corr = df.select_dtypes(include="number").corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
plt.show()
```

Use it to spot strongly related variables (potentially useful features, or redundant ones). Remember: correlation measures linear association only, and it is not causation.

## 5.9 Final Dashboard

A compact summary of the analysis in one figure (technique from Part 4):

```python
numeric_df = df.select_dtypes(include="number")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.histplot(data=df, x="total_bill", kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Total Bill Distribution")

sns.scatterplot(data=df, x="total_bill", y="tip", hue="time", ax=axes[0, 1])
axes[0, 1].set_title("Total Bill vs Tip")

sns.boxplot(data=df, x="day", y="total_bill", ax=axes[1, 0])
axes[1, 0].set_title("Bill Distribution by Day")

sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm",
            vmin=-1, vmax=1, ax=axes[1, 1])
axes[1, 1].set_title("Correlation Matrix")

plt.tight_layout()
plt.show()
```

## 5.10 From EDA to Machine Learning

Seaborn belongs in the stage *before* modelling:

```text
Raw data -> Pandas cleaning -> Seaborn EDA -> feature understanding -> outliers & relationships
         -> feature engineering -> train/test split -> model -> evaluation
```

For a house-price dataset, a scatter plot of each feature against `price` plus a correlation heatmap gives an initial idea of which features may be useful. These plots are hints, not proof. Confirm with modelling and validation.

## 5.11 Cheat Sheet

| Goal | Function |
| --- | --- |
| Numeric distribution | `histplot()` (add `kde=True`) |
| Smooth shape / compare groups | `kdeplot()` |
| Cumulative proportion | `ecdfplot()` |
| Outliers and quartiles | `boxplot()` |
| Distribution shape per category | `violinplot()` |
| Category counts | `countplot()` |
| Category average / aggregate | `barplot()` |
| Individual points per category | `stripplot()`, `swarmplot()` |
| Two numeric variables | `scatterplot()` |
| Trend over ordered x | `lineplot()` |
| Fitted line | `regplot()`, `lmplot()` |
| Many variables | `pairplot()`, `PairGrid` |
| One pair in depth | `jointplot()` |
| Correlation matrix | `corr()` + `heatmap()` |
| Panels by group | `col=`/`row=`, `FacetGrid` |
| Layout and styling | `plt.subplots()`, `set_theme()`, `tight_layout()`, `savefig()` |

## 5.12 Practice Ideas

1. On `tips`, find which day has the highest average bill, then check with a boxplot whether that difference is meaningful or just a few outliers.
2. On `penguins`, find which pair of numeric features separates the three species best using `pairplot(hue="species")`.
3. Build your own 2×2 dashboard on `penguins` after handling missing values (`dropna()`).
4. Export the final dashboard as a 300 dpi PNG.
