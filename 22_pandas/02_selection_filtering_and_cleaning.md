# Pandas Module — Part 2: Selection, Filtering & Cleaning

First we learn to pick the rows and columns we need, then use that skill to fix messy data.

> Assumes `import pandas as pd` and `import numpy as np` from [Part 1](01_basics_and_data_loading.md).

---

# A. Selecting and Filtering

This dataset is reused through the rest of the module:

```python
df = pd.DataFrame({
    "customer": ["Amit", "Ravi", "Priya", "Neha", "Rahul", "Kiran", "Vikas", "Pooja"],
    "city":     ["Jodhpur", "Jaipur", "Delhi", "Mumbai", "Jodhpur", "Delhi", "Jaipur", "Mumbai"],
    "category": ["Laptop", "Mobile", "Laptop", "Tablet", "Mobile", "Laptop", "Tablet", "Mobile"],
    "sales":    [65000, 32000, 72000, 28000, 41000, 85000, 36000, 45000],
})
```

## 2.1 `iloc` and `loc`

```text
iloc -> integer positions      loc -> labels / names
```

```python
df.iloc[0]               # first row
df.iloc[[0, 3, 5]]       # rows at positions 0, 3, 5
df.iloc[0:4]             # positions 0,1,2,3  (end is EXCLUDED)
df.iloc[0, 3]            # row 0, column 3 -> 65000
df.iloc[0:4, 0:3]        # first 4 rows, first 3 columns

df.loc[0, "customer"]                       # 'Amit'
df.loc[0:3, ["customer", "sales"]]          # labels 0,1,2,3 (end is INCLUDED)
```

| | `loc` | `iloc` |
| --- | --- | --- |
| Based on | Labels | Positions |
| Slice end | Included | Excluded |
| Columns by | Names | Numbers |

The slice-end difference is the most common source of off-by-one mistakes.

## 2.2 Boolean Filtering

Put a condition inside `df[...]` and Pandas keeps the rows where it is `True`.

```python
df[df["sales"] > 50000]
df[df["city"] == "Delhi"]            # == compares, = assigns
```

Combine conditions with `&` (and), `|` (or), `~` (not), and **wrap each condition in parentheses**:

```python
df[(df["city"] == "Delhi") & (df["sales"] > 70000)]
```

Cleaner alternatives:

```python
df[df["city"].isin(["Delhi", "Mumbai", "Jaipur"])]     # several allowed values
df[~df["city"].isin(["Delhi", "Mumbai"])]              # exclude values
df[df["sales"].between(40000, 70000)]                  # inclusive range
df.query("sales > 50000 and city == 'Delhi'")          # readable multi-condition filter
```

Filter rows **and** choose columns at once with `loc`:

```python
df.loc[(df["category"] == "Laptop") & (df["sales"] > 60000), ["customer", "city", "sales"]]
```

## 2.3 Top, Maximum and Minimum

```python
df.nlargest(3, "sales")               # top 3 rows (nsmallest for bottom)
df["sales"].max()                     # the highest VALUE
df.loc[df["sales"].idxmax()]          # the ROW with the highest value (idxmin for lowest)
```

`max()` returns a value; `idxmax()` returns the index label of that value.

---

# B. Data Cleaning

Real data is rarely clean. Typical problems: missing values, duplicates, wrong types, extra spaces, inconsistent text, invalid values, outliers.

## 2.4 A Dirty Dataset

```python
raw = pd.DataFrame({
    "customer": ["Amit", "Ravi", " Priya ", "Neha", "Amit", "Rahul", "Kiran", None],
    "age":      [25, 28, 24, None, 25, 150, 31, 29],
    "city":     ["Jodhpur", "Jaipur", "Delhi", "Mumbai", "Jodhpur", "jodhpur", "Delhi", "Jaipur"],
    "sales":    [65000, 32000, None, 28000, 65000, -5000, 85000, 41000],
})
```

Planted problems: missing customer/age/sales, duplicate Amit, age 150, sales −5000, extra spaces, `"Jodhpur"` vs `"jodhpur"`.

## 2.5 Detect Missing Values

```python
raw.isna().sum()                       # count per column (isnull() is identical)
raw.isna().mean() * 100                # percentage per column
raw[raw.isna().any(axis=1)]            # rows with ANY missing value
raw[raw["customer"].isna()]            # rows where one column is missing
```

