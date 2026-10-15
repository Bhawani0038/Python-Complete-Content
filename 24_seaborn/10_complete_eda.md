# Complete EDA

Now we combine the Seaborn concepts into a **real Data Analysis / Data Science EDA workflow**.

The goal of EDA is not just to create charts. It is to answer questions such as:

* What does the data look like?
* Which variables are important?
* Are there outliers?
* How are variables related?
* Are there differences between groups?
* Are there missing values?
* What patterns should we investigate further?

---

# 10.1 EDA Workflow

A practical Seaborn EDA workflow:

```text
Load Data
   ↓
Understand Data
   ↓
Clean Data
   ↓
Univariate Analysis
   ↓
Categorical Analysis
   ↓
Bivariate Analysis
   ↓
Multivariate Analysis
   ↓
Correlation Analysis
   ↓
Find Patterns / Outliers
   ↓
Business / ML Insights
```

---

# 10.2 Load Dataset

For learning, use Seaborn's `tips` dataset:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

df.head()
```

---

# 10.3 Understand the Dataset

### Shape

```python
df.shape
```

### Columns

```python
df.columns
```

### Data types

```python
df.dtypes
```

### Information

```python
df.info()
```

### Statistics

```python
df.describe()
```

For categorical columns:

```python
df.describe(include="object")
```

---

# 10.4 Check Missing Values

```python
df.isnull().sum()
```

Percentage of missing values:

```python
df.isnull().mean() * 100
```

This should be one of the first checks in a real project.

---

# 10.5 Univariate Analysis

Univariate means:

> Analyze one variable at a time.

For numerical data:

```python
sns.histplot(
    data=df,
    x="total_bill",
    kde=True
)

plt.show()
```

Questions:

* Is the distribution normal?
* Is it skewed?
* Are there extreme values?
* Where are most observations concentrated?

---

# 10.6 Analyze Another Numerical Variable

```python
sns.histplot(
    data=df,
    x="tip",
    kde=True
)

plt.show()
```

We can also use:

```python
sns.boxplot(
    data=df,
    x="tip"
)

plt.show()
```

The boxplot helps identify potential outliers.

---

# 10.7 Categorical Analysis

First check category counts:

```python
df["day"].value_counts()
```

Visualize them:

```python
sns.countplot(
    data=df,
    x="day"
)

plt.show()
```

Similarly:

```python
sns.countplot(
    data=df,
    x="time"
)

plt.show()
```

This answers:

> How many observations belong to each category?

---

# 10.8 Category + Numerical Variable

Suppose we want to compare total bills across days.

```python
sns.boxplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.show()
```

This helps compare:

* Median
* Spread
* Outliers
* Distribution

across categories.

---

# 10.9 Add Individual Observations

A boxplot summarizes the data, but sometimes we want to see the actual observations.

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
    color="black",
    alpha=0.5
)

plt.show()
```

Now we see:

```text
Boxplot
   +
Individual observations
```

---

# 10.10 Bivariate Analysis

Bivariate means:

> Analyze the relationship between two variables.

For example:

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

Question:

> Does tip increase when the total bill increases?

---

# 10.11 Add a Regression Line

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

This gives us:

* Data points
* Regression line
* Confidence interval

It helps visually understand the relationship.

---

# 10.12 Add a Categorical Variable

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="time"
)

plt.show()
```

Now we can compare the relationship for:

* Lunch
* Dinner

---

# 10.13 Analyze Categories Together

```python
sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex"
)

plt.show()
```

This allows us to investigate:

> How does the distribution of total bills vary by day and sex?

---

# 10.14 Multivariate Analysis

For multiple numerical variables:

```python
sns.pairplot(
    df[
        [
            "total_bill",
            "tip",
            "size"
        ]
    ]
)

plt.show()
```

With a categorical variable:

```python
sns.pairplot(
    df,
    vars=[
        "total_bill",
        "tip",
        "size"
    ],
    hue="time"
)

plt.show()
```

This gives a quick overview of relationships.

---

# 10.15 Correlation Analysis

Select numerical columns:

```python
numeric_df = df.select_dtypes(
    include="number"
)
```

Calculate correlation:

```python
corr = numeric_df.corr()

corr
```

Visualize:

```python
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.show()
```

Example interpretation:

```text
Correlation close to +1
        ↓
Strong positive relationship

Correlation close to -1
        ↓
Strong negative relationship

Correlation close to 0
        ↓
