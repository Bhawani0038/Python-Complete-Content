# Pandas Module — Part 3: Transformation, Text & Categorical Data

**Transformation** means changing existing data or creating new columns so that the dataset becomes useful for analysis or ML.

> Uses the 8-row sales `df` from [Part 2](02_selection_filtering_and_cleaning.md), with an extra `quantity` column added here:

```python
df["quantity"] = [2, 3, 1, 4, 2, 1, 5, 2]
```

---

# A. Transformation

## 3.1 Creating Columns

Arithmetic works on whole columns at once (**vectorization**):

```python
df["total_sales"] = df["quantity"] * df["sales"]
df["discount"]    = df["total_sales"] * 0.10
df["final_amount"] = df["total_sales"] - df["discount"]
```

> **Principle:** prefer vectorized column operations over `apply(..., axis=1)`. They are shorter and much faster. `df.apply(lambda row: row["quantity"] * row["sales"], axis=1)` gives the same result but is slow on large data.

## 3.2 Conditional Columns

Three tools, from simplest to most flexible:

```python
# loc: assign to rows matching a condition
df["customer_type"] = "Regular"
df.loc[df["total_sales"] >= 100000, "customer_type"] = "High Value"

# np.where: two outcomes
df["customer_type"] = np.where(df["total_sales"] >= 100000, "High Value", "Regular")

# np.select: several outcomes; the FIRST matching condition wins
conditions = [df["total_sales"] >= 120000, df["total_sales"] >= 90000]
choices    = ["Premium", "Gold"]
df["customer_type"] = np.select(conditions, choices, default="Regular")
```

Order the `np.select` conditions from most to least restrictive.

## 3.3 `map()`, `replace()` and `apply()`

```python
codes = {"Jodhpur": "JDH", "Jaipur": "JAI", "Delhi": "DEL", "Mumbai": "MUM"}
df["city_code"] = df["city"].map(codes)

df["category"] = df["category"].replace({"Laptop": "Computer", "Mobile": "Smartphone"})
```

| | `map()` | `replace()` |
| --- | --- | --- |
| Values not in the dictionary | Become `NaN` | Stay unchanged |
| Typical use | Encode / look up every value | Fix a few specific values |

`apply()` runs a custom function and should be the last resort:

```python
df["city_len"] = df["city"].apply(len)       # only when no vectorized method exists
```

## 3.4 Binning Numeric Data

```python
# cut: fixed ranges you define
df["sales_level"] = pd.cut(df["total_sales"], bins=[0, 50000, 100000, float("inf")],
                           labels=["Low", "Medium", "High"])

# qcut: equal-sized groups based on quantiles
df["sales_quartile"] = pd.qcut(df["total_sales"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])
```

`cut()` → fixed ranges (e.g. age bands, salary bands). `qcut()` → groups with roughly equal counts (e.g. top 25% of customers).

## 3.5 Structural Changes

```python
df = df.rename(columns={"sales": "unit_price", "quantity": "units_sold"})   # rename some columns
df = df[["customer", "city", "category", "units_sold", "unit_price"]]       # select/reorder columns
df.insert(2, "region", ["West", "North", "North", "West", "West", "North", "North", "West"])  # at position 2
df = df.drop(columns=["region"])                                           # remove column(s)
```

Use `rename()` (not `df.columns = [...]`) when only a few names change, since assigning the whole list silently breaks if the column order changes.

## 3.6 Transformation Pipeline

```python
df = pd.read_csv("sales.csv")

df["customer"]      = df["customer"].str.strip().str.title()
df["total_sales"]   = df["quantity"] * df["price"]
df["final_amount"]  = df["total_sales"] * 0.90
df["customer_type"] = np.where(df["total_sales"] >= 100000, "High Value", "Regular")
```

---

# B. Text Data

Part 2 used `.str.strip()` and `.str.title()` for cleaning. Here we search, replace and extract.

```python
people = pd.DataFrame({
    "Name":  ["Rahul Sharma", "Priya Singh", "Amit Kumar", "Neha Gupta"],
    "Email": ["rahul@gmail.com", "priya@yahoo.com", "amit@gmail.com", "neha@company.com"],
    "City":  ["Jodhpur", "Jaipur", "Jodhpur", "Delhi"],
})
```

## 3.7 Searching

```python
people[people["City"].str.contains("jodhpur", case=False, na=False)]
people[people["Name"].str.startswith("A", na=False)]
people[people["Email"].str.endswith("@gmail.com", na=False)]
```

- `case=False` ignores case.
- `na=False` treats missing values as "no match"; without it, filtering fails when the column has `NaN`.
- `contains()` interprets its pattern as a **regular expression** by default. Use `regex=False` for literal text with characters like `.` or `+`.

## 3.8 Replace, Length, Split

```python
people["City"]  = people["City"].str.replace("Jodhpur", "JDH", regex=False)
people["Len"]   = people["Name"].str.len()          # useful for spotting suspicious values

people["Username"] = people["Email"].str.split("@").str[0]
people["Domain"]   = people["Email"].str.split("@").str[1]
```

## 3.9 Extracting Patterns with Regex

A **regular expression** (regex) describes a text pattern. `\d+` means "one or more digits". Parentheses mark the part to extract.

```python
orders = pd.DataFrame({"Order": ["ORD-1025", "ORD-2048", "ORD-3099"]})
orders["Number"] = orders["Order"].str.extract(r"(\d+)", expand=False)
```

```text
      Order Number
0  ORD-1025   1025
1  ORD-2048   2048
2  ORD-3099   3099
```

The result is text; convert with `astype(int)` if needed.

---

# C. Categorical Data and Performance

## 3.10 Changing Types with `astype()`

```python
df["units_sold"] = df["units_sold"].astype("int64")
df["category"]   = df["category"].astype("category")
```

The `category` dtype stores each distinct value once, which saves memory when a column has few distinct values repeated many times (city, category, status). Check the effect with `df.memory_usage(deep=True)`.

## 3.11 Performance Checklist

- Use vectorized operations instead of row-wise `apply()` or Python loops.
- Load only needed columns (`usecols`) and rows (`nrows`) when reading (Part 1).
- Use `category` for low-cardinality text columns.

## Quick Reference

| Method | Use |
| --- | --- |
| `df["new"] = ...` | Create column |
| `loc`, `np.where`, `np.select` | Conditional values |
| `map()` / `replace()` | Dictionary mapping / value replacement |
| `pd.cut()` / `pd.qcut()` | Fixed / quantile bins |
| `rename()`, `insert()`, `drop()` | Change structure |
| `.str.contains/startswith/endswith` | Search text |
| `.str.replace/split/extract/len` | Modify and extract text |
| `astype("category")` | Memory-efficient categories |
