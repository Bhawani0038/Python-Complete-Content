# Seaborn Fundamentals & Relational Plots

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

Same example as [4. Basic Seaborn Syntax](#4-basic-seaborn-syntax) above.

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
