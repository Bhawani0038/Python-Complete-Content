# Pandas Module — Part 1: Basics & Data Loading

Pandas is a Python library for data manipulation, cleaning, analysis and preparation of data for Machine Learning and reporting.

```text
Raw Data -> Pandas -> Clean -> Transform -> Analyze -> Visualize -> ML / Reporting
```

## Module Roadmap

The original 20-topic roadmap is covered in five files. Each concept is taught fully in one place and only referenced elsewhere.

| File | Topics |
| --- | --- |
| **01 Basics & Data Loading** (this file) | Series, DataFrame, inspection, reading/saving CSV, Excel, JSON, SQL |
| [02 Selection, Filtering & Cleaning](02_selection_filtering_and_cleaning.md) | `loc`/`iloc`, boolean filters, `query()`, missing values, duplicates, wrong values, data types |
| [03 Transformation, Text & Categorical Data](03_transformation_text_and_categorical.md) | New columns, conditions, `map`/`replace`/`apply`, binning, renaming, `.str`, regex, `category`, performance |
| [04 Sorting, Grouping, Combining & Reshaping](04_sorting_grouping_combining_reshaping.md) | `sort_values`, aggregation, `groupby`, `concat`/`merge`/`join`, `pivot`/`pivot_table`/`melt` |
| [05 Time, Indexing, Analysis & Visualization](05_time_indexing_analysis_visualization.md) | Datetime, resampling, MultiIndex, statistics, KPIs, outliers, plotting |

---

## 1.1 Installation and Import

```bash
pip install pandas
```

```python
import pandas as pd
import numpy as np

print(pd.__version__)
```

`pd` and `np` are the standard aliases. Later files assume these imports.

## 1.2 Series — One Column of Data

A **Series** is one-dimensional labelled data, like a single Excel column. The labels are called the **index**.

```python
marks = pd.Series([75, 82, 68], index=["Amit", "Ravi", "Priya"])

marks["Ravi"]        # 82  -> access by label
marks.iloc[1]        # 82  -> access by position
```

Without a custom index, labels are 0, 1, 2, … Prefer `.loc[label]` and `.iloc[position]` over plain `marks[...]`, because plain indexing is ambiguous when the labels are integers (see Part 2).

## 1.3 DataFrame — A Table

A **DataFrame** is two-dimensional tabular data: each column is a Series, all sharing one index. It is the main Pandas structure.

**From a dictionary** (the most common way to build sample data):

```python
df = pd.DataFrame({
    "customer": ["Amit", "Ravi", "Priya", "Neha"],
    "city":     ["Jodhpur", "Jaipur", "Delhi", "Mumbai"],
    "sales":    [25000, 32000, 28000, 41000],
})
```

```text
  customer     city  sales
0     Amit  Jodhpur  25000
1     Ravi   Jaipur  32000
2    Priya    Delhi  28000
3     Neha   Mumbai  41000
```

**From a list of rows** (give column names explicitly):

```python
rows = [["Amit", "Jodhpur", 25000], ["Ravi", "Jaipur", 32000]]
pd.DataFrame(rows, columns=["customer", "city", "sales"])
```

**From a NumPy array:**

```python
arr = np.array([[25, 35000], [28, 42000]])
pd.DataFrame(arr, columns=["age", "salary"])
```

Selecting columns (rows are covered in Part 2):

```python
df["customer"]                  # one column  -> Series
df[["customer", "sales"]]       # list of names -> DataFrame
```

## 1.4 Inspecting a DataFrame

Always look at the data before working on it.

| Command | Purpose |
| --- | --- |
| `df.head()` / `df.tail()` | First / last rows (`head(10)` for 10 rows) |
| `df.shape` | `(rows, columns)` |
| `df.columns` / `df.index` | Column names / row labels |
| `df.dtypes` | Data type of each column |
| `df.info()` | Structure, dtypes and non-null counts (reveals missing values) |
| `df.describe()` | Summary statistics for numeric columns |
| `df.size` / `df.ndim` | Number of values / dimensions |

---

## 1.5 Reading Data

Data usually comes from files, URLs or databases.

```python
df = pd.read_csv("sales.csv")
df = pd.read_excel("sales.xlsx")                           # first sheet
df = pd.read_excel("sales.xlsx", sheet_name="January")     # one sheet
sheets = pd.read_excel("sales.xlsx", sheet_name=None)      # dict of all sheets
df = pd.read_json("sales.json")                            # list of records
df = pd.read_csv("https://example.com/data.csv")           # public URL
```

SQL (using the standard library's `sqlite3` for the example):

```python
import sqlite3

conn = sqlite3.connect("company.db")
df = pd.read_sql("SELECT * FROM employees", conn)
conn.close()
```

### Useful `read_csv()` parameters

```python
df = pd.read_csv(
    "sales.csv",
    sep=";",                          # separator, if not a comma
    encoding="utf-8",                 # try "latin1" after a UnicodeDecodeError
    usecols=["customer", "sales"],    # load only the columns you need
    nrows=100,                        # load only the first 100 rows (good for testing)
    na_values=["NA", "N/A", "-"],     # treat these text values as missing
    parse_dates=["date"],             # convert to datetime while reading
    dtype={"customer_id": "string"},  # force specific data types
)
```

| Parameter | Purpose |
| --- | --- |
| `sep` | Separator |
| `encoding` | File encoding |
| `header`, `names` | Header row / custom column names |
| `usecols`, `nrows`, `skiprows` | Read only part of the file (important for large files) |
| `na_values` | Extra strings to treat as missing (`NaN`) |
| `dtype` | Force column types |
| `parse_dates` | Parse columns as dates |

## 1.6 Saving Data

```python
df.to_csv("output.csv", index=False)        # index=False avoids an extra index column
df.to_excel("output.xlsx", index=False)
df.to_json("output.json", orient="records", indent=4)
```

## 1.7 Standard First Look

Every analysis starts the same way:

```python
df = pd.read_csv("sales.csv")

df.head()
df.shape
df.info()
df.describe()
```

Then move on to cleaning (Part 2).

## Recap

```text
Series      = one labelled column
DataFrame   = table of Series sharing an index
read_*      = load      to_*   = save
head / shape / info / describe = first look
```
