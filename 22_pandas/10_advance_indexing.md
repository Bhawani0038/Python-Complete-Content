
# Advanced Indexing in Pandas

Advanced indexing is useful when data has **multiple levels of indexing**, such as:

* Region → Product
* Year → Month
* Country → City
* Department → Employee

Pandas provides **MultiIndex**, also called **hierarchical indexing**, for this purpose.

We will cover:

1. MultiIndex
2. Creating MultiIndex
3. `set_index()`
4. Selecting MultiIndex data
5. `loc[]`
6. `xs()`
7. Resetting MultiIndex
8. Real-world example

---

## 15.1 What is MultiIndex?

A normal DataFrame has one index:

```text
Index
  ↓
0
1
2
3
```

A MultiIndex can have multiple levels:

```text
Region
   ↓
North
  ├── Laptop
  └── Mobile

South
  ├── Laptop
  └── Mobile
```

So instead of:

```text
Region
```

we can have:

```text
Region + Product
```

as the index.

---

# 15.2 Creating MultiIndex with `set_index()`

Consider:

```python
import pandas as pd

df = pd.DataFrame({
    "Region": ["North", "North", "South", "South"],
    "Product": ["Laptop", "Mobile", "Laptop", "Mobile"],
    "Sales": [100000, 60000, 80000, 50000]
})

print(df)
```

Output:

```text
  Region Product   Sales
0  North  Laptop  100000
1  North  Mobile   60000
2  South  Laptop   80000
3  South  Mobile   50000
```

Create hierarchical index:

```python
df = df.set_index(["Region", "Product"])

print(df)
```

Output:

```text
                 Sales
Region Product
North  Laptop   100000
       Mobile    60000
South  Laptop    80000
       Mobile    50000
```

Now the index has two levels:

```text
Level 1 → Region
Level 2 → Product
```

---

# 15.3 Selecting One Level

Select all records for `North`:

```python
print(df.loc["North"])
```

Output:

```text
        Sales
Product
Laptop  100000
Mobile   60000
```

Select a specific combination:

```python
print(df.loc[("North", "Laptop")])
```

Output:

```text
Sales    100000
```

---

# 15.4 Selecting Multiple Products

You can use:

```python
print(
    df.loc[
        ("North", ["Laptop", "Mobile"]), :
    ]
)
```

For more complex MultiIndex selection, `pd.IndexSlice` is useful:

```python
idx = pd.IndexSlice

result = df.loc[
    idx["North", ["Laptop", "Mobile"]], :
]

print(result)
```

---

# 15.5 `xs()` — Cross Section

`xs()` is particularly useful for selecting one level of a MultiIndex.

For example, select all `Laptop` records:

```python
print(
    df.xs("Laptop", level="Product")
)
```

Output:

```text
        Sales
Region
North   100000
South    80000
```

This is useful when you want to filter based on a specific index level.

---

# 15.6 Selecting Multiple Regions

```python
result = df.loc[
    ["North", "South"]
]

print(result)
```

Output:

```text
                 Sales
Region Product
North  Laptop   100000
       Mobile    60000
South  Laptop    80000
       Mobile    50000
```

---

# 15.7 Sorting a MultiIndex

A MultiIndex should generally be sorted before performing some advanced selections.

```python
df = df.sort_index()
```

You can sort by a specific level:

```python
df = df.sort_index(level="Product")
```

---

# 15.8 Resetting the Index

If you want to convert the index levels back into normal columns:

```python
df = df.reset_index()
```

Output:

```text
  Region Product   Sales
0  North  Laptop  100000
1  North  Mobile   60000
2  South  Laptop   80000
3  South  Mobile   50000
```

So:

```text
set_index()
     ↓
Columns → Index

reset_index()
     ↓
Index → Columns
```

---

# 15.9 Creating MultiIndex Directly

You can also create a MultiIndex manually:

```python
index = pd.MultiIndex.from_tuples([
    ("North", "Laptop"),
    ("North", "Mobile"),
    ("South", "Laptop"),
    ("South", "Mobile")
], names=["Region", "Product"])

df = pd.DataFrame(
    {"Sales": [100000, 60000, 80000, 50000]},
    index=index
)

print(df)
```

Output:

```text
                 Sales
Region Product
North  Laptop   100000
       Mobile    60000
South  Laptop    80000
       Mobile    50000
```

---

# 15.10 Real-World Example

Consider monthly sales by region and product:

```python
sales = pd.DataFrame({
    "Year": [2025, 2025, 2025, 2025, 2026, 2026],
    "Region": [
        "North", "North", "South",
        "South", "North", "South"
    ],
    "Product": [
        "Laptop", "Mobile", "Laptop",
        "Mobile", "Laptop", "Mobile"
    ],
    "Sales": [
        100000, 60000, 80000,
        50000, 120000, 70000
    ]
})
```

Create hierarchical indexing:

```python
sales = sales.set_index(
    ["Year", "Region", "Product"]
)
```

Now the hierarchy is:

```text
Year
 └── Region
      └── Product
```

Output:

```text
                        Sales
Year Region Product
2025 North  Laptop     100000
           Mobile       60000
     South  Laptop      80000
           Mobile        50000
2026 North  Laptop     120000
     South  Mobile      70000
```

Select all 2026 records:

```python
sales.loc[2026]
```

Select 2026 North Laptop:

```python
sales.loc[(2026, "North", "Laptop")]
```

Select all Laptop records:

```python
sales.xs(
    "Laptop",
    level="Product"
)
```

---

## MultiIndex vs Normal Index

| Normal Index         | MultiIndex                    |
| -------------------- | ----------------------------- |
| One index level      | Multiple levels               |
| Simple datasets      | Hierarchical datasets         |
| `df.loc["North"]`    | `df.loc[("North", "Laptop")]` |
| Easier to understand | More powerful                 |
| Flat structure       | Hierarchical structure        |

### Important Functions

```text
set_index()
      ↓
Create MultiIndex

loc[]
      ↓
Select MultiIndex data

xs()
      ↓
Select cross-section

sort_index()
      ↓
Sort hierarchical index

reset_index()
      ↓
Convert index back to columns
```

### Keywords Recap

```text
Advanced Indexing
├── MultiIndex
├── Hierarchical Index
├── set_index()
├── reset_index()
├── loc[]
├── IndexSlice
├── xs()
└── sort_index()
```