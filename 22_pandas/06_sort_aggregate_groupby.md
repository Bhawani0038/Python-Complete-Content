# Sorting, Aggregation & `groupby()`

Use this sample DataFrame for the examples below:

```python
import pandas as pd

df = pd.DataFrame({
    "customer": ["Amit", "Ravi", "Priya", "Neha", "Rahul", "Kiran", "Vikas", "Pooja"],
    "city": ["Jodhpur", "Jaipur", "Delhi", "Mumbai", "Jodhpur", "Delhi", "Jaipur", "Mumbai"],
    "category": ["Laptop", "Mobile", "Laptop", "Tablet", "Mobile", "Laptop", "Tablet", "Mobile"],
    "quantity": [2, 3, 1, 4, 2, 1, 5, 2],
    "sales": [130000, 96000, 72000, 112000, 82000, 85000, 180000, 90000]
})
```

## Sorting

```python
df.sort_values("sales")                                  # ascending
df.sort_values("sales", ascending=False)                 # descending
df.sort_values(["city", "sales"], ascending=[True, False])
df.sort_index(ascending=False)
df.nlargest(3, "sales")
df.nsmallest(3, "sales")
```

`nlargest()` and `nsmallest()` are preferable when only a few extreme rows are needed.

## Aggregation

Common Series summaries include `sum()`, `mean()`, `median()`, `min()`, `max()`,
`count()` (non-missing values), `std()`, `var()`, and `nunique()`. Calculate
several at once:

```python
df["sales"].agg(["sum", "mean", "min", "max", "median"])
```

## Grouping and aggregating

`groupby()` splits rows by key, applies an aggregation to each group, and returns one result per group:

```python
df.groupby("city")["sales"].sum()
df.groupby("category")["sales"].agg(["sum", "mean"])
df.groupby(["city", "category"])["sales"].sum()
```

Use named aggregations for readable reports. Multiple keys produce a
hierarchical index; `.reset_index()` makes the keys regular columns.

```python
kpi = (
    df.groupby("city")
    .agg(
        total_sales=("sales", "sum"),
        average_sales=("sales", "mean"),
        highest_sale=("sales", "max"),
        transactions=("sales", "count"),
        total_quantity=("quantity", "sum"),
        unique_customers=("customer", "nunique")
    )
    .reset_index()
    .sort_values("total_sales", ascending=False)
)
```

`value_counts()` summarizes categories; `normalize=True` returns proportions:

```python
df["city"].value_counts()
df["city"].value_counts(normalize=True).mul(100)  # percentage
```

Sort or filter grouped results as needed:

```python
city_sales = df.groupby("city")["sales"].sum()
city_sales.sort_values(ascending=False)
city_sales[city_sales > 200000]
city_sales.idxmax()  # label of the largest total; max() returns the value
```

# Combining DataFrames

In real Data Science projects, data usually comes from **multiple tables/files**.

Main Pandas tools:

* `concat()` → stack DataFrames
* `merge()` → combine tables using a common key
* `join()` → combine mainly using index

---

## 1. `concat()` — Combine DataFrames

### Vertical Concatenation

Suppose January and February sales are stored separately:

```python
import pandas as pd

jan = pd.DataFrame({
    "customer": ["Amit", "Ravi", "Priya"],
    "sales": [50000, 35000, 62000]
})

feb = pd.DataFrame({
    "customer": ["Neha", "Rahul", "Kiran"],
    "sales": [42000, 55000, 38000]
})

sales = pd.concat([jan, feb], ignore_index=True)

print(sales)
```

Output:

```text
  customer  sales
0     Amit  50000
1     Ravi  35000
2    Priya  62000
3     Neha  42000
4    Rahul  55000
5    Kiran  38000
```

### Important

```python
pd.concat([jan, feb], ignore_index=True)
```

* `axis=0` → rows
* `axis=1` → columns
* `ignore_index=True` → creates a new index

---

# 2. `merge()` — Combine Tables Using a Key

This is extremely important in Data Analysis.

### Customers table

```python
customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104],
    "customer": ["Amit", "Ravi", "Priya", "Neha"],
    "city": ["Jodhpur", "Jaipur", "Delhi", "Mumbai"]
})
```

### Orders table

```python
orders = pd.DataFrame({
    "order_id": [5001, 5002, 5003, 5004, 5005],
    "customer_id": [101, 102, 101, 104, 105],
    "sales": [65000, 32000, 72000, 28000, 41000]
})
```

