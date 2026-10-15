
# Data Transformation in Pandas

Data transformation means **changing existing data or creating new columns so that the dataset becomes useful for analysis, reporting, or Machine Learning**.

We will use this sales dataset:

```python
import pandas as pd

df = pd.DataFrame({
    "customer": ["Amit", "Ravi", "Priya", "Neha", "Rahul", "Kiran"],
    "city": ["Jodhpur", "Jaipur", "Delhi", "Mumbai", "Jodhpur", "Delhi"],
    "category": ["Laptop", "Mobile", "Laptop", "Tablet", "Mobile", "Laptop"],
    "quantity": [2, 3, 1, 4, 2, 1],
    "price": [65000, 32000, 72000, 28000, 41000, 85000]
})

print(df)
```

---

# 1. Creating a New Column

Suppose:

```text
quantity × price = total_sales
```

Create:

```python
df["total_sales"] = df["quantity"] * df["price"]

print(df)
```

Output:

```text
  customer     city category  quantity  price  total_sales
0     Amit  Jodhpur   Laptop         2  65000       130000
1     Ravi   Jaipur   Mobile         3  32000        96000
2    Priya    Delhi   Laptop         1  72000        72000
3     Neha   Mumbai   Tablet         4  28000       112000
4    Rahul  Jodhpur   Mobile         2  41000        82000
5    Kiran    Delhi   Laptop         1  85000        85000
```

This is one of the most important Pandas operations.

---

# 2. Mathematical Transformation

Create a discount column:

```python
df["discount"] = df["total_sales"] * 0.10
```

Create final revenue:

```python
df["final_amount"] = (
    df["total_sales"] - df["discount"]
)
```

Now we have:

```text
quantity
   ↓
price
   ↓
total_sales
   ↓
discount
   ↓
final_amount
```

---

# 3. Creating a Column with a Condition

Suppose customers spending ₹100,000 or more are classified as `"High Value"`.

```python
df["customer_type"] = "Regular"

df.loc[
    df["total_sales"] >= 100000,
    "customer_type"
] = "High Value"
```

Result:

```text
customer  total_sales  customer_type
Amit         130000     High Value
Ravi          96000     Regular
Priya         72000     Regular
Neha         112000     High Value
Rahul         82000     Regular
Kiran         85000     Regular
```

---

# 4. `np.where()`

For simple two-condition transformations, NumPy's `where()` is useful.

```python
import numpy as np

df["customer_type"] = np.where(
    df["total_sales"] >= 100000,
    "High Value",
    "Regular"
)
```

Logic:

```text
condition
   │
   ├── True  → High Value
   │
   └── False → Regular
```

---

# 5. Multiple Conditions with `np.select()`

Suppose we want three categories:

```text
>= 120000 → Premium
>= 90000  → Gold
< 90000   → Regular
```

```python
conditions = [
    df["total_sales"] >= 120000,
    df["total_sales"] >= 90000
]

choices = [
    "Premium",
    "Gold"
]

df["customer_type"] = np.select(
    conditions,
    choices,
    default="Regular"
)
```

---

# 6. `map()`

`map()` is useful for replacing values according to a mapping dictionary.

Suppose we want city codes:

```python
city_codes = {
    "Jodhpur": "JDH",
    "Jaipur": "JAI",
    "Delhi": "DEL",
    "Mumbai": "MUM"
}

df["city_code"] = df["city"].map(city_codes)
```

Result:

```text
city       city_code
Jodhpur    JDH
Jaipur     JAI
Delhi      DEL
Mumbai     MUM
```

---

# 7. `replace()`

`replace()` is useful when directly replacing values.

```python
df["category"] = df["category"].replace({
    "Laptop": "Computer",
    "Mobile": "Smartphone"
})
```

Now:

```text
Laptop → Computer
Mobile → Smartphone
```

Unlike `map()`, values that aren't present in the mapping can remain unchanged.

---

# 8. `apply()` and Vectorization

`apply()` runs a function on Series values or DataFrame rows. For arithmetic, prefer vectorized operations:

```python
df["tax"] = df["total_sales"] * 0.18
```

Use `Series.apply(function)` only when a suitable vectorized method is
unavailable. `DataFrame.apply(function, axis=1)` passes one row at a time and
is usually slower than column-wise operations.

---

# 9. Text Transformations

Use the `.str` accessor for text columns. For example:

```python
df["customer"] = df["customer"].str.strip().str.title()
```

