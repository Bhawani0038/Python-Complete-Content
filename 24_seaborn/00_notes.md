# Seaborn Complete Tutorial — Part 1

Seaborn is a Python visualization library built on top of Matplotlib. It is especially useful for **Data Analysis, EDA, and Data Science**, because it works naturally with Pandas DataFrames and provides high-level statistical plots. ([Seaborn][1])

## Complete Learning Roadmap

| Module                        | Topics                                                           |
| ----------------------------- | ---------------------------------------------------------------- |
| 1. Seaborn Fundamentals       | Introduction, installation, import, relationship with Matplotlib |
| 2. Dataset Preparation        | Pandas DataFrame, built-in datasets, `load_dataset()`            |
| 3. Relational Plots           | `scatterplot()`, `lineplot()`, `relplot()`                       |
| 4. Distribution Plots         | `histplot()`, `kdeplot()`, `ecdfplot()`, `displot()`             |
| 5. Categorical Plots          | `barplot()`, `countplot()`, `boxplot()`, `violinplot()`          |
| 6. Categorical Relationships  | `stripplot()`, `swarmplot()`, `catplot()`                        |
| 7. Regression Plots           | `regplot()`, `lmplot()`                                          |
| 8. Multivariate Visualization | `pairplot()`, `jointplot()`                                      |
| 9. Heatmaps                   | Correlation matrix, `heatmap()`                                  |
| 10. Styling                   | Themes, palettes, figure size, labels, legends                   |
| 11. Faceting                  | `FacetGrid`, `col`, `row`, `hue`                                 |
| 12. Matplotlib Integration    | `fig`, `ax`, `plt`, combining plots                              |
| 13. EDA with Seaborn          | Complete real-world EDA workflow                                 |
| 14. Practice                  | Data-analysis questions and projects                             |

This roadmap follows the major areas covered by the current Seaborn documentation: relational, distributional, categorical, regression, multi-plot grids, and figure aesthetics. ([Seaborn][2])

---

# 1. Installation

```bash
pip install seaborn
```

Check installation:

```python
import seaborn as sns

print(sns.__version__)
```

---

# 2. Import Seaborn

Standard industry convention:

```python
import seaborn as sns
```

Usually we also import Pandas and Matplotlib:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

A common setup is:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()
```

`set_theme()` applies Seaborn's plotting theme and also affects the underlying Matplotlib configuration. ([Seaborn][1])

---

# 3. Load a Built-in Dataset

Seaborn provides datasets that are useful for learning and experimentation.

For example:

```python
import seaborn as sns

df = sns.load_dataset("tips")

print(df.head())
```

Output:

```text
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No   Sun  Dinner     2
1       10.34  1.66    Male     No   Sun  Dinner     3
2       21.01  3.50    Male     No   Sun  Dinner     3
3       23.68  3.31    Male     No   Sun  Dinner     2
4       24.59  3.61  Female     No   Sun  Dinner     4
```

Check the structure:

```python
df.shape
```

```python
df.columns
```

```python
df.info()
```

```python
df.describe()
```

---

# 4. Basic Seaborn Syntax

Most Seaborn plots follow this pattern:

```python
sns.plot_function(
    data=df,
    x="column1",
    y="column2"
)
```

For example:

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

The important idea is:

```text
DataFrame
   ↓
Seaborn
   ↓
X variable + Y variable
   ↓
Visualization
```

---

# 5. Scatter Plot

A scatter plot is useful when you want to understand the relationship between **two numerical variables**. Seaborn's `scatterplot()` supports additional dimensions through parameters such as `hue`, `size`, and `style`. ([Seaborn][3])

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

### Interpretation

Here:

```text
X → total_bill
Y → tip
```

We can investigate:

> Does the tip increase when the total bill increases?

---

# 6. Scatter Plot with `hue`

`hue` allows another variable to control the color/category of observations.

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="smoker"
)

plt.show()
```

Now the visualization contains three variables:

```text
X      → total_bill
Y      → tip
Color  → smoker
```

This is one of the most useful Seaborn features for EDA. ([Seaborn][3])

---

# 7. Scatter Plot with `style`

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="smoker",
    style="sex"
)

plt.show()
```

Now:

```text
X       → total_bill
Y       → tip
Color   → smoker
Shape   → sex
```

Seaborn automatically maps categorical values to visual properties.

---

# 8. Line Plot

Line plots are particularly useful for showing how a numerical value changes across an ordered variable, especially time. ([Seaborn][3])

Example:

```python
df = sns.load_dataset("fmri")