Both tables have:

```text
customer_id
```

So we can merge them.

---

## 3. Inner Join

```python
result = customers.merge(
    orders,
    on="customer_id",
    how="inner"
)

print(result)
```

Only matching `customer_id` values are returned.

```text
customer_id customer      city  order_id  sales
101         Amit          Jodhpur   5001   65000
102         Ravi          Jaipur    5002   32000
101         Amit          Jodhpur   5003   72000
104         Neha          Mumbai    5004   28000
```

`105` is not present in `customers`, so it is excluded.

---

# 4. Left Join

```python
result = customers.merge(
    orders,
    on="customer_id",
    how="left"
)
```

**All customers are preserved.**

If a customer has no order, Pandas gives `NaN`.

Useful question:

> Show me every customer, even customers who have never purchased.

---

# 5. Right Join

```python
result = customers.merge(
    orders,
    on="customer_id",
    how="right"
)
```

All records from `orders` are preserved.

Useful when the **right DataFrame is your main dataset**.

---

# 6. Outer Join

```python
result = customers.merge(
    orders,
    on="customer_id",
    how="outer"
)
```

Keeps everything from both tables.

This is useful for finding:

* Customers without orders
* Orders without valid customers
* Missing relationships

---

# 7. `indicator=True`

Very useful for data auditing.

```python
result = customers.merge(
    orders,
    on="customer_id",
    how="outer",
    indicator=True
)

print(result)
```

Pandas creates:

```text
_merge
```

Possible values:

```text
left_only
right_only
both
```

You can then find unmatched records:

```python
result[result["_merge"] != "both"]
```

---

# 8. Merge on Multiple Columns

Sometimes one column is not enough to identify a record.

```python
result = sales.merge(
    price,
    on=["product_id", "city"],
    how="left"
)
```

Multiple keys:

```python
on=["product_id", "city"]
```

---

# 9. Different Column Names

Suppose one table has:

```text
customer_id
```

and another has:

```text
cust_id
```

Use:

```python
result = customers.merge(
    orders,
    left_on="customer_id",
    right_on="cust_id",
    how="left"
)
```

---

# 10. Duplicate Column Names

Suppose both tables contain:

```text
city
```

Pandas automatically creates suffixes.

You can control them:

```python
result = df1.merge(
    df2,
    on="customer_id",
    suffixes=("_customer", "_order")
)
```

Result:

```text
city_customer
city_order
```

---

# 11. `validate()` — Production Data Checking

This is very useful in real projects.

If each customer should appear only once in `customers`:

```python
result = customers.merge(
    orders,
    on="customer_id",
    how="left",
    validate="many_to_one"
)
```

Meaning:

```text
Many orders → One customer
```

If the relationship is wrong, Pandas raises an error instead of silently producing incorrect data.

---

# 12. `join()`

`join()` is commonly used when working with indexes.

```python
customer_info = pd.DataFrame({
    "customer": ["Amit", "Ravi", "Priya"]
}, index=[101, 102, 103])

sales = pd.DataFrame({
    "sales": [65000, 32000, 72000]
}, index=[101, 102, 103])

result = customer_info.join(sales)

print(result)
```

Output:

```text
     customer  sales
101  Amit      65000
102  Ravi      32000
103  Priya     72000
```

---

## `concat()` vs `merge()` vs `join()`

| Method     | Main Purpose               |
| ---------- | -------------------------- |
| `concat()` | Stack/append DataFrames    |
| `merge()`  | Combine using columns/keys |
| `join()`   | Combine mainly using index |

### Simple rule

```text
Same structure?
      ↓
   concat()

Different tables + common ID?
      ↓
    merge()

Index-based combination?
      ↓
     join()
```

---

## Important Real-World Pitfall

Suppose:

```python
customers
```

has one row per customer.

But:

```python
orders
```

has multiple orders per customer.

Then:

```python
customers.merge(orders, on="customer_id")
```

will create **multiple rows for customers having multiple orders**.

This is normally correct for a one-to-many relationship, but you should always check the row count after a merge.

### Practical check

```python
print("Before:", len(customers))

result = customers.merge(
    orders,
    on="customer_id",
    how="left"
)

print("After:", len(result))
```

This helps detect unexpected row multiplication.

---

### Module 7 Keywords

```text
concat()
merge()
join()
inner join
left join
right join
outer join
on=
left_on=
right_on=
suffixes=
indicator=True
validate=
one-to-one
one-to-many
many-to-one
```