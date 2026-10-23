# Pandas Module — Part 4: Sorting, Grouping, Combining & Reshaping

This part is about **summarizing** data (sort, aggregate, group) and **restructuring** it (combine tables, reshape).

```python
df = pd.DataFrame({
    "customer": ["Amit", "Ravi", "Priya", "Neha", "Rahul", "Kiran", "Vikas", "Pooja"],
    "city":     ["Jodhpur", "Jaipur", "Delhi", "Mumbai", "Jodhpur", "Delhi", "Jaipur", "Mumbai"],
    "category": ["Laptop", "Mobile", "Laptop", "Tablet", "Mobile", "Laptop", "Tablet", "Mobile"],
    "quantity": [2, 3, 1, 4, 2, 1, 5, 2],
    "sales":    [130000, 96000, 72000, 112000, 82000, 85000, 180000, 90000],
})
```

---

# A. Sorting, Aggregation and `groupby()`

## 4.1 Sorting

```python
df.sort_values("sales")                                       # ascending
df.sort_values("sales", ascending=False)                      # descending
df.sort_values(["city", "sales"], ascending=[True, False])    # by city A-Z, then sales high-low
df.sort_index()                                               # by index
df.nlargest(3, "sales")                                       # faster when you need only a few rows
```

## 4.2 Aggregation

An **aggregation** reduces many values to one: `sum`, `mean`, `median`, `min`, `max`, `std`, `var`, `nunique`, and `count` (non-missing values only).

```python
df["sales"].sum()
df["sales"].agg(["sum", "mean", "median", "min", "max"])      # several at once
```

## 4.3 `groupby()`

`groupby()` follows **split → apply → combine**: split rows by key, aggregate each group, return one row per group.

```python
df.groupby("city")["sales"].sum()
df.groupby("category")["sales"].agg(["sum", "mean"])
df.groupby(["city", "category"])["sales"].sum()          # two keys -> hierarchical index
```

For reports, use **named aggregations** (`new_name=("column", "function")`):

```python
kpi = (
    df.groupby("city")
      .agg(
          total_sales=("sales", "sum"),
          average_sale=("sales", "mean"),
          transactions=("sales", "count"),
          total_quantity=("quantity", "sum"),
          unique_customers=("customer", "nunique"),
      )
      .reset_index()                                     # group keys back to normal columns
      .sort_values("total_sales", ascending=False)
)
```

Working with grouped results:

```python
city_sales = df.groupby("city")["sales"].sum()
city_sales.sort_values(ascending=False)
city_sales[city_sales > 200000]          # filter groups
city_sales.idxmax()                      # NAME of the best city (max() gives the value)
```

Counting categories:

```python
df["city"].value_counts()
df["city"].value_counts(normalize=True).mul(100)         # percentages
```

---

# B. Combining DataFrames

Real projects use several tables. Three tools:

| Tool | Purpose |
| --- | --- |
| `concat()` | Stack DataFrames (same columns) |
| `merge()` | Combine tables using a common key (like SQL JOIN) |
| `join()` | Combine using the index |

```text
Same structure?               -> concat()
Different tables + common ID? -> merge()
Index-based combination?      -> join()
```

## 4.4 `concat()`

```python
jan = pd.DataFrame({"customer": ["Amit", "Ravi", "Priya"], "sales": [50000, 35000, 62000]})
feb = pd.DataFrame({"customer": ["Neha", "Rahul", "Kiran"], "sales": [42000, 55000, 38000]})

pd.concat([jan, feb], ignore_index=True)       # stack rows, rebuild index 0..5
```

`axis=0` stacks rows (default); `axis=1` places DataFrames side by side.

## 4.5 `merge()` and Join Types

```python
customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104],
    "customer":    ["Amit", "Ravi", "Priya", "Neha"],
    "city":        ["Jodhpur", "Jaipur", "Delhi", "Mumbai"],
})
orders = pd.DataFrame({
    "order_id":    [5001, 5002, 5003, 5004, 5005],
    "customer_id": [101, 102, 101, 104, 105],
    "sales":       [65000, 32000, 72000, 28000, 41000],
})
```

Customer 103 has no orders; order 5005 belongs to an unknown customer (105).

```python
customers.merge(orders, on="customer_id", how="inner")
```

| `how=` | Keeps | Here |
| --- | --- | --- |
| `"inner"` | Only keys present in **both** | 103 and 105 are dropped |
| `"left"` | All rows of the left table | Priya (103) kept, order columns = `NaN` |
| `"right"` | All rows of the right table | Order 5005 kept, customer columns = `NaN` |
| `"outer"` | Everything from both | Both 103 and 105 kept |

