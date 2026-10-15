# Selecting and Filtering Data in Pandas

Selecting the correct rows and columns is one of the most important skills in Data Analysis.

We will use this dataset throughout the module:

```python
import pandas as pd

df = pd.DataFrame({
    "customer": ["Amit", "Ravi", "Priya", "Neha", "Rahul", "Kiran", "Vikas", "Pooja"],
    "city": ["Jodhpur", "Jaipur", "Delhi", "Mumbai", "Jodhpur", "Delhi", "Jaipur", "Mumbai"],
    "category": ["Laptop", "Mobile", "Laptop", "Tablet", "Mobile", "Laptop", "Tablet", "Mobile"],
    "sales": [65000, 32000, 72000, 28000, 41000, 85000, 36000, 45000]
})

print(df)
```

Output:

```text
  customer     city category  sales
0     Amit  Jodhpur   Laptop  65000
1     Ravi   Jaipur   Mobile  32000
2    Priya    Delhi   Laptop  72000
3     Neha   Mumbai   Tablet  28000
4    Rahul  Jodhpur   Mobile  41000
5    Kiran    Delhi   Laptop  85000
6    Vikas   Jaipur   Tablet  36000
7    Pooja   Mumbai   Mobile  45000
```

---

# 1. Selecting One Column

Use:

```python
df["customer"]
```

Output:

```text
0     Amit
1     Ravi
2    Priya
3     Neha
4    Rahul
5    Kiran
6    Vikas
7    Pooja
Name: customer, dtype: object
```

Another example:

```python
df["sales"]
```

---

# 2. Selecting Multiple Columns

Use a list of column names:

```python
df[["customer", "sales"]]
```

Output:

```text
  customer  sales
0     Amit  65000
1     Ravi  32000
2    Priya  72000
3     Neha  28000
4    Rahul  41000
5    Kiran  85000
6    Vikas  36000
7    Pooja  45000
```

Three columns:

```python
df[["customer", "city", "sales"]]
```

---

# 3. Selecting Rows Using Index

### First row

```python
df.iloc[0]
```

### Third row

```python
df.iloc[2]
```

### Rows 0 to 3

```python
df.iloc[0:4]
```

Output:

```text
  customer     city category  sales
0     Amit  Jodhpur   Laptop  65000
1     Ravi   Jaipur   Mobile  32000
2    Priya    Delhi   Laptop  72000
3     Neha   Mumbai   Tablet  28000
```

Remember:

```text
iloc = integer/location based indexing
```

---

# 4. Selecting Specific Rows

```python
df.iloc[[0, 3, 5]]
```

This selects rows:

```text
0
3
5
```

---

# 5. Selecting Rows and Columns with `iloc`

Syntax:

```python
df.iloc[row_position, column_position]
```

Example:

```python
df.iloc[0, 3]
```

Output:

```text
65000
```

Because:

```text
row 0     → Amit
column 3  → sales
```

---

## Selecting Multiple Rows and Columns

```python
df.iloc[0:4, 0:3]
```

This means:

```text
Rows    → 0 to 3
Columns → 0 to 2
```

Output:

```text
  customer     city category
0     Amit  Jodhpur   Laptop
1     Ravi   Jaipur   Mobile
2    Priya    Delhi   Laptop
3     Neha   Mumbai   Tablet
```

---

# 6. `loc[]`

`loc` is used for **label-based selection**.

Syntax:

```python
df.loc[row_label, column_label]
```

Example:

```python
df.loc[0, "customer"]
```

Output:

```text
Amit
```

Another:

```python
df.loc[2, "sales"]
```

Output:

```text
72000
```

---

# 7. `loc` with Multiple Columns

```python
df.loc[0:3, ["customer", "sales"]]
```

Output:

```text
  customer  sales
0     Amit  65000
1     Ravi  32000
2    Priya  72000
3     Neha  28000
```

Notice an important difference:

```python
df.iloc[0:3]
```

selects rows:

```text
0, 1, 2
```

while:

```python
df.loc[0:3]
```

with the default integer index includes:

```text
0, 1, 2, 3
```

---

# 8. `loc` vs `iloc`

| Feature              | `loc`       | `iloc`            |
| -------------------- | ----------- | ----------------- |
| Based on             | Labels      | Integer positions |
| Example              | `df.loc[2]` | `df.iloc[2]`      |
| Column selection     | Names       | Positions         |
| `df.loc[2, "sales"]` | Valid       | —                 |
| `df.iloc[2, 3]`      | —           | Valid             |

Simple rule:

```text
loc  → labels/names
iloc → positions/numbers
```

---

# 9. Conditional Filtering

Keep rows where a condition is `True`:

```python
df[df["sales"] > 50000]
```

Comparison operators include `>`, `<`, `>=`, `<=`, and `==` (equality; `=` assigns).

Filter text the same way:

```python
df[df["city"] == "Delhi"]
```

Combine conditions with `&` (AND), `|` (OR), and `~` (NOT). Parenthesize each condition:

```python
df[
    (df["city"] == "Delhi") &
    (df["sales"] > 70000)
]
```

For several possible values, prefer `isin()` to a chain of OR conditions:

```python
df[df["city"].isin(["Delhi", "Mumbai", "Jaipur"])]
```

Use `~` to exclude values, and `between()` for an inclusive numeric range:

```python
df[~df["city"].isin(["Delhi", "Mumbai"])]
df[df["sales"].between(40000, 70000)]
```

---

# 10. Filtering with `query()`

```python
df.query("sales > 50000 and city == 'Delhi'")
```

`query()` can make multi-condition filters more readable.

---

# 11. Selecting Columns After Filtering

```python
df.loc[
    (df["category"] == "Laptop") & (df["sales"] > 60000),
    ["customer", "city", "sales"]
]
```

---

# 12. Selecting Top Sales

Use `nlargest()` for the top rows, or sort the full DataFrame when you need every row ordered:

```python
df.nlargest(3, "sales")
df.sort_values("sales", ascending=False)
```

---

# 13. Selecting Maximum and Minimum

```python
df["sales"].max()                # highest sales value
df.loc[df["sales"].idxmax()]     # row with the highest sales
df.loc[df["sales"].idxmin()]     # row with the lowest sales
```

---