sns.lineplot(
    data=df,
    x="timepoint",
    y="signal"
)

plt.show()
```

Basic interpretation:

```text
timepoint → X-axis
signal    → Y-axis
```

---

# 9. `relplot()`

Seaborn provides a higher-level function called `relplot()` for relational visualization.

It can create either a scatter plot or line plot:

```python
sns.relplot(
    data=df,
    x="timepoint",
    y="signal",
    kind="line"
)

plt.show()
```

For scatter:

```python
sns.relplot(
    data=df,
    x="timepoint",
    y="signal",
    kind="scatter"
)

plt.show()
```

`relplot()` is a **figure-level function**, while `scatterplot()` and `lineplot()` are **axes-level functions**. Figure-level functions are particularly useful when creating multiple related plots through faceting. ([Seaborn][2])

---

# 10. Important Seaborn Parameters

These parameters will appear repeatedly throughout the tutorial:

| Parameter | Purpose                 |
| --------- | ----------------------- |
| `data`    | DataFrame               |
| `x`       | X-axis column           |
| `y`       | Y-axis column           |
| `hue`     | Color based on variable |
| `style`   | Marker/line style       |
| `size`    | Size based on variable  |
| `palette` | Color palette           |
| `kind`    | Plot type               |
| `col`     | Create plots by columns |
| `row`     | Create plots by rows    |
| `ax`      | Matplotlib Axes object  |

For example:

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex",
    style="smoker",
    size="size"
)

plt.show()
```

Part 2: Distribution Plots

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

```python
sns.histplot(
    data=df,
    x="total_bill",
    kde=True
)

plt.show()
```

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

```python
sns.histplot(
    data=df,
    x="total_bill",
    kde=True
)

plt.show()
```

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

```python
sns.displot(
    data=df,
    x="total_bill",
    col="time",
    kind="hist"
)

plt.show()
```

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

# Part 3: Categorical Plots

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

```python
sns.countplot(
    data=df,
    x="day"
)

plt.show()
```

### Question 2: Which day has the highest average bill?

```python
sns.barplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.show()
```

### Question 3: Which day has more variation in bills?

```python
sns.boxplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.show()
```

### Question 4: What does the bill distribution look like?

```python
sns.violinplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.show()
```

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

# Part 4: Categorical Relationship Plots

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

```python
sns.catplot(
    data=df,
    x="day",
    y="total_bill",
    kind="box"
)

plt.show()
```

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

```python
sns.swarmplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.show()
```

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

# Seaborn Tutorial — Part 6: Multivariate Visualization

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

```python
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f"
)

plt.show()
```

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

```python
sns.pairplot(
    df,
    hue="species"
)

plt.show()
```

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

# Part 7: Styling & Customization

Seaborn provides several functions for controlling the **appearance, readability, and presentation** of visualizations.

The main topics:

```text
set_theme()
set_style()
set_context()
set_palette()
figure size
titles
labels
legends
axis limits
```

---

# 1. `set_theme()`

A common starting point for Seaborn projects is:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
```

Then:

```python
df = sns.load_dataset("tips")

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

`set_theme()` applies a consistent Seaborn/Matplotlib visual theme.

---

# 2. `set_style()`

Seaborn provides several built-in styles.

Common styles include:

```text
darkgrid
whitegrid
dark
white
ticks
```

### `darkgrid`

```python
sns.set_style("darkgrid")

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

### `whitegrid`

```python
sns.set_style("whitegrid")

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

### `white`

```python
sns.set_style("white")

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

### `ticks`

```python
sns.set_style("ticks")

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

---

# 3. Which Style to Use?

| Style       | Typical Use                   |
| ----------- | ----------------------------- |
| `darkgrid`  | General EDA                   |
| `whitegrid` | Business/data reports         |
| `dark`      | Dark-background visualization |
| `white`     | Clean presentation            |
| `ticks`     | Publication-style plots       |

A common EDA setup:

```python
sns.set_theme(style="whitegrid")
```

---

# 4. `set_context()`

`set_context()` controls the **scale of plot elements**, such as fonts and lines.

Available contexts:

```text
paper
notebook
talk
poster
```

### Notebook

```python
sns.set_context("notebook")
```

### Presentation

```python
sns.set_context("talk")
```

### Large presentation

```python
sns.set_context("poster")
```

For example:

```python
sns.set_theme(
    style="whitegrid",
    context="talk"
)

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

---

# 5. Figure Size

You can control the figure size using Matplotlib:

```python
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

The format is:

```python
figsize=(width, height)
```

For example:

```python
figsize=(12, 6)
```

means:

```text
Width  = 12 inches
Height = 6 inches
```

---

# 6. Titles

Use Matplotlib's `plt.title()`:

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.title("Total Bill vs Tip")

plt.show()
```

You can also use the axes object:

```python
ax = sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

ax.set_title("Total Bill vs Tip")

plt.show()
```

For production-style plotting, working with `ax` is often more flexible.

---

# 7. Axis Labels

```python
ax = sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")

plt.show()
```

You can also use:

```python
ax.set(
    xlabel="Total Bill",
    ylabel="Tip",
    title="Total Bill vs Tip"
)
```

---

# 8. Axis Limits

Use:

```python
plt.xlim()
plt.ylim()
```

For example:

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.xlim(0, 60)
plt.ylim(0, 12)

plt.show()
```

This restricts the visible range.

---

# 9. Color Palettes

Seaborn provides many built-in palettes.

```python
sns.color_palette()
```

You can specify a palette:

```python
sns.set_palette("deep")
```

Or directly:

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex",
    palette="Set2"
)

plt.show()
```

---

# 10. Common Palette Types

Some commonly used palettes:

```text
deep
muted
bright
pastel
dark
colorblind
Set1
Set2
Set3
viridis
magma
rocket
```

Example:

```python
sns.set_palette("colorblind")
```

For categorical visualizations:

```python
sns.barplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex",
    palette="Set2"
)

plt.show()
```

---

# 11. Sequential vs Diverging Palettes

This is important for data visualization.

### Sequential

Used when values progress from low → high.

Examples:

```text
viridis
magma
Blues
Greens
```

Example:

```python
sns.heatmap(
    df.select_dtypes("number").corr(),
    cmap="viridis"
)

plt.show()
```

### Diverging

Useful when values have a meaningful center, such as:

```text
negative ← 0 → positive
```

For example:

```python
sns.heatmap(
    df.select_dtypes("number").corr(),
    cmap="coolwarm",
    annot=True
)

plt.show()
```

---

# 12. Removing Spines

Seaborn provides:

```python
sns.despine()
```

Example:

```python
sns.set_theme(style="white")

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

sns.despine()

plt.show()
```

This removes unnecessary plot borders.

---

# 13. Rotating Axis Labels

Suppose category names are long.

```python
sns.countplot(
    data=df,
    x="day"
)

plt.xticks(rotation=45)

plt.show()
```

For more control:

```python
plt.xticks(rotation=45, ha="right")
```

This is especially useful for:

```text
Long product names
Long department names
Dates
City names
Categories
```

---

# 14. Legend Position

You can control the legend through Matplotlib.

```python
ax = sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex"
)

ax.legend(
    title="Gender",
    loc="upper left"
)

plt.show()
```

---

# 15. Removing the Legend

If the legend isn't needed:

```python
ax = sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex"
)

ax.legend_.remove()

plt.show()
```

---

# 16. Professional Plot Example

A clean reusable pattern:

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(
    style="whitegrid",
    context="notebook"
)

fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex",
    style="smoker",
    ax=ax
)

ax.set_title("Relationship Between Total Bill and Tip")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")

sns.despine()

plt.tight_layout()
plt.show()
```

Notice the use of:

```text
fig
ax
```

This becomes particularly important when building **multiple charts in a single figure**.

---

# 17. Why Use `ax`?

Instead of:

```python
sns.scatterplot(...)
plt.title(...)
```

you can explicitly work with an Axes object:

```python
fig, ax = plt.subplots()

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=ax
)

ax.set_title("Bill vs Tip")
```

This is more flexible because you can control exactly **which axes** the Seaborn plot belongs to.

---

# 18. `tight_layout()`

Use:

```python
plt.tight_layout()
```

before displaying or saving the figure.

It helps prevent:

* Overlapping labels
* Cut-off titles
* Crowded axes

Example:

```python
plt.tight_layout()
plt.show()
```

---

# 19. Saving a Seaborn Plot

Since Seaborn uses Matplotlib underneath, you can save the figure with:

```python
plt.savefig(
    "sales_analysis.png",
    dpi=300,
    bbox_inches="tight"
)
```

For example:

```python
fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(
    data=df,
    x="day",
    y="total_bill",
    ax=ax
)

ax.set_title("Average Bill by Day")

plt.tight_layout()

plt.savefig(
    "average_bill_by_day.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
```

