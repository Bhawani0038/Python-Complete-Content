# Date & Time in Pandas

Date and time data is very common in **sales, finance, healthcare, web analytics, IoT, and transaction datasets**.

We will cover:

1. `pd.to_datetime()`
2. Extracting year, month, day
3. Date filtering
4. Date arithmetic
5. Date ranges
6. Resampling

---

## 12.1 Creating Date Data

```python
import pandas as pd

df = pd.DataFrame({
    "Date": [
        "2026-01-10",
        "2026-02-15",
        "2026-03-20",
        "2026-04-25"
    ],
    "Sales": [50000, 60000, 75000, 90000]
})

print(df)
```

Initially, `Date` may be stored as a string.

Check:

```python
print(df.dtypes)
```

Output:

```text
Date     object
Sales     int64
dtype: object
```

Convert it to datetime:

```python
df["Date"] = pd.to_datetime(df["Date"])
```

Now:

```python
print(df.dtypes)
```

Output:

```text
Date     datetime64[ns]
Sales             int64
dtype: object
```

---

# 12.2 Extract Year, Month and Day

Once the column is datetime:

### Year

```python
df["Year"] = df["Date"].dt.year
```

### Month

```python
df["Month"] = df["Date"].dt.month
```

### Day

```python
df["Day"] = df["Date"].dt.day
```

### Day Name

```python
df["Day_Name"] = df["Date"].dt.day_name()
```

### Month Name

```python
df["Month_Name"] = df["Date"].dt.month_name()
```

Example:

```python
print(df)
```

Output:

```text
        Date  Sales  Year  Month  Day Day_Name Month_Name
0 2026-01-10  50000  2026      1   10 Saturday    January
1 2026-02-15  60000  2026      2   15 Sunday   February
2 2026-03-20  75000  2026      3   20 Friday      March
3 2026-04-25  90000  2026      4   25 Saturday    April
```

---

# 12.3 Date Filtering

Suppose we want records after March 1:

```python
result = df[df["Date"] > "2026-03-01"]

print(result)
```

Output:

```text
        Date  Sales
2 2026-03-20  75000
3 2026-04-25  90000
```

You can also filter a date range:

```python
result = df[
    (df["Date"] >= "2026-02-01") &
    (df["Date"] <= "2026-03-31")
]
```

---

# 12.4 Using `.dt`

The `.dt` accessor provides many useful datetime operations.

| Operation   | Code                               |
| ----------- | ---------------------------------- |
| Year        | `df["Date"].dt.year`               |
| Month       | `df["Date"].dt.month`              |
| Day         | `df["Date"].dt.day`                |
| Day name    | `df["Date"].dt.day_name()`         |
| Month name  | `df["Date"].dt.month_name()`       |
| Day of week | `df["Date"].dt.dayofweek`          |
| Quarter     | `df["Date"].dt.quarter`            |
| Week        | `df["Date"].dt.isocalendar().week` |

---

# 12.5 Date Arithmetic

You can add or subtract time using `pd.Timedelta`.

```python
df["Next_Week"] = df["Date"] + pd.Timedelta(days=7)
```

Subtract 30 days:

```python
df["Previous_Month"] = df["Date"] - pd.Timedelta(days=30)
```

---

# 12.6 Creating Date Ranges

`pd.date_range()` generates a sequence of dates.

```python
dates = pd.date_range(
    start="2026-01-01",
    end="2026-01-10"
)

print(dates)
```

You can specify frequency:

```python
dates = pd.date_range(
    start="2026-01-01",
    periods=5,
    freq="D"
)
```

Output:

```text
2026-01-01
2026-01-02
2026-01-03
2026-01-04
2026-01-05
```

Common frequencies:

| Frequency | Meaning     |
| --------- | ----------- |
| `D`       | Daily       |
| `W`       | Weekly      |
| `ME`      | Month end   |
| `MS`      | Month start |
| `QE`      | Quarter end |
| `YE`      | Year end    |
| `h`       | Hourly      |
| `min`     | Minute      |

---

# 12.7 Resampling

**Resampling** means changing the frequency of time-series data.

For example:

```text
Daily Sales
     ↓
Monthly Sales
```

Example:

```python
df = pd.DataFrame({
    "Date": pd.date_range("2026-01-01", periods=90, freq="D"),
    "Sales": range(100, 190)
})

df = df.set_index("Date")
```

Now calculate monthly sales:

```python
monthly_sales = df["Sales"].resample("ME").sum()

print(monthly_sales)
```

This converts:

```text
Daily Data
    ↓
Monthly Data
```

For monthly average:

```python
monthly_avg = df["Sales"].resample("ME").mean()
```

For monthly maximum:

```python
monthly_max = df["Sales"].resample("ME").max()
```

---

## Important Real-World Pattern

A typical sales-analysis workflow is:

```python
df["Date"] = pd.to_datetime(df["Date"])

df = df.set_index("Date")

monthly_sales = (
    df["Sales"]
    .resample("ME")
    .sum()
)

print(monthly_sales)
```

This pattern is extremely useful for **monthly revenue reports, financial analysis, website traffic, transactions, and business dashboards**.

### Keywords Recap

```text
Date & Time
├── pd.to_datetime()
├── .dt.year
├── .dt.month
├── .dt.day
├── .dt.day_name()
├── Date Filtering
├── pd.Timedelta
├── pd.date_range()
├── set_index()
└── resample()
```