# Seaborn Module — Part 2: Distributions & Categorical Plots

Part 1 covered relationships between two numeric variables. This part answers two different questions:

- **Distribution plots:** how is one numeric variable spread?
- **Categorical plots:** how does a numeric value (or a count) differ across categories?

> Assumes the imports and `df = sns.load_dataset("tips")` from [Part 1](01_basics_and_relational_plots.md).

---

# A. Distribution Plots

## 2.1 Histogram — `histplot()`

A histogram splits values into intervals called **bins** and counts the observations in each.

```python
sns.histplot(data=df, x="total_bill", bins=20)
plt.show()
```

- Few bins give a simple but coarse picture.
- Many bins give detail but become noisy.

Useful options:

```python
sns.histplot(data=df, x="total_bill", hue="sex")                 # compare groups
sns.histplot(data=df, x="total_bill", kde=True)                  # add smooth KDE curve
sns.histplot(data=df, x="total_bill", stat="probability")        # proportions instead of counts
```

`stat` can be `"count"` (default), `"probability"`, `"percent"`, `"density"` or `"frequency"`. Use `"density"` or `"percent"` when comparing groups of different sizes.

## 2.2 KDE — `kdeplot()`

A **Kernel Density Estimate** is a smooth estimate of the distribution's shape. It removes the dependence on bin choice.

```python
sns.kdeplot(data=df, x="total_bill", hue="sex", fill=True)
plt.show()
```

| Plot | Best for |
| --- | --- |
| `histplot()` | Actual counts per bin |
| `kdeplot()` | Overall shape, easy group comparison |
| `histplot(kde=True)` | Both together (a good default for EDA) |

## 2.3 ECDF — `ecdfplot()`

The **Empirical Cumulative Distribution Function** shows, for each value on the x-axis, the proportion of observations at or below it.

```python
sns.ecdfplot(data=df, x="total_bill")
plt.show()
```

If the curve reads 0.70 at a bill of 20, then 70% of bills are 20 or less. ECDFs need no bins or smoothing, so they are good for exact comparisons between groups.

## 2.4 `displot()` — Figure-level Distributions

`displot()` wraps all three through `kind` and adds faceting (see axes-level vs figure-level in Part 1).

```python
sns.displot(data=df, x="total_bill", kind="hist")                    # or "kde", "ecdf"
sns.displot(data=df, x="total_bill", hue="time", kind="kde")         # overlay groups
sns.displot(data=df, x="total_bill", col="time", kind="hist")        # one panel per group
plt.show()
```

---

# B. Categorical Plots

Categorical variables here: `day`, `sex`, `smoker`, `time`.

## 2.5 Choosing a Categorical Plot

| Question | Function |
| --- | --- |
| How many rows per category? | `countplot()` |
| What is the average (or other aggregate) per category? | `barplot()` |
| What are the median, spread and outliers? | `boxplot()` |
| What is the distribution shape? | `violinplot()` |
| Where are the individual observations? | `stripplot()` / `swarmplot()` |

All take `x` for the category and `y` for the numeric value (except `countplot`, which needs only one axis).

## 2.6 `countplot()` — Frequencies

```python
sns.countplot(data=df, x="day", hue="smoker")
plt.show()
```

Use `y="day"` instead of `x="day"` for a horizontal chart, which is better for long category names.

## 2.7 `barplot()` — Aggregates

`barplot()` is **not** a count chart. It aggregates a numeric column per category (mean by default) and draws an error bar showing uncertainty.

```python
sns.barplot(data=df, x="day", y="total_bill")                       # mean bill per day
sns.barplot(data=df, x="day", y="total_bill", estimator="median")   # use median
sns.barplot(data=df, x="day", y="total_bill", estimator="sum", errorbar=None)  # total bill
plt.show()
```

| Call | Meaning |
| --- | --- |
| `countplot(x="day")` | Number of records per day |
| `barplot(x="day", y="total_bill")` | Average bill per day |

> A bar of averages hides spread and outliers. That is why the next plots exist.

## 2.8 `boxplot()` — Median, Quartiles, Outliers

```python
sns.boxplot(data=df, x="day", y="total_bill", hue="sex")
plt.show()
```

```text
        │   <- upper whisker
     ┌─────┐
     │ ─── │ <- median (middle line); box = Q1 to Q3
     └─────┘
        │   <- lower whisker
        •   <- potential outlier
```

Boxplots are the standard EDA tool for **outlier detection**. For example, in a salary column such as `[25000, 28000, 30000, 32000, 35000, 38000, 40000, 250000]`, the value 250000 will appear as an isolated point above the whisker.

```python
salary = pd.DataFrame({"salary": [25000, 28000, 30000, 32000, 35000, 38000, 40000, 250000]})
sns.boxplot(data=salary, y="salary")
plt.show()
```

## 2.9 `violinplot()` — Distribution Shape

A violin plot combines a boxplot-style summary with a KDE. Its width shows how dense the data is at each value.

```python
sns.violinplot(data=df, x="day", y="total_bill", hue="sex")
plt.show()
```

Boxplot vs violin: a boxplot is compact and highlights outliers; a violin reveals shapes a box cannot, such as two peaks.

## 2.10 `stripplot()` and `swarmplot()` — Individual Observations

Summaries can hide how much data there is. These two draw every point.

```python
sns.stripplot(data=df, x="day", y="total_bill", jitter=True)
sns.swarmplot(data=df, x="day", y="total_bill")
plt.show()
```

| | `stripplot()` | `swarmplot()` |
| --- | --- | --- |
| Overlap handling | Random jitter | Points are positioned so none overlap |
| Speed on large data | Fast | Slow, and warns when points can't be placed |
| Best for | Larger or quick views | Small/medium data |

**Combine summary + raw points** (a very useful EDA pattern):

```python
sns.boxplot(data=df, x="day", y="total_bill")
sns.stripplot(data=df, x="day", y="total_bill", color="black", alpha=0.5)
plt.show()
```

## 2.11 `catplot()` — Figure-level Categorical Plots

`catplot()` is the single interface for all of the above, with faceting.

```python
sns.catplot(data=df, x="day", y="total_bill", kind="box", col="time")
plt.show()
```

`kind` accepts `"count"`, `"bar"`, `"box"`, `"violin"`, `"strip"`, `"swarm"`, plus `"boxen"` and `"point"`. Use `col=` for side-by-side panels and `row=` for stacked panels.

## 2.12 Controlling Category Order

By default, categories appear in the order found in the data. Set a meaningful order explicitly:

```python
order = ["Thur", "Fri", "Sat", "Sun"]
sns.boxplot(data=df, x="day", y="total_bill", order=order)
```

Or order by a metric (e.g. lowest to highest average bill):

```python
order = df.groupby("day")["total_bill"].mean().sort_values().index
sns.barplot(data=df, x="day", y="total_bill", order=order)
plt.show()
```

If a category column is really numeric (like `size`) and you want proper spacing on the axis, use `native_scale=True` in `stripplot`/`swarmplot`.

---

## Practical Workflow for One Category + One Number

```text
1. countplot   -> how many records per category? (is data balanced?)
2. barplot     -> which category has the highest average?
3. boxplot     -> how much does it vary? any outliers?
4. swarm/strip -> where are the actual observations?
```

## Common Mistakes

- Using `barplot()` when you want counts (use `countplot()`).
- Reading a bar of means as the whole story; always check spread with a boxplot or points.
- Using `swarmplot()` on thousands of rows.
- Comparing groups of different sizes with `stat="count"` histograms; use `density` or `percent`.
