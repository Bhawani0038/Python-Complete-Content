# Pandas Module — Part 5: Time, Indexing, Analysis & Visualization

The final part covers time-series data, hierarchical indexes, statistics and business analysis, and plotting the results.

> Assumes `import pandas as pd`, `import numpy as np` and `import matplotlib.pyplot as plt`.

---

# A. Date & Time

Date data is common in sales, finance, web analytics and IoT.

## 5.1 Converting and Extracting

Dates read from files are usually text (`object`). Convert first (see also `parse_dates` in Part 1):

```python
df = pd.DataFrame({
    "Date":  ["2026-01-10", "2026-02-15", "2026-03-20", "2026-04-25"],
    "Sales": [50000, 60000, 75000, 90000],
})
df["Date"] = pd.to_datetime(df["Date"])          # dtype becomes datetime64[ns]
```

The `.dt` accessor then exposes date parts:

| Part | Code |
| --- | --- |
| Year / month / day | `df["Date"].dt.year`, `.dt.month`, `.dt.day` |
| Names | `.dt.day_name()`, `.dt.month_name()` |
| Weekday (Mon=0) | `.dt.dayofweek` |
| Quarter / ISO week | `.dt.quarter`, `.dt.isocalendar().week` |
| Monthly period | `.dt.to_period("M")` |

```python
df["Month_Name"] = df["Date"].dt.month_name()
```

## 5.2 Filtering and Arithmetic

```python
df[df["Date"] > "2026-03-01"]
df[(df["Date"] >= "2026-02-01") & (df["Date"] <= "2026-03-31")]

df["Next_Week"] = df["Date"] + pd.Timedelta(days=7)
df["Days_Since"] = (pd.Timestamp("2026-05-01") - df["Date"]).dt.days
```

## 5.3 Date Ranges

```python
pd.date_range(start="2026-01-01", periods=5, freq="D")
```

| Frequency | Meaning |
| --- | --- |
| `D`, `W` | Daily, weekly |
| `MS` / `ME` | Month start / month end |
| `QE`, `YE` | Quarter end, year end |
| `h`, `min` | Hourly, minute |

> `ME`, `QE`, `YE` are the names in pandas 2.2 and later. In older versions use `M`, `Q`, `Y`.

## 5.4 Resampling

**Resampling** changes the frequency of time-series data (e.g. daily → monthly). The DataFrame needs a datetime index.

```python
daily = pd.DataFrame({
    "Date":  pd.date_range("2026-01-01", periods=90, freq="D"),
    "Sales": range(100, 190),
}).set_index("Date")

daily["Sales"].resample("ME").sum()      # monthly total
daily["Sales"].resample("ME").mean()     # monthly average
```

The standard monthly-report pattern:

```python
df["Date"] = pd.to_datetime(df["Date"])
monthly_sales = df.set_index("Date")["Sales"].resample("ME").sum()
```

Alternative without changing the index: `df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()`.

---

# B. Advanced Indexing (MultiIndex)

A **MultiIndex** (hierarchical index) has several levels, such as Region → Product or Year → Month.

## 5.5 Creating and Selecting

```python
sales = pd.DataFrame({
    "Region":  ["North", "North", "South", "South"],
    "Product": ["Laptop", "Mobile", "Laptop", "Mobile"],
    "Sales":   [100000, 60000, 80000, 50000],
}).set_index(["Region", "Product"])
```

```text
                 Sales
Region Product
North  Laptop   100000
       Mobile    60000
South  Laptop    80000
       Mobile    50000
```

```python
sales.loc["North"]                      # all rows of one outer level
sales.loc[("North", "Laptop")]          # one exact combination
sales.loc[["North", "South"]]           # several outer labels
sales.xs("Laptop", level="Product")     # cross-section: every Laptop row across regions

idx = pd.IndexSlice
sales.loc[idx["North", ["Laptop", "Mobile"]], :]    # advanced slicing
```

`xs()` is the easiest way to select by an **inner** level.

## 5.6 Sorting, Resetting and Manual Creation

```python
sales = sales.sort_index()                    # sort before slicing a MultiIndex
sales.sort_index(level="Product")             # sort by one level
sales.reset_index()                           # index levels -> normal columns
```

```python
pd.MultiIndex.from_tuples(
    [("North", "Laptop"), ("North", "Mobile")], names=["Region", "Product"]
)
```

`set_index()` moves columns into the index; `reset_index()` moves them back. Groupby with several keys (Part 4) also produces a MultiIndex, so `reset_index()` and `xs()` are useful there too.

---

# C. Statistical Analysis and Business Analysis

## 5.7 Descriptive Statistics

```python
stu = pd.DataFrame({
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 9],
    "Marks":       [45, 50, 55, 62, 68, 74, 81, 88],
    "Attendance":  [65, 70, 72, 78, 80, 85, 90, 94],
})

stu["Marks"].agg(["count", "mean", "median", "std", "var", "min", "max"])
stu["Marks"].quantile([0.25, 0.5, 0.75])
stu.describe()
```

- The **median** is less sensitive to extreme values than the mean.
- Pandas `std()` is the *sample* standard deviation (`ddof=1`); use `std(ddof=0)` for the population version.
- Variance is the squared standard deviation; range is `max() - min()`.

## 5.8 Correlation and Covariance

```python
stu["Study_Hours"].corr(stu["Marks"])      # one pair
stu.corr()                                 # correlation matrix
stu.cov()                                  # covariance matrix
```