For reports and presentations, `dpi=300` is commonly useful for raster images.

---

# 20. A Reusable Seaborn Configuration

For an EDA notebook:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(
    style="whitegrid",
    context="notebook"
)
```

Then individual plots can focus on the data:

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex"
)

plt.title("Total Bill vs Tip")
plt.tight_layout()
plt.show()
```

---

# 21. Important Styling Functions

| Function             | Purpose                   |
| -------------------- | ------------------------- |
| `sns.set_theme()`    | Global theme              |
| `sns.set_style()`    | Background/grid style     |
| `sns.set_context()`  | Scale of plot elements    |
| `sns.set_palette()`  | Default color palette     |
| `sns.despine()`      | Remove unnecessary spines |
| `plt.figure()`       | Create/configure figure   |
| `plt.subplots()`     | Create figure + axes      |
| `plt.tight_layout()` | Prevent layout overlap    |
| `plt.savefig()`      | Save visualization        |

---

# 22. Styling Mental Model

```text
                  Seaborn Styling
                        │
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
       Theme          Context       Palette
          │             │             │
     set_theme()   set_context()  set_palette()
          │
      set_style()
          │
          ↓
       Plot
          │
     ┌────┴────┐
     ↓         ↓
  Labels     Legend
     │         │
     └────┬────┘
          ↓
      tight_layout()
          ↓
      savefig()
```

# Multi-Plot Grids & Faceting

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

```python
g = sns.FacetGrid(df, col="time")

g.map_dataframe(
    sns.scatterplot,
    x="total_bill",
    y="tip"
)

plt.show()
```

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

# Part 9 — Matplotlib Integration with Seaborn

Seaborn is built on top of Matplotlib, so in real projects you will often use **both together**.

The basic pattern is:

```python
fig, ax = plt.subplots()

sns.scatterplot(data=df, x="x", y="y", ax=ax)

ax.set_title("My Plot")

plt.show()
```

---

## 9.1 Why Use Matplotlib with Seaborn?

Seaborn is excellent for:

* Creating attractive statistical plots
* Working with DataFrames
* Grouping using `hue`
* Statistical visualizations

Matplotlib gives more control over:

* Figure size
* Titles
* Axis labels
* Multiple plots
* Annotations
* Saving figures
* Subplot layouts

So a common workflow is:

```text
Pandas
   ↓
Data Preparation
   ↓
Seaborn
   ↓
Create Visualization
   ↓
Matplotlib
   ↓
Customize Visualization
```

---

# 9.2 `Figure` and `Axes`

This is one of the most important concepts.

```python
fig, ax = plt.subplots()
```

There are two objects:

### `fig`

The complete figure/canvas.

### `ax`

The individual plotting area.

Think:

```text
Figure
┌───────────────────────────────┐
│                               │
│        Axes                   │
│      ┌─────────────┐          │
│      │             │          │
│      │    Plot     │          │
│      │             │          │
│      └─────────────┘          │
│                               │
└───────────────────────────────┘
```

---

# 9.3 Passing `ax` to Seaborn

```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=ax
)

plt.show()
```

The important part is:

```python
ax=ax
```

It tells Seaborn:

> Draw this plot on this specific Matplotlib Axes.

---

# 9.4 Customize Using `ax`

Instead of:

```python
plt.title()
plt.xlabel()
plt.ylabel()
```

you can use:

```python
ax.set_title()
ax.set_xlabel()
ax.set_ylabel()
```

Example:

```python
fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=ax
)

ax.set_title("Total Bill vs Tip")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip Amount")

plt.show()
```

---

# 9.5 Multiple Subplots

This is where Matplotlib becomes especially useful.

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
```

This creates:

```text
┌────────────────┬────────────────┐
│                │                │
│    axes[0]     │    axes[1]     │
│                │                │
└────────────────┴────────────────┘
```

Now we can put different Seaborn plots into each Axes.

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=axes[0]
)

sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    ax=axes[1]
)

plt.tight_layout()
plt.show()
```

---

# 9.6 Two Rows and Two Columns

```python
fig, axes = plt.subplots(
    2,
    2,
    figsize=(12, 8)
)
```

Structure:

```text
┌───────────────┬───────────────┐
│   axes[0,0]    │   axes[0,1]   │
├───────────────┼───────────────┤
│   axes[1,0]    │   axes[1,1]   │
└───────────────┴───────────────┘
```