`axis=1` means "check across the columns of each row". Percentages are more useful than counts when deciding what to do.

## 2.6 Handle Missing Values

**Remove**, but only where it makes sense:

```python
raw.dropna()                           # drops any row with a missing value (often too aggressive)
raw.dropna(subset=["customer"])        # drop only if the essential column is missing
```

**Fill**:

```python
raw["customer"] = raw["customer"].fillna("Unknown")
raw["age"]      = raw["age"].fillna(raw["age"].median())
```

Choose the fill value by the column's meaning. The median resists outliers; the mean can be pulled by extreme values. Fill *after* fixing invalid values (2.10), so that wrong values don't affect the median.

## 2.7 Duplicates

```python
raw.duplicated().sum()                 # count
raw[raw.duplicated()]                  # show duplicates
raw = raw.drop_duplicates()            # remove (keeps the first occurrence)
raw.drop_duplicates(subset=["customer"])   # only if `customer` really defines a unique record
```

Using `subset` on a column that is not truly unique silently deletes valid data.

## 2.8 Text Cleaning

The `.str` accessor applies string methods to a whole column (searching and extraction are covered in Part 3).

```python
raw["customer"] = raw["customer"].str.strip()     # " Priya " -> "Priya"
raw["city"]     = raw["city"].str.title()         # "jodhpur" -> "Jodhpur"
```

Other cases: `.str.lower()`, `.str.upper()`. For several columns, loop:

```python
for col in ["customer", "city"]:
    raw[col] = raw[col].str.strip().str.title()
```

Missing values stay missing (`NaN`) during `.str` operations.

## 2.9 Data Types

```python
raw.dtypes
```

Convert safely:

```python
raw["sales"] = pd.to_numeric(raw["sales"], errors="coerce")        # invalid text -> NaN
raw["age"]   = raw["age"].astype("Int64")                          # nullable integer
dates = pd.to_datetime(pd.Series(["2026-01-10", "invalid"]), errors="coerce")   # invalid -> NaT
```

- `astype("int64")` fails if the column has `NaN`; use `"Int64"` (capital I), which allows missing values.
- `NaT` means "Not a Time" (the missing value for dates).
- `errors="coerce"` turns unconvertible values into missing values instead of raising errors.

## 2.10 Invalid Values

Missing data is easy to detect; wrong values need business rules.

```python
raw[raw["age"] > 100]                          # age 150?
raw[raw["sales"] < 0]                          # negative sales?

raw.loc[raw["age"] > 100, "age"] = np.nan      # mark as missing, then fill (2.6)
raw.loc[raw["sales"] < 0, "sales"] = np.nan
```

Do not delete extreme values automatically. They may be real. Check them against the business context (outlier detection is covered in Part 5).

## 2.11 A Complete Cleaning Pipeline

```python
df = pd.read_csv("sales.csv")

df = df.drop_duplicates()

for col in ["customer", "city"]:
    df[col] = df[col].str.strip().str.title()

df["age"]   = pd.to_numeric(df["age"], errors="coerce")
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

df.loc[df["age"] > 100, "age"] = np.nan          # invalid -> missing
df.loc[df["sales"] < 0, "sales"] = np.nan

df["age"]   = df["age"].fillna(df["age"].median())
df["sales"] = df["sales"].fillna(df["sales"].median())
```

Order matters: convert types and standardize text first, then mark invalid values, then fill. Standardize text *before* dropping duplicates when casing or spaces differ (`"Amit"` vs `" amit"`), otherwise duplicates are missed.

```text
Inspect -> Duplicates -> Text -> Types -> Invalid values -> Missing values -> Clean data
```

## Quick Reference

| Task | Function |
| --- | --- |
| Detect / remove / fill missing | `isna()`, `dropna()`, `fillna()` |
| Detect / remove duplicates | `duplicated()`, `drop_duplicates()` |
| Standardize text | `.str.strip()`, `.str.title()`, `.str.lower()` |
| Convert types | `astype()`, `pd.to_numeric()`, `pd.to_datetime()` |
| Select by label / position | `loc`, `iloc` |
| Filter | `df[cond]`, `isin()`, `between()`, `query()` |