Inner result:

```text
   customer_id customer     city  order_id  sales
0          101     Amit  Jodhpur      5001  65000
1          101     Amit  Jodhpur      5003  72000
2          102     Ravi   Jaipur      5002  32000
3          104     Neha   Mumbai      5004  28000
```

Left join answers: *show every customer, even those who never purchased.*

## 4.6 Merge Options

```python
# Audit unmatched rows
res = customers.merge(orders, on="customer_id", how="outer", indicator=True)
res[res["_merge"] != "both"]            # _merge: left_only / right_only / both

# Several key columns
a.merge(b, on=["product_id", "city"], how="left")

# Key columns with different names
customers.merge(orders, left_on="customer_id", right_on="cust_id")

# Same non-key column name in both tables
a.merge(b, on="customer_id", suffixes=("_customer", "_order"))
```

## 4.7 Merge Safety: `validate` and Row Counts

`validate` makes Pandas raise an error if the key relationship is not what you expect. The orders table has many rows per customer, so orders → customers is **many-to-one**:

```python
orders.merge(customers, on="customer_id", how="left", validate="many_to_one")
```

Options: `"one_to_one"`, `"one_to_many"`, `"many_to_one"`, `"many_to_many"`. The wording refers to the **left → right** direction (so `customers.merge(orders, ...)` would be `"one_to_many"`).

A one-to-many merge legitimately repeats customer rows, but unexpected duplicates in a key silently multiply rows. Always check:

```python
print(len(orders), "->", len(orders.merge(customers, on="customer_id", how="left")))
```

## 4.8 `join()`

`join()` combines on the **index**:

```python
info  = pd.DataFrame({"customer": ["Amit", "Ravi", "Priya"]}, index=[101, 102, 103])
sales = pd.DataFrame({"sales": [65000, 32000, 72000]},        index=[101, 102, 103])

info.join(sales)
```

---

# C. Reshaping Data

Reshaping changes the **structure** of a table without changing its information.

| Function | Direction |
| --- | --- |
| `pivot()` | Long → Wide |
| `pivot_table()` | Long → Wide **with aggregation** |
| `melt()` | Wide → Long |

## 4.9 `pivot()` and `pivot_table()`

```python
long_df = pd.DataFrame({
    "Month":   ["Jan", "Jan", "Feb", "Feb"],
    "Product": ["Laptop", "Mobile", "Laptop", "Mobile"],
    "Sales":   [50000, 30000, 60000, 35000],
})

long_df.pivot(index="Month", columns="Product", values="Sales")
```

```text
Product  Laptop  Mobile
Month
Feb       60000   35000
Jan       50000   30000
```

`pivot()` raises an error if a Month+Product pair appears twice. `pivot_table()` aggregates duplicates:

```python
dup = pd.DataFrame({
    "Month":   ["Jan", "Jan", "Jan", "Feb", "Feb"],
    "Product": ["Laptop", "Laptop", "Mobile", "Laptop", "Mobile"],
    "Sales":   [50000, 55000, 30000, 60000, 35000],
})

dup.pivot_table(index="Month", columns="Product", values="Sales", aggfunc="sum", fill_value=0)
```

```text
Product  Laptop  Mobile
Month
Feb       60000   35000
Jan      105000   30000        # Jan Laptop = 50000 + 55000
```

`aggfunc` can be `"sum"`, `"mean"`, `"count"`, `"max"`, etc. Pivot tables are the standard way to build report tables for Excel, dashboards and Power BI.

## 4.10 `melt()`

```python
wide = pd.DataFrame({
    "Product": ["Laptop", "Mobile", "Tablet"],
    "Jan": [50000, 30000, 20000],
    "Feb": [60000, 35000, 25000],
})

wide.melt(id_vars="Product", var_name="Month", value_name="Sales")
```

```text
  Product Month  Sales
0  Laptop   Jan  50000
1  Mobile   Jan  30000
2  Tablet   Jan  20000
3  Laptop   Feb  60000
...
```

Long format is what most plotting and `groupby` workflows expect (including Seaborn).

## Quick Reference

| Task | Function |
| --- | --- |
| Sort | `sort_values()`, `sort_index()`, `nlargest()` |
| Summarize groups | `groupby().agg(name=("col", "func"))` |
| Stack tables | `concat()` |
| Join on key | `merge(on=, how=, validate=, indicator=)` |
| Join on index | `join()` |
| Long → wide | `pivot()`, `pivot_table()` |
| Wide → long | `melt()` |