See [Text Data in Pandas](#text-data-in-pandas) for searching, replacing, extracting, and other string operations.

---

# 10. `astype()`

Change data type:

```python
df["quantity"] = df["quantity"].astype("int64")
```

Convert to string:

```python
df["quantity"] = df["quantity"].astype("string")
```

For categorical data:

```python
df["category"] = df["category"].astype("category")
```

Categorical types can reduce memory usage when a column contains relatively few repeated values.

---

# 11. Binning Numerical Data

Suppose we want to convert customer spending into groups:

```text
0–50000       Low
50000–100000  Medium
100000+       High
```

Use `pd.cut()`:

```python
df["sales_level"] = pd.cut(
    df["total_sales"],
    bins=[0, 50000, 100000, float("inf")],
    labels=["Low", "Medium", "High"]
)
```

This is useful for:

* Customer segmentation
* Age groups
* Salary bands
* Price ranges
* Risk categories

---

# 12. `pd.qcut()`

`qcut()` creates groups based on **quantiles**.

For example, divide customers into four equally sized groups:

```python
df["sales_quartile"] = pd.qcut(
    df["total_sales"],
    q=4,
    labels=["Q1", "Q2", "Q3", "Q4"]
)
```

Difference:

| Function | Grouping               |
| -------- | ---------------------- |
| `cut()`  | Fixed numerical ranges |
| `qcut()` | Quantile-based groups  |

---

# 13. Renaming Columns

Rename specific columns:

```python
df = df.rename(columns={
    "price": "unit_price",
    "quantity": "units_sold"
})
```

Rename all columns:

```python
df.columns = [
    "customer",
    "city",
    "category",
    "units_sold",
    "unit_price"
]
```

For production pipelines, `rename()` is usually safer when only a few columns need changing.

---

# 14. Reordering Columns

Suppose we want:

```text
customer
city
category
units_sold
unit_price
total_sales
```

Use:

```python
df = df[
    [
        "customer",
        "city",
        "category",
        "units_sold",
        "unit_price",
        "total_sales"
    ]
]
```

---

# 15. Insert a Column at a Specific Position

```python
df.insert(
    2,
    "region",
    ["West", "North", "North", "West", "West", "North"]
)
```

Syntax:

```python
df.insert(
    position,
    column_name,
    values
)
```

---

# 16. Remove a Column

```python
df = df.drop(
    columns=["region"]
)
```

Multiple columns:

```python
df = df.drop(
    columns=["region", "customer_type"]
)
```

---

# 17. A Real Transformation Pipeline

A typical sales-analysis transformation might look like:

```python
import pandas as pd
import numpy as np

df = pd.read_csv("sales.csv")

# Clean text
df["customer"] = (
    df["customer"]
    .str.strip()
    .str.title()
)

df["city"] = (
    df["city"]
    .str.strip()
    .str.title()
)

# Calculate sales
df["total_sales"] = (
    df["quantity"] * df["price"]
)

# Calculate discount
df["discount"] = (
    df["total_sales"] * 0.10
)

# Calculate final amount
df["final_amount"] = (
    df["total_sales"] - df["discount"]
)

# Customer segmentation
df["customer_type"] = np.where(
    df["total_sales"] >= 100000,
    "High Value",
    "Regular"
)
```

Now the raw dataset has been transformed into an analysis-ready dataset.

---

# 18. Transformation Methods to Remember

| Method            | Main Use                   |
| ----------------- | -------------------------- |
| `df["new"] = ...` | Create columns             |
| `loc[]`           | Conditional transformation |
| `np.where()`      | Two-way conditions         |
| `np.select()`     | Multiple conditions        |
| `map()`           | Dictionary-based mapping   |
| `replace()`       | Replace values             |
| `apply()`         | Custom functions           |
| `.str`            | Text transformation        |
| `astype()`        | Data type conversion       |
| `pd.cut()`        | Fixed-range bins           |
| `pd.qcut()`       | Quantile bins              |
| `rename()`        | Rename columns             |
| `drop()`          | Remove columns/rows        |
| `insert()`        | Add column at position     |

## Core Principle

Prefer **vectorized Pandas/NumPy operations** whenever possible:

```python
df["total"] = df["quantity"] * df["price"]
```

rather than:

```python
df["total"] = df.apply(
    lambda row: row["quantity"] * row["price"],
    axis=1
)
```

Vectorized operations are generally simpler, faster, and easier to maintain.