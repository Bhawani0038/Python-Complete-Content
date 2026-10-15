
# Statistical Analysis in Pandas

Pandas provides summary, distribution, and relationship measures for numeric and categorical data.

## Sample data

```python
import pandas as pd

df = pd.DataFrame({
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 9],
    "Marks": [45, 50, 55, 62, 68, 74, 81, 88],
    "Attendance": [65, 70, 72, 78, 80, 85, 90, 94]
})
```

## Descriptive statistics

Use `agg()` for selected statistics, `quantile()` for percentiles, and `describe()` for a standard summary:

```python
df["Marks"].agg(["count", "mean", "median", "std", "var", "min", "max"])
df["Marks"].quantile([0.25, 0.5, 0.75])
df.describe()
```

The median is less sensitive to extreme values than the mean. Pandas uses
sample standard deviation by default (`ddof=1`); use `std(ddof=0)` for the
population standard deviation. Variance is the squared standard deviation;
range is `max() - min()`.

## Relationships between numeric columns

```python
df["Study_Hours"].corr(df["Marks"])
df.corr()  # correlation matrix

df["Study_Hours"].cov(df["Marks"])
df.cov()   # covariance matrix
```

Correlation ranges from -1 to +1 and describes the strength and direction of a
linear relationship; it does not establish causation. Covariance indicates
whether values move together, but its magnitude depends on their units.

## Categorical counts

```python
departments = pd.Series(["IT", "HR", "IT", "Sales", "IT", "HR"])
departments.value_counts()
departments.value_counts(normalize=True).mul(100)  # percentage
```

# Data Analysis with Pandas

Use Pandas summaries to answer business questions, compare segments, track trends, and flag unusual values.

## Sample sales data

```python
import pandas as pd

df = pd.DataFrame({
    "Date": [
        "2026-01-05", "2026-01-10", "2026-01-15",
        "2026-02-05", "2026-02-12", "2026-02-20",
        "2026-03-05", "2026-03-15", "2026-03-25"
    ],
    "Region": ["North", "South", "North", "South", "East", "North", "East", "South", "North"],
    "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Tablet", "Laptop", "Mobile", "Tablet", "Mobile"],
    "Sales": [85000, 45000, 50000, 90000, 35000, 95000, 55000, 40000, 60000],
    "Quantity": [5, 10, 8, 6, 7, 5, 11, 8, 12]
})
df["Date"] = pd.to_datetime(df["Date"])
```

## KPIs and segment summaries

A KPI is a numeric measure of business performance. A dictionary is useful for a small dashboard summary:

```python
kpis = {
    "total_sales": df["Sales"].sum(),
    "average_sale": df["Sales"].mean(),
    "total_quantity": df["Quantity"].sum(),
    "orders": len(df),
    "maximum_sale": df["Sales"].max()
}
```

Use named aggregations to compare metrics by region or product:

```python
region_summary = df.groupby("Region").agg(
    total_sales=("Sales", "sum"),
    average_sale=("Sales", "mean"),
    quantity=("Quantity", "sum"),
    orders=("Sales", "count")
)

product_summary = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
```

## Trends and segmentation

Group by month to calculate sales and month-over-month change:

```python
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()
monthly_growth = monthly_sales.pct_change().mul(100)
```

Compare two dimensions with `groupby()` or reshape the result into a report with `pivot_table()`:

```python
sales_by_segment = df.pivot_table(
    index="Region",
    columns="Product",
    values="Sales",
    aggfunc="sum",
    fill_value=0
)
```

## Outliers and business thresholds

The IQR rule flags statistical outliers; a business threshold is a separate rule chosen for the use case.

```python
q1, q3 = df["Sales"].quantile([0.25, 0.75])
iqr = q3 - q1
outliers = df[df["Sales"].lt(q1 - 1.5 * iqr) | df["Sales"].gt(q3 + 1.5 * iqr)]
high_value = df[df["Sales"] > 80000]  # example business threshold
```

Use `idxmax()` on grouped totals to get the best-performing segment, `nlargest()`
for top transactions, and the monthly summary above for trends. `max()` returns
a value; `idxmax()` returns the label for that value.

## Analysis workflow

```text
Inspect ? Clean ? Transform ? Summarize ? Segment ? Check trends/outliers ? Communicate
```

A typical first pass is `df.info()`, `df.describe()`, then KPI and grouped
summaries tailored to the question. Validate extreme values against the data
and business context instead of treating every one as an error.