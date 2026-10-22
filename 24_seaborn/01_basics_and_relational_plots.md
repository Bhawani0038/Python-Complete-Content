# Seaborn Module — Part 1: Basics & Relational Plots

Seaborn is a Python visualization library built on top of Matplotlib. It works directly with Pandas DataFrames and provides high-level statistical plots, which makes it a standard tool for EDA (Exploratory Data Analysis).

## Module Roadmap

The module is split into five files. Each concept is taught fully in one place and only referenced elsewhere.

| File | Topics |
| --- | --- |
| **01 Basics & Relational Plots** (this file) | Setup, data format, axes-level vs figure-level, `scatterplot`, `lineplot`, `relplot` |
| [02 Distributions & Categorical Plots](02_distributions_and_categorical_plots.md) | `histplot`, `kdeplot`, `ecdfplot`, `displot`, `countplot`, `barplot`, `boxplot`, `violinplot`, `stripplot`, `swarmplot`, `catplot`, ordering |
| [03 Regression & Multivariate Plots](03_regression_and_multivariate_plots.md) | `regplot`, `lmplot`, `pairplot`, `jointplot`, correlation, `heatmap` |
| [04 Matplotlib, Styling & Grids](04_matplotlib_styling_and_grids.md) | Figure/Axes, subplots, themes, palettes, saving, `FacetGrid`, `PairGrid` |
| [05 Complete EDA](05_complete_eda.md) | End-to-end workflow, dashboard, cheat sheet |

Note: Matplotlib integration is taught *before* styling and grids (in file 04) because styling code relies on `fig` and `ax`.

---

## 1.1 Installation and Setup

```bash
pip install seaborn
```

Standard imports used throughout the module:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()   # applies Seaborn's default look to all plots
print(sns.__version__)
```

> Later files assume these imports and do not repeat them.

## 1.2 Data Format and Built-in Datasets

Seaborn works best with **tidy data**: one row per observation, one column per variable. Seaborn ships with practice datasets:

```python
df = sns.load_dataset("tips")   # restaurant bills
df.head()
```

```text
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No   Sun  Dinner     2
1       10.34  1.66    Male     No   Sun  Dinner     3
2       21.01  3.50    Male     No   Sun  Dinner     3
```

Inspect before plotting:

```python
df.shape          # rows, columns
df.info()         # dtypes and non-null counts
df.describe()     # numeric summary
```

Datasets used in this module: `tips` (most examples), `penguins` (multivariate), `fmri` (line plots).

## 1.3 The Standard Seaborn Call

Almost every function follows the same pattern:

```python
sns.plot_function(data=df, x="column1", y="column2", hue="column3")
plt.show()
```

Parameters you will see repeatedly:

| Parameter | Purpose |
| --- | --- |
| `data` | The DataFrame |
| `x`, `y` | Columns for the axes |
| `hue` | Colour by a variable |
| `style` | Marker/line style by a variable |
| `size` | Marker size by a variable |
| `palette` | Colour palette |
| `kind` | Plot type (figure-level functions) |
| `col`, `row` | Split into subplots (figure-level functions) |
| `ax` | Matplotlib Axes to draw on (axes-level functions) |

## 1.4 Axes-level vs Figure-level Functions

This is the most important design idea in Seaborn, and it explains why many plot types have two functions.

- **Axes-level** (e.g. `scatterplot`, `histplot`, `boxplot`): draws on *one* Matplotlib Axes. Accepts `ax=`. Easy to place inside your own subplot layout.
- **Figure-level** (e.g. `relplot`, `displot`, `catplot`, `lmplot`): creates its *own* figure and can split data into subplots using `col` and `row`. Accepts `kind=`, but **not** `ax=`.

| Plot family | Figure-level | Axes-level functions |
| --- | --- | --- |
| Relational | `relplot` | `scatterplot`, `lineplot` |
| Distribution | `displot` | `histplot`, `kdeplot`, `ecdfplot` |
| Categorical | `catplot` | `countplot`, `barplot`, `boxplot`, `violinplot`, `stripplot`, `swarmplot` |
| Regression | `lmplot` | `regplot` |

Rule of thumb: use axes-level for a single plot or a custom subplot layout; use figure-level when you want faceting (`col`/`row`).

---

## 1.5 Scatter Plot — `scatterplot()`

A scatter plot shows the relationship between **two numerical variables**.

```python
sns.scatterplot(data=df, x="total_bill", y="tip")
plt.show()
```

Question it answers: *does the tip increase when the bill increases?*

Seaborn can encode extra variables using `hue`, `style` and `size`:

```python
sns.scatterplot(
    data=df, x="total_bill", y="tip",
    hue="smoker",     # colour  -> smoker
    style="sex",      # shape   -> sex
    size="size",      # size    -> party size
)
plt.show()
```

This plot shows five variables at once. Use this carefully: more than two or three encodings quickly become hard to read.

## 1.6 Line Plot — `lineplot()`

A line plot shows how a value changes across an **ordered** variable, usually time.

```python
fmri = sns.load_dataset("fmri")

sns.lineplot(data=fmri, x="timepoint", y="signal")
plt.show()
```

The `fmri` data has many measurements per `timepoint`. By default, `lineplot()` **aggregates them**: the line is the mean, and the shaded band is a 95% confidence interval. This is different from `scatterplot()`, which draws every row.

Add `hue` to draw one line per group:

```python
sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event")
plt.show()
```

## 1.7 `relplot()` — Figure-level Relational Plot

`relplot()` draws either plot type through `kind=` and can facet:

```python
sns.relplot(data=df, x="total_bill", y="tip", kind="scatter", col="time")
plt.show()
```

```python
sns.relplot(data=fmri, x="timepoint", y="signal", kind="line", hue="event", col="region")
plt.show()
```

`scatterplot(...)` and `relplot(kind="scatter")` draw the same marks. The reason to choose `relplot` is the ability to split into panels with `col` and `row`.

## 1.8 Common Mistakes

- Using `lineplot()` on unordered categories. Lines imply order; use a categorical plot instead (file 02).
- Passing `ax=` to a figure-level function. It will fail; use the axes-level version.
- Forgetting that `lineplot()` aggregates repeated x-values. If you want raw points, use `scatterplot()`.
- Encoding too many variables in one scatter plot.

## Recap

```text
Two numeric variables              -> scatterplot()
Numeric change over ordered x      -> lineplot()
Same, but with col/row panels      -> relplot(kind=...)
Axes-level = one Axes (ax=)   |   Figure-level = whole figure (col/row)
```
