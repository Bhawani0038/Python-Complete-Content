# Reshaping Data in Pandas

Reshaping means **changing the structure of a DataFrame without changing the underlying information**.

We will cover:

1. `pivot()`
2. `pivot_table()`
3. `melt()`
4. Difference between `pivot()` and `pivot_table()`
5. Real-world example

---

## 11.1 `pivot()`

`pivot()` converts **unique row values into columns**.

### Example

```python
import pandas as pd

df = pd.DataFrame({
    "Month": ["Jan", "Jan", "Feb", "Feb"],
    "Product": ["Laptop", "Mobile", "Laptop", "Mobile"],
    "Sales": [50000, 30000, 60000, 35000]
})

print(df)
```

Output:

```text
  Month Product  Sales
0   Jan  Laptop  50000
1   Jan  Mobile  30000
2   Feb  Laptop  60000
3   Feb  Mobile  35000
```

Now reshape it:

```python
result = df.pivot(
    index="Month",
    columns="Product",
    values="Sales"
)

print(result)
```

Output:

```text
Product  Laptop  Mobile
Month
Feb       60000   35000
Jan       50000   30000
```

### Structure

```text
pivot(
    index=,
    columns=,
    values=
)
```

Think of it as:

```text
Rows      → index
Columns   → columns
Values    → values
```

---

# 11.2 `pivot_table()`

`pivot_table()` is similar to `pivot()`, but it can **aggregate duplicate records**.

This is extremely useful in real-world data.

```python
df = pd.DataFrame({
    "Month": ["Jan", "Jan", "Jan", "Feb", "Feb"],
    "Product": ["Laptop", "Laptop", "Mobile", "Laptop", "Mobile"],
    "Sales": [50000, 55000, 30000, 60000, 35000]
})
```

Here January has **two Laptop records**.

Using:

```python
df.pivot(
    index="Month",
    columns="Product",
    values="Sales"
)
```

will produce an error because the `Month + Product` combination is not unique.

Instead:

```python
result = df.pivot_table(
    index="Month",
    columns="Product",
    values="Sales",
    aggfunc="sum"
)

print(result)
```

Output:

```text
Product  Laptop  Mobile
Month
Feb       60000   35000
Jan      105000   30000
```

Because:

```text
Jan Laptop
= 50000 + 55000
= 105000
```

---

## 11.3 Different Aggregations

You can use:

```python
aggfunc="sum"
```

```python
aggfunc="mean"
```

```python
aggfunc="count"
```

```python
aggfunc="max"
```

Example:

```python
df.pivot_table(
    index="Month",
    columns="Product",
    values="Sales",
    aggfunc="mean"
)
```

---

# 11.4 `melt()`

`melt()` does the **opposite type of transformation**.

It converts **wide data → long data**.

Example:

```python
df = pd.DataFrame({
    "Product": ["Laptop", "Mobile", "Tablet"],
    "Jan": [50000, 30000, 20000],
    "Feb": [60000, 35000, 25000],
    "Mar": [70000, 40000, 30000]
})

print(df)
```

Output:

```text
  Product    Jan    Feb    Mar
0  Laptop  50000  60000  70000
1  Mobile  30000  35000  40000
2  Tablet  20000  25000  30000
```

Convert it into long format:

```python
result = df.melt(
    id_vars="Product",
    var_name="Month",
    value_name="Sales"
)

print(result)
```

Output:

```text
  Product Month  Sales
0  Laptop   Jan  50000
1  Mobile   Jan  30000
2  Tablet   Jan  20000
3  Laptop   Feb  60000
4  Mobile   Feb  35000
5  Tablet   Feb  25000
6  Laptop   Mar  70000
7  Mobile   Mar  40000
8  Tablet   Mar  30000
```

---

## 11.5 `pivot()` vs `pivot_table()` vs `melt()`

| Function        | Purpose                   |
| --------------- | ------------------------- |
| `pivot()`       | Long → Wide               |
| `pivot_table()` | Long → Wide + aggregation |
| `melt()`        | Wide → Long               |

### Easy way to remember

```text
melt()
   ↓
Wide → Long

pivot()
   ↓
Long → Wide

pivot_table()
   ↓
Long → Wide + aggregation
```

---

# Real-World Example

Suppose a company has sales data:

```python
sales = pd.DataFrame({
    "Region": ["North", "North", "South", "South"],
    "Product": ["Laptop", "Mobile", "Laptop", "Mobile"],
    "Sales": [100000, 60000, 80000, 50000]
})
```

Create a report:

```python
report = sales.pivot_table(
    index="Region",
    columns="Product",
    values="Sales",
    aggfunc="sum"
)

print(report)
```

Output:

```text
Product  Laptop  Mobile
Region
North    100000   60000
South     80000   50000
```

This type of reshaping is commonly used before creating **Excel reports, dashboards, Power BI datasets, and analytical summaries**.

### Keywords Recap

```text
Reshaping
├── pivot()
├── pivot_table()
├── melt()
├── Wide Data
├── Long Data
└── Aggregation
```