Example:

```python
fig, axes = plt.subplots(
    2,
    2,
    figsize=(12, 8)
)

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=axes[0, 0]
)

sns.histplot(
    data=df,
    x="total_bill",
    ax=axes[0, 1]
)

sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    ax=axes[1, 0]
)

sns.barplot(
    data=df,
    x="day",
    y="tip",
    ax=axes[1, 1]
)

plt.tight_layout()
plt.show()
```

This creates a small **EDA dashboard**.

---

# 9.7 Different Titles for Each Plot

```python
fig, axes = plt.subplots(
    1, 2,
    figsize=(12, 5)
)

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=axes[0]
)

axes[0].set_title("Bill vs Tip")

sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    ax=axes[1]
)

axes[1].set_title("Bill by Day")

plt.tight_layout()
plt.show()
```

---

# 9.8 Sharing Axes

Sometimes multiple plots should use the same axis scale.

```python
fig, axes = plt.subplots(
    1,
    2,
    figsize=(12, 5),
    sharey=True
)
```

`sharey=True` means both plots share the same Y-axis.

Similarly:

```python
sharex=True
```

shares the X-axis.

---

# 9.9 Combining Different Seaborn Plots

A practical EDA dashboard:

```python
fig, axes = plt.subplots(
    2,
    2,
    figsize=(14, 10)
)

# 1. Relationship
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=axes[0, 0]
)
axes[0, 0].set_title("Bill vs Tip")


# 2. Distribution
sns.histplot(
    data=df,
    x="total_bill",
    kde=True,
    ax=axes[0, 1]
)
axes[0, 1].set_title("Bill Distribution")


# 3. Category comparison
sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    ax=axes[1, 0]
)
axes[1, 0].set_title("Bill by Day")


# 4. Category average
sns.barplot(
    data=df,
    x="day",
    y="tip",
    ax=axes[1, 1]
)
axes[1, 1].set_title("Average Tip by Day")

plt.tight_layout()
plt.show()
```

This is a very common **Data Analyst / Data Scientist EDA pattern**.

---

# 9.10 Adding Annotations

Matplotlib can add text to a Seaborn plot.

```python
fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=ax
)

ax.annotate(
    "High Tip",
    xy=(45, 9),
    xytext=(50, 10)
)

plt.show()
```

This is useful for highlighting:

* Outliers
* Important points
* Maximum values
* Minimum values
* Business events

---

# 9.11 Rotate X-axis Labels

Useful when category names are long.

```python
fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(
    data=df,
    x="day",
    y="total_bill",
    ax=ax
)

ax.tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.show()
```

---

# 9.12 Removing Unnecessary Spines

```python
sns.despine()
```

Or with an Axes:

```python
sns.despine(ax=ax)
```

Example:

```python
fig, ax = plt.subplots()

sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    ax=ax
)

sns.despine(ax=ax)

plt.show()
```

---

# 9.13 Save the Final Visualization

Use:

```python
plt.savefig(
    "sales_analysis.png",
    dpi=300,
    bbox_inches="tight"
)
```

Example:

```python
fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=ax
)

ax.set_title("Total Bill vs Tip")

plt.tight_layout()

plt.savefig(
    "bill_vs_tip.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
```

---

# 9.14 Professional Visualization Pattern

For projects, this pattern is worth remembering:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="time",
    ax=ax
)

ax.set_title("Total Bill vs Tip")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")

sns.despine(ax=ax)

plt.tight_layout()
plt.show()
```

### Mental model

```text
plt.subplots()
      ↓
Create Figure + Axes
      ↓
Seaborn plot
      ↓
Pass ax=ax
      ↓
Customize with ax
      ↓
tight_layout()
      ↓
show() / savefig()
```

---

## Quick Reference

| Task                | Code                       |
| ------------------- | -------------------------- |
| Create figure       | `fig, ax = plt.subplots()` |
| Set size            | `figsize=(10, 6)`          |
| Use Seaborn on Axes | `ax=ax`                    |
| Title               | `ax.set_title()`           |
| X label             | `ax.set_xlabel()`          |
| Y label             | `ax.set_ylabel()`          |
| Multiple plots      | `plt.subplots(rows, cols)` |
| Rotate labels       | `ax.tick_params()`         |
| Remove spines       | `sns.despine(ax=ax)`       |
| Adjust layout       | `plt.tight_layout()`       |
| Save                | `plt.savefig()`            |

# Part 10 — Complete EDA with Seaborn

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