Weak linear relationship
```

Correlation is useful for exploration, but **correlation alone does not establish causation**.

---

# 10.16 Distribution by Category

We can use `hue`:

```python
sns.histplot(
    data=df,
    x="total_bill",
    hue="time",
    kde=True
)

plt.show()
```

Now we can compare the distributions of lunch and dinner bills.

---

# 10.17 Faceted EDA

Use `FacetGrid` when you want separate plots for different groups.

```python
g = sns.FacetGrid(
    df,
    col="time",
    row="sex"
)

g.map_dataframe(
    sns.scatterplot,
    x="total_bill",
    y="tip"
)

plt.show()
```

This creates a grid like:

```text
                 Lunch       Dinner

Male            Plot         Plot

Female          Plot         Plot
```

This is useful when relationships may differ between groups.

---

# 10.18 Complete EDA Dashboard

We can combine multiple plots.

```python
fig, axes = plt.subplots(
    2,
    2,
    figsize=(14, 10)
)

# Distribution
sns.histplot(
    data=df,
    x="total_bill",
    kde=True,
    ax=axes[0, 0]
)
axes[0, 0].set_title("Total Bill Distribution")


# Relationship
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="time",
    ax=axes[0, 1]
)
axes[0, 1].set_title("Total Bill vs Tip")


# Category comparison
sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    ax=axes[1, 0]
)
axes[1, 0].set_title("Bill Distribution by Day")


# Correlation
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    ax=axes[1, 1]
)
axes[1, 1].set_title("Correlation Matrix")

plt.tight_layout()
plt.show()
```

This gives a compact **EDA dashboard**.

---

# 10.19 What to Look for During EDA

### Numerical variables

Check:

```text
Distribution
   ↓
Center
   ↓
Spread
   ↓
Skewness
   ↓
Outliers
```

Useful plots:

* `histplot()`
* `kdeplot()`
* `boxplot()`
* `ecdfplot()`

---

### Categorical variables

Check:

```text
Frequency
   ↓
Category imbalance
   ↓
Category vs numerical variable
```

Useful plots:

* `countplot()`
* `barplot()`
* `boxplot()`
* `violinplot()`

---

### Relationships

Check:

```text
Variable A
     ↓
Relationship
     ↓
Variable B
```

Useful plots:

* `scatterplot()`
* `regplot()`
* `lineplot()`
* `pairplot()`
* `heatmap()`

---

# 10.20 EDA → Machine Learning

For an ML project, Seaborn can help before model training.

Example:

```text
Raw Dataset
     ↓
Pandas Cleaning
     ↓
Seaborn EDA
     ↓
Understand Features
     ↓
Identify Outliers
     ↓
Check Relationships
     ↓
Feature Engineering
     ↓
Train/Test Split
     ↓
Model Training
     ↓
Evaluation
```

For example, in a house-price dataset:

```python
sns.scatterplot(
    data=df,
    x="sqft_area",
    y="price_lakh"
)

plt.show()
```

Then:

```python
sns.heatmap(
    df.select_dtypes("number").corr(),
    annot=True,
    fmt=".2f"
)

plt.show()
```

This gives an initial understanding of which numerical variables may have useful relationships with price.

---

# 10.21 Seaborn EDA Cheat Sheet

| Analysis                   | Recommended Plot |
| -------------------------- | ---------------- |
| Numerical distribution     | `histplot()`     |
| Smooth distribution        | `kdeplot()`      |
| Cumulative distribution    | `ecdfplot()`     |
| Category frequency         | `countplot()`    |
| Category average           | `barplot()`      |
| Outliers                   | `boxplot()`      |
| Distribution + density     | `violinplot()`   |
| Individual observations    | `stripplot()`    |
| Relationship               | `scatterplot()`  |
| Trend                      | `lineplot()`     |
| Regression relationship    | `regplot()`      |
| Multiple variables         | `pairplot()`     |
| Two-variable detailed view | `jointplot()`    |
| Correlation                | `heatmap()`      |
| Grouped plots              | `FacetGrid()`    |
| Custom pairwise grid       | `PairGrid()`     |

### Complete Seaborn EDA Mental Model

```text
                SEABORN EDA
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
   Distribution   Categories   Relationships
        │            │            │
   histplot       countplot    scatterplot
   kdeplot        barplot      regplot
   boxplot        boxplot      lineplot
        │            │            │
        └────────────┼────────────┘
                     ↓
              Multivariate
                     │
              pairplot()
              jointplot()
              heatmap()
                     ↓
                Faceting
                     │
               FacetGrid
               PairGrid
                     ↓
                 Insights
```