Correlation (−1 to +1) measures the strength and direction of a **linear** relationship. Covariance shows whether variables move together, but its size depends on the units, so it is hard to compare. Neither proves causation. (Correlation heatmaps are in the Seaborn module.)

## 5.9 Business Analysis Workflow

```text
Inspect -> Clean -> Transform -> Summarize -> Segment -> Check trends/outliers -> Communicate
```

Sample data:

```python
sales = pd.DataFrame({
    "Date": pd.to_datetime([
        "2026-01-05", "2026-01-10", "2026-01-15",
        "2026-02-05", "2026-02-12", "2026-02-20",
        "2026-03-05", "2026-03-15", "2026-03-25"]),
    "Region":   ["North", "South", "North", "South", "East", "North", "East", "South", "North"],
    "Product":  ["Laptop", "Mobile", "Mobile", "Laptop", "Tablet", "Laptop", "Mobile", "Tablet", "Mobile"],
    "Sales":    [85000, 45000, 50000, 90000, 35000, 95000, 55000, 40000, 60000],
    "Quantity": [5, 10, 8, 6, 7, 5, 11, 8, 12],
})
```

**KPIs** (Key Performance Indicators: numbers that measure business performance):

```python
kpis = {
    "total_sales":    sales["Sales"].sum(),
    "average_sale":   sales["Sales"].mean(),
    "total_quantity": sales["Quantity"].sum(),
    "orders":         len(sales),
}
```

**Segment comparison** (techniques from Part 4):

```python
region_summary = sales.groupby("Region").agg(
    total_sales=("Sales", "sum"), average_sale=("Sales", "mean"), orders=("Sales", "count"))

product_sales = sales.groupby("Product")["Sales"].sum().sort_values(ascending=False)
product_sales.idxmax()                    # best-performing product

sales.pivot_table(index="Region", columns="Product", values="Sales", aggfunc="sum", fill_value=0)
```

**Trend:**

```python
monthly = sales.groupby(sales["Date"].dt.to_period("M"))["Sales"].sum()
monthly_growth = monthly.pct_change().mul(100)         # month-over-month % change
```

**Outliers.** The IQR rule flags statistical outliers; a business threshold is a separate rule.

```python
q1, q3 = sales["Sales"].quantile([0.25, 0.75])
iqr = q3 - q1
outliers   = sales[(sales["Sales"] < q1 - 1.5 * iqr) | (sales["Sales"] > q3 + 1.5 * iqr)]
high_value = sales[sales["Sales"] > 80000]             # example business rule
```

Check extreme values against the business context before treating them as errors.

---

# D. Visualization with Pandas + Matplotlib

Visualization turns numbers into patterns. Aggregate first, then plot.

```text
Raw data -> groupby / resample -> aggregated result -> plot
```

## 5.10 Choosing a Chart

| Question | Chart | Matplotlib | Pandas `kind=` |
| --- | --- | --- | --- |
| Change over time? | Line | `plt.plot()` | `"line"` |
| Compare categories? | Bar | `plt.bar()` | `"bar"` / `"barh"` |
| Distribution of a number? | Histogram | `plt.hist()` | `"hist"` |
| Outliers / spread? | Box plot | `plt.boxplot()` | `"box"` |
| Two numeric variables related? | Scatter | `plt.scatter()` | `"scatter"` |
| Share of a total (few categories)? | Pie | `plt.pie()` | `"pie"` |

Use `barh` for long category names. Bars are easier to compare than pie slices when there are many categories.

## 5.11 Plotting Directly from Pandas

Every Pandas Series and DataFrame has a `.plot()` method that uses Matplotlib underneath.

```python
monthly_df = pd.DataFrame({
    "Month":  ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales":  [50000, 60000, 55000, 75000, 80000, 90000],
    "Orders": [120, 140, 130, 170, 180, 210],
})

monthly_df.plot(x="Month", y="Sales", kind="line", marker="o", title="Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
```

```python
monthly_df["Sales"].plot(kind="hist", bins=5)
monthly_df["Sales"].plot(kind="box")
monthly_df.plot(x="Orders", y="Sales", kind="scatter", title="Orders vs Sales")
```

## 5.12 Plotting Grouped Results

```python
region_sales = sales.groupby("Region")["Sales"].sum()

region_sales.plot(kind="bar", title="Sales by Region")
plt.ylabel("Sales")
plt.show()

region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.show()
```

Plot a visualization and its number together: a scatter plot shows the relationship, and `corr()` quantifies it.

```python
monthly_df["Orders"].corr(monthly_df["Sales"])
```

## 5.13 Reusable Monthly-Trend Pattern

```python
sales["Date"] = pd.to_datetime(sales["Date"])

monthly = sales.groupby(sales["Date"].dt.to_period("M"))["Sales"].sum()

monthly.plot(kind="line", marker="o")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

For richer statistical plots and layouts, continue with the Seaborn module.

## Quick Reference

| Task | Tool |
| --- | --- |
| String to date | `pd.to_datetime()` |
| Date parts | `.dt.year`, `.dt.month_name()`, `.dt.to_period("M")` |
| Date arithmetic | `pd.Timedelta`, `pd.date_range()` |
| Change frequency | `set_index()` + `resample()` |
| Multi-level index | `set_index([...])`, `loc`, `xs()`, `reset_index()` |
| Statistics | `describe()`, `agg()`, `quantile()`, `corr()`, `cov()` |
| Best segment | `groupby().sum().idxmax()` |
| Trend / growth | `groupby(to_period)` + `pct_change()` |
| Outliers | IQR rule, business threshold |
| Plot | `df.plot(kind=...)`, Matplotlib |
