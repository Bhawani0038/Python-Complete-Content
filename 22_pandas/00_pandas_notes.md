# Pandas for Data Science & Data Analysis

## Complete Learning Roadmap

| Module                   | Topics                                                                   |
| ------------------------ | ------------------------------------------------------------------------ |
| 1. Pandas Fundamentals   | Introduction, installation, import, Series, DataFrame                    |
| 2. Creating Data         | Lists, dictionaries, NumPy arrays, CSV, Excel, JSON                      |
| 3. Inspecting Data       | `head()`, `tail()`, `shape`, `columns`, `dtypes`, `info()`, `describe()` |
| 4. Selecting Data        | Columns, rows, `loc`, `iloc`, boolean filtering                          |
| 5. Data Cleaning         | Missing values, duplicates, incorrect values, data types                 |
| 6. Data Transformation   | `apply()`, `map()`, `replace()`, `astype()`, string operations           |
| 7. Sorting & Ranking     | `sort_values()`, `sort_index()`, ranking                                 |
| 8. GroupBy               | `groupby()`, aggregation, multiple aggregations                          |
| 9. Aggregation           | `sum()`, `mean()`, `median()`, `count()`, `min()`, `max()`               |
| 10. Combining Data       | `concat()`, `merge()`, `join()`                                          |
| 11. Reshaping Data       | `pivot()`, `pivot_table()`, `melt()`                                     |
| 12. Date & Time          | `datetime`, date filtering, resampling                                   |
| 13. Text Data            | `str.lower()`, `contains()`, `replace()`, regex                          |
| 14. Categorical Data     | Categories, memory optimization                                          |
| 15. Advanced Indexing    | MultiIndex, hierarchical data                                            |
| 16. Statistical Analysis | Correlation, covariance, distributions                                   |
| 17. Data Analysis        | KPIs, trends, segmentation, outliers                                     |
| 18. Visualization        | Pandas with Matplotlib                                                   |
| 19. Performance          | Vectorization, memory usage, efficient operations                        |
| 20. Real Projects        | Sales, customers, healthcare, finance, e-commerce datasets               |

---

Pandas Fundamentals

## 1. What is Pandas?

**Pandas** is a Python library used for:

* Data manipulation
* Data cleaning
* Data analysis
* Data transformation
* Statistical analysis
* Working with CSV/Excel/JSON data
* Preparing data for Machine Learning
* Exploratory Data Analysis (EDA)

Typical workflow:

```text
Raw Data
   ↓
Pandas
   ↓
Clean Data
   ↓
Transform
   ↓
Analyze
   ↓
Visualize
   ↓
Machine Learning / Reporting
```

---

# 2. Installing Pandas

```bash
pip install pandas
```

Check installation:

```python
import pandas as pd

print(pd.__version__)
```

`pd` is the standard alias used for Pandas.

---

# 3. Pandas Data Structures

Pandas mainly provides two important data structures:

```text
Pandas
│
├── Series
│
└── DataFrame
```

### Series

One-dimensional data:

```text
10
20
30
40
```

### DataFrame

Two-dimensional tabular data:

```text
Name       Age    Salary
Amit       25     35000
Ravi       28     42000
Priya      24     38000
```

---

# 4. Pandas Series

A Series is similar to a single column in an Excel sheet.

```python
import pandas as pd

marks = pd.Series([75, 82, 68, 91, 88])

print(marks)
```

Output:

```text
0    75
1    82
2    68
3    91
4    88
dtype: int64
```

The left side is the **index**.

```text
Index    Value
  0        75
  1        82
  2        68
  3        91
  4        88
```

---

# 5. Accessing Series Values

```python
print(marks[0])
```

Output:

```text
75
```

Multiple values:

```python
print(marks[1:4])
```

Output:

```text
1    82
2    68
3    91
dtype: int64
```

---

# 6. Creating Series with Custom Index

```python
marks = pd.Series(
    [75, 82, 68],
    index=["Amit", "Ravi", "Priya"]
)

print(marks)
```

Output:

```text
Amit     75
Ravi     82
Priya    68
dtype: int64
```

Now:

```python
print(marks["Ravi"])
```

Output:

```text
82
```

---

# 7. DataFrame

A DataFrame is the most important Pandas structure for Data Science.

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Amit", "Ravi", "Priya", "Neha"],
    "age": [25, 28, 24, 27],
    "salary": [35000, 42000, 38000, 45000]
})

print(df)
```

Output:

```text
    name  age  salary
0   Amit   25   35000
1   Ravi   28   42000
2  Priya   24   38000
3   Neha   27   45000
```

Think of a DataFrame as:

```text
             Columns
        ↓       ↓       ↓
      name     age    salary
        │       │       │
        ├───────┼───────┤
        │       │       │
        ├───────┼───────┤
        │       │       │
        └───────┴───────┘
              Rows
```

---

# 8. DataFrame Columns

Get all column names:

```python
print(df.columns)
```

Output:

```text
Index(['name', 'age', 'salary'], dtype='object')
```

Select one column:

```python
print(df["name"])
```

Select multiple columns:

```python
print(df[["name", "salary"]])
```

Output:

```text
    name  salary
0   Amit   35000
1   Ravi   42000
2  Priya   38000
3   Neha   45000
```

---

# 9. Basic DataFrame Inspection

These commands are extremely important in Data Analysis.

### First 5 rows

```python
df.head()
```

### First 10 rows

```python
df.head(10)
```

### Last 5 rows

```python
df.tail()
```

### Number of rows and columns

```python
df.shape
```

Output:

```text
(4, 3)
```

Meaning:

```text
4 rows
3 columns
```

### Column names

```python
df.columns
```

### Data types

```python
df.dtypes
```

### Complete information

```python
df.info()
```

### Statistical summary

```python
df.describe()
```

---

# 10. Most Important Inspection Commands

| Command         | Purpose                    |
| --------------- | -------------------------- |
| `df.head()`     | First rows                 |
| `df.tail()`     | Last rows                  |
| `df.shape`      | Rows and columns           |
| `df.columns`    | Column names               |
| `df.dtypes`     | Data types                 |
| `df.info()`     | Structure + missing values |
| `df.describe()` | Statistical summary        |
| `df.index`      | Index information          |
| `df.size`       | Total number of elements   |
| `df.ndim`       | Number of dimensions       |


---


# Creating and Loading Data in Pandas

In Data Science, data usually comes from **CSV, Excel, JSON, databases, APIs, or Python/NumPy objects**.

---

## 1. Create DataFrame from Dictionary

This is one of the most common ways to create sample data.

```python
import pandas as pd

data = {
    "customer": ["Amit", "Ravi", "Priya", "Neha"],
    "city": ["Jodhpur", "Jaipur", "Delhi", "Mumbai"],
    "sales": [25000, 32000, 28000, 41000]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
  customer     city  sales
0     Amit  Jodhpur  25000
1     Ravi   Jaipur  32000
2    Priya    Delhi  28000
3     Neha   Mumbai  41000
```

---

# 2. DataFrame from List

Suppose the data is available as rows:

```python
data = [
    ["Amit", "Jodhpur", 25000],
    ["Ravi", "Jaipur", 32000],
    ["Priya", "Delhi", 28000],
    ["Neha", "Mumbai", 41000]
]

df = pd.DataFrame(
    data,
    columns=["customer", "city", "sales"]
)

print(df)
```

---

# 3. DataFrame from NumPy Array

Pandas works very closely with NumPy.

```python
import numpy as np
import pandas as pd

data = np.array([
    [25, 35000],
    [28, 42000],
    [24, 38000],
    [31, 51000]
])

df = pd.DataFrame(
    data,
    columns=["age", "salary"]
)

print(df)
```

Output:

```text
   age  salary
0   25   35000
1   28   42000
2   24   38000
3   31   51000
```

---

# 4. Reading CSV Files

CSV is one of the most common formats in Data Science.

Suppose we have:

```text
sales.csv
```

Then:

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print(df)
```

### Recommended initial inspection

```python
print(df.head())
print(df.shape)
print(df.info())
```

---

# 5. CSV with Different Separator

Not every CSV-like file uses commas.

Example:

```text
customer;city;sales
Amit;Jodhpur;25000
Ravi;Jaipur;32000
```

Use:

```python
df = pd.read_csv(
    "sales.csv",
    sep=";"
)
```

---

# 6. CSV with Specific Encoding

Sometimes you may get:

```text
UnicodeDecodeError
```

You can specify encoding:

```python
df = pd.read_csv(
    "sales.csv",
    encoding="utf-8"
)
```

For some legacy files:

```python
df = pd.read_csv(
    "sales.csv",
    encoding="latin1"
)
```

---

# 7. Reading Excel Files

For Excel:

```python
df = pd.read_excel("sales.xlsx")
```

Specific sheet:

```python
df = pd.read_excel(
    "sales.xlsx",
    sheet_name="January"
)
```

Multiple sheets:

```python
data = pd.read_excel(
    "sales.xlsx",
    sheet_name=None
)
```

This returns a dictionary where each key is a sheet name.

---

# 8. Reading JSON

Example JSON:

```json
[
    {
        "name": "Amit",
        "sales": 25000
    },
    {
        "name": "Ravi",
        "sales": 32000
    }
]
```

Read it:

```python
df = pd.read_json("sales.json")

print(df)
```

---

# 9. Reading Data from URL

Pandas can directly read many publicly accessible CSV URLs.

```python
url = "https://example.com/data.csv"

df = pd.read_csv(url)

print(df.head())
```

This is useful when working with:

* Public datasets
* GitHub datasets
* Government datasets
* Google Sheets published as CSV
* Data APIs returning CSV

---

# 10. Reading Data from SQL

Pandas can also work with databases.

Example:

```python
import pandas as pd
import sqlite3

connection = sqlite3.connect("company.db")

query = """
SELECT *
FROM employees
"""

df = pd.read_sql(query, connection)

print(df.head())

connection.close()
```

The important function is:

```python
pd.read_sql()
```

---

# 11. Important `read_csv()` Parameters

`read_csv()` has many useful parameters.

```python
df = pd.read_csv(
    "sales.csv",
    sep=",",
    encoding="utf-8",
    na_values=["NA", "N/A", "-"],
)
```

Common parameters:

| Parameter     | Purpose                  |
| ------------- | ------------------------ |
| `filepath`    | File location            |
| `sep`         | Separator                |
| `encoding`    | File encoding            |
| `header`      | Header row               |
| `names`       | Custom column names      |
| `usecols`     | Read selected columns    |
| `nrows`       | Read limited rows        |
| `skiprows`    | Skip rows                |
| `na_values`   | Define missing values    |
| `dtype`       | Specify data types       |
| `parse_dates` | Convert columns to dates |

---

# 12. Reading Only Selected Columns

Suppose the CSV contains:

```text
customer
city
age
salary
department
```

But you only need:

```text
customer
salary
```

Use:

```python
df = pd.read_csv(
    "employees.csv",
    usecols=["customer", "salary"]
)
```

This is useful for **large datasets** because unnecessary columns don't need to be loaded.

---

# 13. Reading Limited Rows

For testing a large dataset:

```python
df = pd.read_csv(
    "sales.csv",
    nrows=100
)
```

Only the first 100 rows are loaded.

---

# 14. Handling Missing Values While Reading

Suppose your file contains:

```text
customer,sales
Amit,25000
Ravi,NA
Priya,28000
Neha,-
```

Use:

```python
df = pd.read_csv(
    "sales.csv",
    na_values=["NA", "-"]
)
```

Pandas will interpret those values as missing values:

```text
customer    sales
Amit        25000
Ravi        NaN
Priya       28000
Neha        NaN
```

We will study missing-value handling in detail in the **Data Cleaning module**.

---

# 15. Reading Date Columns

Suppose:

```text
date,sales
2026-01-10,25000
2026-01-15,32000
2026-02-03,28000
```

You can convert the date while reading:

```python
df = pd.read_csv(
    "sales.csv",
    parse_dates=["date"]
)
```

Check:

```python
print(df.dtypes)
```

The `date` column will have a datetime type.

---

# 16. Data Analysis Example

Let's create a small sales dataset.

```python
import pandas as pd

df = pd.DataFrame({
    "customer": [
        "Amit", "Ravi", "Priya", "Neha",
        "Rahul", "Kiran", "Vikas", "Pooja"
    ],
    "city": [
        "Jodhpur", "Jaipur", "Delhi", "Mumbai",
        "Jodhpur", "Delhi", "Jaipur", "Mumbai"
    ],
    "category": [
        "Laptop", "Mobile", "Laptop", "Tablet",
        "Mobile", "Laptop", "Tablet", "Mobile"
    ],
    "sales": [
        65000, 32000, 72000, 28000,
        41000, 85000, 36000, 45000
    ]
})

print(df)
```

Now inspect it:

```python
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())
```

This represents a basic **real-world sales analysis workflow**.

---

# 17. Saving a DataFrame

After analysis, you often need to export the result.

### CSV

```python
df.to_csv("sales_output.csv", index=False)
```

`index=False` prevents Pandas from creating an unnecessary index column.

### Excel

```python
df.to_excel(
    "sales_output.xlsx",
    index=False
)
```

### JSON

```python
df.to_json(
    "sales_output.json",
    orient="records",
    indent=4
)
```

---

# 18. The Complete Data Loading Workflow

A practical Pandas workflow often starts like this:

```python
import pandas as pd

# 1. Load
df = pd.read_csv("sales.csv")

# 2. Inspect
print(df.head())
print(df.shape)
print(df.info())

# 3. Understand columns
print(df.columns)
print(df.dtypes)

# 4. Statistical overview
print(df.describe())

# 5. Continue with cleaning
# missing values
# duplicates
# incorrect data
# outliers
# transformations
# analysis
```

This initial stage is often called **data inspection / data understanding**.

---

## Important Keywords

```text
pd.DataFrame()
pd.Series()
pd.read_csv()
pd.read_excel()
pd.read_json()
pd.read_sql()
df.to_csv()
df.to_excel()
df.to_json()

sep
encoding
usecols
nrows
skiprows
na_values
dtype
parse_dates
```


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

This is extremely important in Data Analysis.

Suppose we want customers whose sales are greater than ₹50,000.

```python
df[df["sales"] > 50000]
```

Output:

```text
  customer     city category  sales
0     Amit  Jodhpur   Laptop  65000
2    Priya    Delhi   Laptop  72000
5    Kiran    Delhi   Laptop  85000
```

The condition:

```python
df["sales"] > 50000
```

produces:

```text
True
False
True
False
False
True
False
False
```

Pandas then keeps only the rows where the condition is `True`.

---

# 10. Sales Less Than ₹40,000

```python
df[df["sales"] < 40000]
```

---

# 11. Sales Equal to ₹45,000

```python
df[df["sales"] == 45000]
```

Important:

```text
=   assignment
==  comparison
```

---

# 12. Filtering Text

Find customers from Delhi:

```python
df[df["city"] == "Delhi"]
```

Output:

```text
  customer   city category  sales
2    Priya  Delhi   Laptop  72000
5    Kiran  Delhi   Laptop  85000
```

---

# 13. Multiple Conditions — AND

Suppose:

```text
city = Delhi
AND
sales > 70000
```

Use `&`:

```python
df[
    (df["city"] == "Delhi") &
    (df["sales"] > 70000)
]
```

Output:

```text
  customer   city category  sales
2    Priya  Delhi   Laptop  72000
5    Kiran  Delhi   Laptop  85000
```

### Important

Each condition should normally be enclosed in parentheses:

```python
(condition1) & (condition2)
```

---

# 14. Multiple Conditions — OR

Suppose we want:

```text
Delhi
OR
Mumbai
```

Use `|`:

```python
df[
    (df["city"] == "Delhi") |
    (df["city"] == "Mumbai")
]
```

---

# 15. AND vs OR

| Requirement | Pandas |   |
| ----------- | ------ | - |
| AND         | `&`    |   |
| OR          | `      | ` |
| NOT         | `~`    |   |

Example:

```python
df[(df["sales"] > 40000) & (df["category"] == "Mobile")]
```

---

# 16. `isin()`

Instead of:

```python
df[
    (df["city"] == "Delhi") |
    (df["city"] == "Mumbai") |
    (df["city"] == "Jaipur")
]
```

Use:

```python
df[df["city"].isin(["Delhi", "Mumbai", "Jaipur"])]
```

This is cleaner and easier to maintain.

---

# 17. NOT with `isin()`

Customers who are **not** from Delhi:

```python
df[~df["city"].isin(["Delhi"])]
```

Multiple cities:

```python
df[~df["city"].isin(["Delhi", "Mumbai"])]
```

---

# 18. `between()`

Suppose we need sales between ₹40,000 and ₹70,000:

```python
df[df["sales"].between(40000, 70000)]
```

Output:

```text
  customer     city category  sales
0     Amit  Jodhpur   Laptop  65000
4    Rahul  Jodhpur   Mobile  41000
7    Pooja   Mumbai   Mobile  45000
```

By default, the boundaries are included.

---

# 19. Filtering with `query()`

Pandas provides a very readable way to filter data:

```python
df.query("sales > 50000")
```

Multiple conditions:

```python
df.query("sales > 50000 and city == 'Delhi'")
```

Output:

```text
  customer   city category  sales
2    Priya  Delhi   Laptop  72000
5    Kiran  Delhi   Laptop  85000
```

Another example:

```python
df.query("category == 'Laptop' and sales > 60000")
```

This is particularly useful when working with complex analytical queries.

---

# 20. Selecting Columns After Filtering

Suppose we only want the customer and sales:

```python
df.loc[
    df["sales"] > 50000,
    ["customer", "sales"]
]
```

Output:

```text
  customer  sales
0     Amit  65000
2    Priya  72000
5    Kiran  85000
```

This is a very common real-world pattern.

---

# 21. Practical Analysis Example

### Question

Find all **Laptop** customers whose sales are greater than ₹60,000.

```python
result = df[
    (df["category"] == "Laptop") &
    (df["sales"] > 60000)
]

print(result)
```

Output:

```text
  customer     city category  sales
0     Amit  Jodhpur   Laptop  65000
2    Priya    Delhi   Laptop  72000
5    Kiran    Delhi   Laptop  85000
```

---

# 22. Another Business Question

### Find Delhi customers with sales above ₹70,000.

```python
result = df.query(
    "city == 'Delhi' and sales > 70000"
)

print(result)
```

---

# 23. Selecting Top Sales

We can combine filtering and sorting:

```python
df.sort_values(
    "sales",
    ascending=False
)
```

Output:

```text
  customer     city category  sales
5    Kiran    Delhi   Laptop  85000
2    Priya    Delhi   Laptop  72000
0     Amit  Jodhpur   Laptop  65000
7    Pooja   Mumbai   Mobile  45000
4    Rahul  Jodhpur   Mobile  41000
6    Vikas   Jaipur   Tablet  36000
1     Ravi   Jaipur   Mobile  32000
3     Neha   Mumbai   Tablet  28000
```

Top 3:

```python
df.sort_values(
    "sales",
    ascending=False
).head(3)
```

---

# 24. Selecting Maximum and Minimum

Maximum sales:

```python
df["sales"].max()
```

Output:

```text
85000
```

Minimum:

```python
df["sales"].min()
```

Customer with maximum sales:

```python
df.loc[
    df["sales"].idxmax()
]
```

Output:

```text
customer     Kiran
city         Delhi
category     Laptop
sales         85000
```

Customer with minimum sales:

```python
df.loc[df["sales"].idxmin()]
```

---
# Module 4 — Data Cleaning in Pandas

Real-world data is rarely clean. Before analysis or Machine Learning, you commonly need to handle:

* Missing values
* Duplicate records
* Wrong data types
* Incorrect values
* Extra spaces
* Inconsistent text
* Invalid dates
* Outliers

---

## 1. Create a Dirty Dataset

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "customer": [
        "Amit", "Ravi", " Priya ", "Neha",
        "Amit", "Rahul", "Kiran", None
    ],
    "age": [
        25, 28, 24, None,
        25, 150, 31, 29
    ],
    "city": [
        "Jodhpur", "Jaipur", "Delhi", "Mumbai",
        "Jodhpur", "jodhpur", "Delhi", "Jaipur"
    ],
    "sales": [
        65000, 32000, None, 28000,
        65000, -5000, 85000, 41000
    ]
})

print(df)
```

Here we deliberately have several problems:

```text
Missing customer
Missing age
Missing sales
Duplicate Amit
Age = 150
Sales = -5000
Extra spaces
"Jodhpur" vs "jodhpur"
```

---

# 2. Detect Missing Values

Use:

```python
df.isnull()
```

This produces `True` where a value is missing.

For a useful summary:

```python
df.isnull().sum()
```

Example output:

```text
customer    1
age         1
city        0
sales       1
dtype: int64
```

An equivalent method is:

```python
df.isna().sum()
```

---

# 3. Percentage of Missing Values

For Data Analysis, percentages are often more useful than just counts.

```python
missing_percentage = (
    df.isna().mean() * 100
)

print(missing_percentage)
```

Example:

```text
customer    12.5
age         12.5
city         0.0
sales       12.5
```

---

# 4. Find Rows Having Missing Values

```python
df[df["customer"].isna()]
```

For rows where **any column** is missing:

```python
df[df.isna().any(axis=1)]
```

Here:

```text
axis=1
```

means check across columns for each row.

---

# 5. Remove Missing Rows

```python
df.dropna()
```

This removes rows containing missing values.

To modify the DataFrame:

```python
df = df.dropna()
```

---

# 6. Remove Rows Only When a Specific Column Is Missing

Suppose customer name is essential:

```python
df = df.dropna(
    subset=["customer"]
)
```

This is often better than blindly removing every row containing any missing value.

---

# 7. Fill Missing Values

Instead of deleting missing data, we can replace it.

For example:

```python
df["age"] = df["age"].fillna(
    df["age"].median()
)
```

Why median?

Because median is generally less affected by extreme values than mean.

---

# 8. Fill Numeric Missing Values with Mean

```python
df["sales"] = df["sales"].fillna(
    df["sales"].mean()
)
```

Use mean when it makes sense for the distribution.

---

# 9. Fill Text Missing Values

```python
df["customer"] = df["customer"].fillna(
    "Unknown"
)
```

For city:

```python
df["city"] = df["city"].fillna(
    "Unknown"
)
```

---

# 10. Different Strategies for Different Columns

A practical cleaning operation might look like:

```python
df["customer"] = df["customer"].fillna("Unknown")

df["age"] = df["age"].fillna(
    df["age"].median()
)

df["sales"] = df["sales"].fillna(
    df["sales"].median()
)
```

---

# 11. Detect Duplicate Rows

Use:

```python
df.duplicated()
```

To count duplicates:

```python
df.duplicated().sum()
```

To display duplicate records:

```python
df[df.duplicated()]
```

---

# 12. Remove Duplicates

```python
df = df.drop_duplicates()
```

For a specific business key:

```python
df = df.drop_duplicates(
    subset=["customer"]
)
```

You should only do this when the selected column(s) actually define uniqueness in the business data.

---

# 13. Handling Extra Spaces

Our dataset contains:

```text
" Priya "
```

Remove leading/trailing spaces:

```python
df["customer"] = df["customer"].str.strip()
```

Now:

```text
" Priya "
```

becomes:

```text
"Priya"
```

---

# 14. Standardizing Text Case

Suppose we have:

```text
Jodhpur
jodhpur
JODHPUR
```

Convert everything to lowercase:

```python
df["city"] = df["city"].str.lower()
```

Or uppercase:

```python
df["city"] = df["city"].str.upper()
```

For standardized title case:

```python
df["city"] = df["city"].str.title()
```

Now:

```text
Jodhpur
jodhpur
JODHPUR
```

become:

```text
Jodhpur
Jodhpur
Jodhpur
```

---

# 15. Cleaning Multiple Text Columns

Instead of writing the operation repeatedly:

```python
text_columns = ["customer", "city"]

for column in text_columns:
    df[column] = (
        df[column]
        .str.strip()
        .str.title()
    )
```

This is more maintainable when a dataset contains many text columns.

---

# 16. Detect Incorrect Values

Our dataset contains:

```text
age = 150
sales = -5000
```

A person's age of 150 may be invalid for this business context.

Find it:

```python
df[df["age"] > 100]
```

Find negative sales:

```python
df[df["sales"] < 0]
```

---

# 17. Replace Invalid Values

If negative sales are invalid and should be treated as missing:

```python
df.loc[df["sales"] < 0, "sales"] = np.nan
```

Then handle them:

```python
df["sales"] = df["sales"].fillna(
    df["sales"].median()
)
```

---

# 18. Replace Specific Values

Suppose city values contain:

```text
Jodhpur
jodhpur
JODHPUR
```

You can use:

```python
df["city"] = df["city"].replace(
    {
        "jodhpur": "Jodhpur",
        "JODHPUR": "Jodhpur"
    }
)
```

For larger text-cleaning tasks, `.str` operations are usually more flexible.

---

# 19. Data Type Inspection

Use:

```python
df.dtypes
```

Example:

```text
customer     object
age         float64
city         object
sales       float64
dtype: object
```

---

# 20. Converting Data Types

Suppose age should be integer:

```python
df["age"] = df["age"].astype("int64")
```

However, this will fail if `age` still contains `NaN`.

A safer modern approach is:

```python
df["age"] = df["age"].astype("Int64")
```

Notice the capital `I`.

Pandas `Int64` supports missing values.

---

# 21. `pd.to_numeric()`

When numeric data arrives as text:

```text
"25000"
"32000"
"41000"
```

use:

```python
df["sales"] = pd.to_numeric(
    df["sales"],
    errors="coerce"
)
```

`errors="coerce"` converts invalid values into `NaN`.

---

# 22. Date Cleaning

Suppose:

```python
df = pd.DataFrame({
    "date": [
        "2026-01-10",
        "2026-02-15",
        "invalid",
        "2026-03-20"
    ]
})
```

Convert:

```python
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)
```

Invalid dates become `NaT`.

`NaT` means **Not a Time**.

---

# 23. Complete Cleaning Pipeline

A practical cleaning process can look like this:

```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("sales.csv")

# Remove duplicate records
df = df.drop_duplicates()

# Clean text
text_columns = ["customer", "city"]

for column in text_columns:
    df[column] = (
        df[column]
        .str.strip()
        .str.title()
    )

# Convert numeric columns
df["age"] = pd.to_numeric(
    df["age"],
    errors="coerce"
)

df["sales"] = pd.to_numeric(
    df["sales"],
    errors="coerce"
)

# Mark invalid values as missing
df.loc[df["age"] > 100, "age"] = np.nan
df.loc[df["sales"] < 0, "sales"] = np.nan

# Fill missing values
df["age"] = df["age"].fillna(
    df["age"].median()
)

df["sales"] = df["sales"].fillna(
    df["sales"].median()
)

print(df)
```

---

# 24. Cleaning Workflow

A useful mental model:

```text
Raw Data
   ↓
Inspect
   ↓
Missing Values
   ↓
Duplicates
   ↓
Data Types
   ↓
Text Standardization
   ↓
Invalid Values
   ↓
Outliers
   ↓
Clean Dataset
   ↓
Analysis / ML
```

---

# 25. Important Cleaning Functions

| Function            | Purpose                   |
| ------------------- | ------------------------- |
| `isna()`            | Detect missing values     |
| `isnull()`          | Detect missing values     |
| `notna()`           | Detect non-missing values |
| `dropna()`          | Remove missing values     |
| `fillna()`          | Fill missing values       |
| `duplicated()`      | Detect duplicates         |
| `drop_duplicates()` | Remove duplicates         |
| `replace()`         | Replace values            |
| `astype()`          | Convert data type         |
| `pd.to_numeric()`   | Convert to numeric        |
| `pd.to_datetime()`  | Convert to dates          |
| `.str.strip()`      | Remove spaces             |
| `.str.lower()`      | Lowercase                 |
| `.str.upper()`      | Uppercase                 |
| `.str.title()`      | Title case                |

---

## Important Data Science Rule

Do **not** automatically delete or replace every unusual value.

For example:

```text
age = 150
sales = -5000
```

may be:

* Data-entry errors
* Valid values under a special business definition
* System-generated values
* Missing-value codes

The correct treatment should come from the **business meaning and data source**, not just from the fact that the value looks unusual.

---

## Keywords

```text
Missing Values
NaN
NaT
isna()
isnull()
notna()
dropna()
fillna()
Duplicates
duplicated()
drop_duplicates()
Data Types
astype()
to_numeric()
to_datetime()
Text Cleaning
strip()
lower()
upper()
title()
Invalid Values
```


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

# 8. `apply()`

`apply()` allows you to execute a function on values.

Example:

```python
def calculate_tax(amount):
    return amount * 0.18

df["tax"] = df["total_sales"].apply(
    calculate_tax
)
```

This calculates 18% tax for every row.

---

# 9. Lambda with `apply()`

For a small transformation:

```python
df["tax"] = df["total_sales"].apply(
    lambda x: x * 0.18
)
```

Equivalent:

```python
def calculate_tax(x):
    return x * 0.18
```

However, for simple arithmetic, **vectorized Pandas operations are preferred**:

```python
df["tax"] = df["total_sales"] * 0.18
```

This is generally clearer and more efficient than `apply()`.

---

# 10. Row-wise `apply()`

Sometimes a calculation depends on multiple columns.

```python
def calculate_revenue(row):
    return row["quantity"] * row["price"]

df["revenue"] = df.apply(
    calculate_revenue,
    axis=1
)
```

Here:

```text
axis=1
```

means the function receives one row at a time.

But for this particular example, prefer:

```python
df["revenue"] = df["quantity"] * df["price"]
```

because vectorization is more efficient.

---

# 11. String Transformation

Pandas provides the `.str` accessor for text columns.

Convert customer names to uppercase:

```python
df["customer"] = df["customer"].str.upper()
```

Lowercase:

```python
df["customer"] = df["customer"].str.lower()
```

Title case:

```python
df["customer"] = df["customer"].str.title()
```

---

# 12. String Length

```python
df["customer_length"] = df["customer"].str.len()
```

Example:

```text
Amit   → 4
Ravi   → 4
Priya  → 5
```

---

# 13. Search Text with `contains()`

Find customers whose names contain `"a"`:

```python
df[df["customer"].str.contains(
    "a",
    case=False,
    na=False
)]
```

Parameters:

```text
case=False
```

ignores uppercase/lowercase.

```text
na=False
```

prevents missing values from causing problems.

---

# 14. String Replacement

```python
df["city"] = df["city"].str.replace(
    "Jodhpur",
    "Jodhpur City",
    regex=False
)
```

For regex-based replacements, `regex=True` can be used when appropriate.

---

# 15. Extracting Text

Suppose:

```python
df["email"] = [
    "amit@gmail.com",
    "ravi@yahoo.com",
    "priya@gmail.com",
    "neha@outlook.com",
    "rahul@gmail.com",
    "kiran@yahoo.com"
]
```

Extract the domain:

```python
df["domain"] = (
    df["email"]
    .str.split("@")
    .str[1]
)
```

Result:

```text
email              domain
amit@gmail.com     gmail.com
ravi@yahoo.com     yahoo.com
priya@gmail.com    gmail.com
```

---

# 16. `astype()`

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

# 17. Binning Numerical Data

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

# 18. `pd.qcut()`

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

# 19. Renaming Columns

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

# 20. Reordering Columns

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

# 21. Insert a Column at a Specific Position

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

# 22. Remove a Column

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

# 23. A Real Transformation Pipeline

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

# 24. Transformation Methods to Remember

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

# Sorting, Aggregation & `groupby()`

This module is where Pandas starts becoming a serious **data-analysis tool**.

We will use:

```python id="b9rj4x"
import pandas as pd

df = pd.DataFrame({
    "customer": ["Amit", "Ravi", "Priya", "Neha", "Rahul", "Kiran", "Vikas", "Pooja"],
    "city": ["Jodhpur", "Jaipur", "Delhi", "Mumbai", "Jodhpur", "Delhi", "Jaipur", "Mumbai"],
    "category": ["Laptop", "Mobile", "Laptop", "Tablet", "Mobile", "Laptop", "Tablet", "Mobile"],
    "quantity": [2, 3, 1, 4, 2, 1, 5, 2],
    "sales": [130000, 96000, 72000, 112000, 82000, 85000, 180000, 90000]
})

print(df)
```

---

# 1. Sorting Data

## Sort by One Column

Sort sales from smallest to largest:

```python id="u7d5bs"
df.sort_values("sales")
```

Descending:

```python id="9ahp7f"
df.sort_values(
    "sales",
    ascending=False
)
```

---

# 2. Sort by Multiple Columns

Suppose we want:

1. City alphabetically
2. Sales highest first within each city

```python id="1gj8eq"
df.sort_values(
    ["city", "sales"],
    ascending=[True, False]
)
```

This is useful for reports where records need a business-specific ordering.

---

# 3. Sort by Index

```python id="g5b0mz"
df.sort_index()
```

Descending:

```python id="40jv4r"
df.sort_index(
    ascending=False
)
```

---

# 4. Get Top Records

Top 5 highest sales:

```python id="3a8x5c"
df.nlargest(
    5,
    "sales"
)
```

Top 3:

```python id="jjf1lm"
df.nlargest(
    3,
    "sales"
)
```

---

# 5. Get Bottom Records

```python id="nyz2sd"
df.nsmallest(
    3,
    "sales"
)
```

This is cleaner than sorting the entire DataFrame when you only need a few extreme records.

---

# 6. Basic Aggregation

Aggregation means reducing multiple values into a meaningful result.

### Total sales

```python id="0e2i3f"
df["sales"].sum()
```

### Average sales

```python id="7s3ym7"
df["sales"].mean()
```

### Minimum

```python id="7gqk8v"
df["sales"].min()
```

### Maximum

```python id="n7w1di"
df["sales"].max()
```

### Number of values

```python id="4kq7mg"
df["sales"].count()
```

### Median

```python id="2xgy6k"
df["sales"].median()
```

---

# 7. Important Aggregation Functions

| Function    | Meaning                 |
| ----------- | ----------------------- |
| `sum()`     | Total                   |
| `mean()`    | Average                 |
| `median()`  | Middle value            |
| `min()`     | Minimum                 |
| `max()`     | Maximum                 |
| `count()`   | Non-missing count       |
| `std()`     | Standard deviation      |
| `var()`     | Variance                |
| `nunique()` | Number of unique values |

---

# 8. Multiple Aggregations

You can calculate several statistics together:

```python id="z7k1t4"
df["sales"].agg([
    "sum",
    "mean",
    "min",
    "max",
    "median"
])
```

This gives a compact statistical summary.

---

# 9. `groupby()` — Most Important Concept

Suppose we want:

> Total sales for each city.

Use:

```python id="p0c6kl"
df.groupby("city")["sales"].sum()
```

Output conceptually:

```text id="y8pqqf"
city
Delhi       157000
Jaipur      276000
Jodhpur     212000
Mumbai      202000
```

The logic is:

```text id="l2l2b1"
groupby("city")
       ↓
Separate rows by city
       ↓
Calculate sum of sales
       ↓
Return one result per city
```

---

# 10. Average Sales by City

```python id="gq9h43"
df.groupby("city")["sales"].mean()
```

---

# 11. Maximum Sales by City

```python id="k9h6gz"
df.groupby("city")["sales"].max()
```

---

# 12. Number of Transactions by City

```python id="9j9x0x"
df.groupby("city")["sales"].count()
```

This answers:

> How many sales transactions occurred in each city?

---

# 13. Group by Category

Total sales for each product category:

```python id="yq0w8m"
df.groupby("category")["sales"].sum()
```

Average sales:

```python id="e7y7qy"
df.groupby("category")["sales"].mean()
```

---

# 14. Group by Multiple Columns

Suppose we want:

> Sales by city and category.

```python id="e4y3cc"
df.groupby(
    ["city", "category"]
)["sales"].sum()
```

The result has a hierarchical index:

```text id="o8z1q3"
city      category
Delhi     Laptop       ...
Jaipur    Mobile       ...
Jaipur    Tablet       ...
Jodhpur   Laptop       ...
Jodhpur   Mobile       ...
Mumbai    Mobile       ...
Mumbai    Tablet       ...
```

---

# 15. `reset_index()`

After `groupby()`, you may want a normal DataFrame.

```python id="3z1tq7"
result = (
    df.groupby("city")["sales"]
    .sum()
    .reset_index()
)

print(result)
```

Now:

```text id="s6e4jp"
       city   sales
0     Delhi  157000
1    Jaipur  276000
2   Jodhpur  212000
3    Mumbai  202000
```

This is especially useful before visualization or exporting the result.

---

# 16. Multiple Aggregations with `agg()`

Suppose the business wants:

* Total sales
* Average sales
* Maximum sales
* Number of transactions

per city.

```python id="9t9y5j"
result = (
    df.groupby("city")["sales"]
    .agg([
        "sum",
        "mean",
        "max",
        "count"
    ])
    .reset_index()
)

print(result)
```

---

# 17. Named Aggregations

For production-quality reports, descriptive column names are better:

```python id="y2f7na"
result = (
    df.groupby("city")
    .agg(
        total_sales=("sales", "sum"),
        average_sales=("sales", "mean"),
        highest_sale=("sales", "max"),
        transactions=("sales", "count")
    )
    .reset_index()
)

print(result)
```

Output structure:

```text
city      total_sales   average_sales   highest_sale   transactions
Delhi        ...           ...             ...              ...
Jaipur       ...           ...             ...              ...
Jodhpur      ...           ...             ...              ...
Mumbai       ...           ...             ...              ...
```

This approach is highly useful for business dashboards and reporting.

---

# 18. Grouping Different Columns

We can calculate different aggregations for different columns:

```python id="l4pjkg"
result = (
    df.groupby("city")
    .agg(
        total_sales=("sales", "sum"),
        avg_sales=("sales", "mean"),
        total_quantity=("quantity", "sum"),
        customers=("customer", "count")
    )
    .reset_index()
)
```

Now we have a city-level KPI table.

---

# 19. Unique Customers

Number of unique customers:

```python id="8q2f4v"
df["customer"].nunique()
```

Unique cities:

```python id="3t2e0b"
df["city"].nunique()
```

Unique categories:

```python id="h2s7z5"
df["category"].nunique()
```

---

# 20. `value_counts()`

This is one of the easiest ways to understand categorical data.

```python id="j0j7pw"
df["city"].value_counts()
```

Example:

```text
Delhi       2
Jaipur      2
Jodhpur     2
Mumbai      2
```

Category frequency:

```python id="0c0v7q"
df["category"].value_counts()
```

---

# 21. Percentage Distribution

```python id="s1j8yp"
df["category"].value_counts(
    normalize=True
) * 100
```

This tells you the percentage of transactions belonging to each category.

---

# 22. GroupBy + Sorting

Suppose we want cities ordered by total sales:

```python id="h3b9rj"
result = (
    df.groupby("city")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print(result)
```

This is a very common analytical pattern:

```text
Group
 ↓
Aggregate
 ↓
Sort
```

---

# 23. GroupBy + Filter

Suppose we want only cities whose total sales exceed ₹200,000.

```python id="qf9v6v"
city_sales = (
    df.groupby("city")["sales"]
    .sum()
)

result = city_sales[
    city_sales > 200000
]

print(result)
```

---

# 24. Real Business Analysis

### Question 1

Which city generated the highest total sales?

```python id="1y6z8b"
city_sales = (
    df.groupby("city")["sales"]
    .sum()
)

highest_city = city_sales.idxmax()

print(highest_city)
```

Notice the distinction:

* `max()` → returns the highest value
* `idxmax()` → returns the label associated with that value

---

### Question 2

Which category generated the highest total sales?

```python id="x9w3dj"
category_sales = (
    df.groupby("category")["sales"]
    .sum()
)

print(category_sales.idxmax())
```

---

### Question 3

What is the average transaction value?

```python id="h6c0n4"
average_transaction = df["sales"].mean()

print(average_transaction)
```

---

# 25. `groupby()` Mental Model

Imagine:

```text
              Original Data
                    │
                    ▼
             groupby("city")
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
     Delhi        Jaipur       Mumbai
       │            │            │
       ▼            ▼            ▼
     sales        sales        sales
       │            │            │
       ▼            ▼            ▼
      SUM          SUM          SUM
```

This is the foundation of many business analyses.

---

# 26. Common Business Questions and Pandas

| Business Question        | Pandas Approach          |
| ------------------------ | ------------------------ |
| Total sales?             | `sum()`                  |
| Average sales?           | `mean()`                 |
| Highest sale?            | `max()`                  |
| Lowest sale?             | `min()`                  |
| Number of transactions?  | `count()`                |
| Unique customers?        | `nunique()`              |
| Sales by city?           | `groupby()`              |
| Sales by category?       | `groupby()`              |
| Top 5 customers?         | `nlargest()`             |
| Bottom 5 customers?      | `nsmallest()`            |
| Most common category?    | `value_counts()`         |
| City with highest sales? | `groupby()` + `idxmax()` |

---

# 27. Production-Style KPI Table

A useful sales summary can be generated with:

```python id="j3y8t5"
kpi = (
    df.groupby("city")
    .agg(
        total_sales=("sales", "sum"),
        average_sales=("sales", "mean"),
        total_quantity=("quantity", "sum"),
        transactions=("sales", "count"),
        unique_customers=("customer", "nunique")
    )
    .reset_index()
    .sort_values(
        "total_sales",
        ascending=False
    )
)

print(kpi)
```

This pattern is extremely common in:

* Business Intelligence
* Sales reporting
* Power BI preparation
* Exploratory Data Analysis
* Customer analytics
* Financial reporting

---

## Important Keywords

```text
sort_values()
sort_index()
nlargest()
nsmallest()

sum()
mean()
median()
min()
max()
count()
std()
var()
nunique()

groupby()
agg()
reset_index()

value_counts()
idxmax()
idxmin()
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

**Next → Module 8: Date & Time Handling in Pandas**
`to_datetime()`, extracting year/month/day, date filtering, time differences, resampling, and sales-by-month analysis.

Type **continue**.

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

# Text Data in Pandas

Text columns are common in real-world datasets:

* Customer names
* Email addresses
* Product names
* Cities
* Reviews
* Categories
* Phone numbers
* Addresses

Pandas provides the `.str` accessor for efficient string operations.

We will cover:

1. `.str.lower()`
2. `.str.upper()`
3. `.str.strip()`
4. `.str.contains()`
5. `.str.replace()`
6. `.str.startswith()` / `.str.endswith()`
7. `.str.len()`
8. `.str.extract()`
9. Regular expressions

---

## 13.1 Sample Dataset

```python
import pandas as pd

df = pd.DataFrame({
    "Name": [
        "Rahul Sharma",
        " PRIYA SINGH ",
        "amit kumar",
        "Neha Gupta",
        "ROHIT VERMA"
    ],
    "Email": [
        "rahul@gmail.com",
        "priya@yahoo.com",
        "amit@gmail.com",
        "neha@company.com",
        "rohit@gmail.com"
    ],
    "City": [
        "Jodhpur",
        "Jaipur",
        "Jodhpur",
        "Delhi",
        "Jaipur"
    ]
})

print(df)
```

---

# 13.2 Convert Text to Lowercase

```python
df["Name"] = df["Name"].str.lower()
```

Example:

```text
"Rahul Sharma" → "rahul sharma"
"ROHIT VERMA"  → "rohit verma"
```

For an entire column:

```python
df["City"] = df["City"].str.lower()
```

---

# 13.3 Convert Text to Uppercase

```python
df["Name"] = df["Name"].str.upper()
```

Output:

```text
RAHUL SHARMA
PRIYA SINGH
AMIT KUMAR
NEHA GUPTA
ROHIT VERMA
```

---

# 13.4 Remove Extra Spaces

This is very important during **data cleaning**.

```python
df["Name"] = df["Name"].str.strip()
```

For example:

```text
" PRIYA SINGH "
        ↓
"PRIYA SINGH"
```

You can also remove spaces from both sides of every string column:

```python
df["City"] = df["City"].str.strip()
```

---

# 13.5 Search Text Using `contains()`

Suppose we want customers from Jodhpur:

```python
result = df[
    df["City"].str.contains("Jodhpur")
]

print(result)
```

Output:

```text
           Name  Email     City
0  Rahul Sharma  ...    Jodhpur
2    Amit Kumar  ...    Jodhpur
```

### Case-insensitive search

```python
result = df[
    df["City"].str.contains(
        "jodhpur",
        case=False,
        na=False
    )
]
```

`case=False` means:

```text
Jodhpur
jodhpur
JODHPUR
JoDhPuR
```

can all match.

`na=False` prevents missing values from causing problems.

---

# 13.6 Search for Gmail Customers

```python
gmail_users = df[
    df["Email"].str.contains(
        "@gmail.com",
        na=False
    )
]

print(gmail_users)
```

This is useful for filtering customer records based on email domains.

---

# 13.7 `startswith()`

Find names beginning with `"A"`:

```python
result = df[
    df["Name"].str.startswith("A", na=False)
]
```

Example:

```text
Amit Kumar
```

---

# 13.8 `endswith()`

Find Gmail addresses:

```python
result = df[
    df["Email"].str.endswith(
        "@gmail.com",
        na=False
    )
]
```

---

# 13.9 Replace Text

Suppose the dataset contains:

```text
Jodhpur
JPR
Jaipur
```

and we want to replace `JPR` with `Jaipur`:

```python
df["City"] = df["City"].str.replace(
    "JPR",
    "Jaipur",
    regex=False
)
```

For multiple replacements, `replace()` at the Series level can sometimes be cleaner:

```python
df["City"] = df["City"].replace({
    "JPR": "Jaipur",
    "JDP": "Jodhpur"
})
```

---

# 13.10 String Length

```python
df["Name_Length"] = df["Name"].str.len()
```

Example:

```text
Rahul Sharma → 12
Amit Kumar   → 10
```

This can be useful for detecting suspicious or invalid text values.

---

# 13.11 Extract Parts of Text

Suppose we have:

```python
df = pd.DataFrame({
    "Email": [
        "rahul@gmail.com",
        "priya@yahoo.com",
        "amit@company.com"
    ]
})
```

Extract username:

```python
df["Username"] = df["Email"].str.split("@").str[0]
```

Output:

```text
             Email Username
0  rahul@gmail.com    rahul
1  priya@yahoo.com    priya
2  amit@company.com     amit
```

Extract domain:

```python
df["Domain"] = df["Email"].str.split("@").str[1]
```

---

# 13.12 Using Regular Expressions

Regular expressions are useful when the pattern is more complex.

For example, extract the email domain:

```python
df["Domain"] = df["Email"].str.extract(
    r"@(.+)$"
)
```

Output:

```text
gmail.com
yahoo.com
company.com
```

### Extract numbers from text

Suppose:

```python
df = pd.DataFrame({
    "Order": [
        "ORD-1025",
        "ORD-2048",
        "ORD-3099"
    ]
})
```

Extract the numeric portion:

```python
df["Order_Number"] = df["Order"].str.extract(
    r"(\d+)"
)
```

Output:

```text
  Order    Order_Number
0 ORD-1025    1025
1 ORD-2048    2048
2 ORD-3099    3099
```

---

# 13.13 Common String Operations

| Operation     | Code                                   |
| ------------- | -------------------------------------- |
| Lowercase     | `df["Name"].str.lower()`               |
| Uppercase     | `df["Name"].str.upper()`               |
| Remove spaces | `df["Name"].str.strip()`               |
| Contains      | `df["Name"].str.contains("Rahul")`     |
| Starts with   | `df["Name"].str.startswith("A")`       |
| Ends with     | `df["Name"].str.endswith("a")`         |
| Replace       | `df["Name"].str.replace("old", "new")` |
| Length        | `df["Name"].str.len()`                 |
| Split         | `df["Name"].str.split()`               |
| Extract       | `df["Name"].str.extract()`             |

---

# Real-World Data Cleaning Example

Suppose customer names contain inconsistent formatting:

```python
df = pd.DataFrame({
    "Customer": [
        " rahul sharma",
        "PRIYA SINGH ",
        " Amit Kumar ",
        "neha gupta"
    ]
})
```

A clean standardization process:

```python
df["Customer"] = (
    df["Customer"]
    .str.strip()
    .str.title()
)
```

Result:

```text
      Customer
0 Rahul Sharma
1 Priya Singh
2 Amit Kumar
3 Neha Gupta
```

This chaining pattern is commonly used in production data-cleaning pipelines.

### Keywords Recap

```text
Text Data
├── .str.lower()
├── .str.upper()
├── .str.strip()
├── .str.contains()
├── .str.startswith()
├── .str.endswith()
├── .str.replace()
├── .str.len()
├── .str.split()
├── .str.extract()
└── Regular Expressions
```

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
        ("North", ["Laptop", "Mobile"])
    ]
)
```

For more complex MultiIndex selection, `pd.IndexSlice` is useful:

```python
idx = pd.IndexSlice

result = df.loc[
    idx["North", ["Laptop", "Mobile"]]
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
#  Statistical Analysis in Pandas

Pandas provides built-in methods for performing statistical analysis directly on DataFrames and Series.

We will cover:

1. `mean()`
2. `median()`
3. `std()`
4. `var()`
5. `min()` / `max()`
6. `quantile()`
7. `corr()`
8. `cov()`
9. `value_counts()`
10. Practical statistical analysis

---

## 16.1 Sample Dataset

```python
import pandas as pd

df = pd.DataFrame({
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 9],
    "Marks": [45, 50, 55, 62, 68, 74, 81, 88],
    "Attendance": [65, 70, 72, 78, 80, 85, 90, 94]
})

print(df)
```

Output:

```text
   Study_Hours  Marks  Attendance
0            2     45          65
1            3     50          70
2            4     55          72
3            5     62          78
4            6     68          80
5            7     74          85
6            8     81          90
7            9     88          94
```

---

# 16.2 Mean

Mean is the arithmetic average.

```python
print(df["Marks"].mean())
```

Formula:

```text
Mean = Sum of values / Number of values
```

For example:

```text
45 + 50 + 55 + ... + 88
-------------------------
           8
```

---

# 16.3 Median

Median is the **middle value after sorting**.

```python
print(df["Marks"].median())
```

It is especially useful when the data contains outliers.

Example:

```python
values = [10, 20, 30, 40, 500]

print(pd.Series(values).mean())
print(pd.Series(values).median())
```

The mean is strongly affected by `500`, while the median is much less affected.

---

# 16.4 Standard Deviation

Standard deviation measures how spread out the values are around the mean.

```python
print(df["Marks"].std())
```

Conceptually:

```text
Small std
   ↓
Values are close together

Large std
   ↓
Values are more spread out
```

Pandas uses sample standard deviation by default (`ddof=1`).

For population standard deviation:

```python
df["Marks"].std(ddof=0)
```

---

# 16.5 Variance

Variance is related to standard deviation:

```python
print(df["Marks"].var())
```

Mathematically:

```text
Variance = (Standard Deviation)²
```

For example:

```python
std = df["Marks"].std()
variance = df["Marks"].var()

print(std)
print(variance)
```

---

# 16.6 Minimum and Maximum

```python
print(df["Marks"].min())
print(df["Marks"].max())
```

Output:

```text
45
88
```

Range:

```python
data_range = (
    df["Marks"].max() -
    df["Marks"].min()
)

print(data_range)
```

---

# 16.7 Quantiles

Quantiles divide data into portions.

### 25th percentile

```python
print(df["Marks"].quantile(0.25))
```

### 50th percentile

```python
print(df["Marks"].quantile(0.50))
```

This is the median.

### 75th percentile

```python
print(df["Marks"].quantile(0.75))
```

You can calculate several at once:

```python
print(
    df["Marks"].quantile([0.25, 0.50, 0.75])
)
```

---

# 16.8 Descriptive Statistics

Instead of calculating each statistic individually:

```python
print(df["Marks"].describe())
```

Output will contain:

```text
count
mean
std
min
25%
50%
75%
max
```

For the entire DataFrame:

```python
print(df.describe())
```

This is one of the most useful first steps during **Exploratory Data Analysis (EDA)**.

---

# 16.9 Correlation

Correlation measures the **strength and direction of a linear relationship** between numerical variables.

```python
print(df["Study_Hours"].corr(df["Marks"]))
```

The correlation coefficient ranges from:

```text
-1  ←──────── 0 ────────→  +1
```

General interpretation:

|   Correlation | Interpretation                       |
| ------------: | ------------------------------------ |
|          `+1` | Perfect positive linear relationship |
| Close to `+1` | Strong positive relationship         |
|           `0` | No linear relationship               |
| Close to `-1` | Strong negative relationship         |
|          `-1` | Perfect negative linear relationship |

For example:

```python
print(
    df["Study_Hours"].corr(
        df["Marks"]
    )
)
```

The result will be positive because, in this example, marks generally increase as study hours increase.

**Important:** Correlation does not by itself establish causation.

---

# 16.10 Correlation Matrix

Instead of comparing two columns:

```python
df["Study_Hours"].corr(df["Marks"])
```

we can calculate correlation between all numerical columns:

```python
corr_matrix = df.corr()

print(corr_matrix)
```

Conceptually:

```text
             Study_Hours   Marks   Attendance
Study_Hours      1.00       ...       ...
Marks             ...       1.00      ...
Attendance        ...        ...      1.00
```

Diagonal values are always `1` because each variable is perfectly correlated with itself.

---

# 16.11 Covariance

Covariance indicates whether two variables tend to move together.

```python
print(
    df["Study_Hours"].cov(
        df["Marks"]
    )
)
```

Interpretation:

```text
Positive covariance
        ↓
Variables tend to increase together

Negative covariance
        ↓
One tends to increase while the other decreases
```

Unlike correlation, covariance does **not** have a fixed range such as `-1 to +1`.

---

# 16.12 Covariance Matrix

```python
print(df.cov())
```

This calculates covariance between every pair of numerical columns.

---

# 16.13 `value_counts()`

`value_counts()` is extremely useful for categorical analysis.

```python
df = pd.DataFrame({
    "Department": [
        "IT", "HR", "IT",
        "Sales", "IT", "HR"
    ]
})

print(df["Department"].value_counts())
```

Output:

```text
IT       3
HR       2
Sales    1
```

It tells us how frequently each category occurs.

### Percentage Distribution

```python
print(
    df["Department"]
    .value_counts(normalize=True)
)
```

Output will represent proportions.

To display percentages:

```python
print(
    df["Department"]
    .value_counts(normalize=True)
    .mul(100)
)
```

---

# 16.14 Statistical Summary of Multiple Columns

You can calculate several statistics together:

```python
result = df.describe()
```

Or explicitly:

```python
stats = df["Marks"].agg([
    "count",
    "mean",
    "median",
    "min",
    "max",
    "std"
])

print(stats)
```

You can also use named aggregations:

```python
result = df["Marks"].agg(
    average="mean",
    median="median",
    minimum="min",
    maximum="max",
    standard_deviation="std"
)

print(result)
```

---

# 16.15 Real-World Example

Consider customer purchase data:

```python
sales = pd.DataFrame({
    "Customer": [
        "A", "B", "C", "D", "E", "F"
    ],
    "Orders": [
        2, 5, 3, 8, 4, 10
    ],
    "Revenue": [
        5000, 12000, 7000,
        18000, 9000, 22000
    ]
})
```

### Average Revenue

```python
sales["Revenue"].mean()
```

### Median Revenue

```python
sales["Revenue"].median()
```

### Revenue variability

```python
sales["Revenue"].std()
```

### Relationship between orders and revenue

```python
sales["Orders"].corr(
    sales["Revenue"]
)
```

### Complete statistical summary

```python
sales[["Orders", "Revenue"]].describe()
```

This provides the basic statistical profile needed before deeper business analysis.

---

## Important Difference

### Correlation

```python
df["Study_Hours"].corr(df["Marks"])
```

Measures **standardized linear relationship**.

### Covariance

```python
df["Study_Hours"].cov(df["Marks"])
```

Measures whether variables **move together**, but its magnitude depends on the units of the variables.

### Standard Deviation

```python
df["Marks"].std()
```

Measures **spread of one variable**.

### Variance

```python
df["Marks"].var()
```

Measures squared spread.

---

## Keywords Recap

```text
Statistical Analysis
├── mean()
├── median()
├── std()
├── var()
├── min()
├── max()
├── quantile()
├── describe()
├── corr()
├── cov()
├── value_counts()
└── agg()
```

# Data Analysis with Pandas

Data analysis means going beyond simply cleaning data. The goal is to answer **business questions using data**.

We will cover:

1. KPIs
2. Trends
3. Segmentation
4. Outliers
5. Business questions
6. Practical Pandas analysis workflow

---

## 17.1 Sample Sales Dataset

```python
import pandas as pd

df = pd.DataFrame({
    "Date": [
        "2026-01-05", "2026-01-10", "2026-01-15",
        "2026-02-05", "2026-02-12", "2026-02-20",
        "2026-03-05", "2026-03-15", "2026-03-25"
    ],
    "Region": [
        "North", "South", "North",
        "South", "East", "North",
        "East", "South", "North"
    ],
    "Product": [
        "Laptop", "Mobile", "Mobile",
        "Laptop", "Tablet", "Laptop",
        "Mobile", "Tablet", "Mobile"
    ],
    "Sales": [
        85000, 45000, 50000,
        90000, 35000, 95000,
        55000, 40000, 60000
    ],
    "Quantity": [
        5, 10, 8,
        6, 7, 5,
        11, 8, 12
    ]
})

df["Date"] = pd.to_datetime(df["Date"])
```

---

# 17.2 KPI — Key Performance Indicator

A KPI is a numerical measurement used to track business performance.

Common sales KPIs:

```text
Total Sales
Average Order Value
Total Quantity
Number of Orders
Maximum Sale
Minimum Sale
```

### Total Sales

```python
total_sales = df["Sales"].sum()

print(total_sales)
```

### Total Quantity

```python
total_quantity = df["Quantity"].sum()

print(total_quantity)
```

### Average Sale

```python
average_sale = df["Sales"].mean()

print(average_sale)
```

### Number of Orders

```python
total_orders = len(df)

print(total_orders)
```

---

# 17.3 Create a KPI Dictionary

You can calculate several KPIs together:

```python
kpis = {
    "Total Sales": df["Sales"].sum(),
    "Average Sale": df["Sales"].mean(),
    "Total Quantity": df["Quantity"].sum(),
    "Total Orders": len(df),
    "Maximum Sale": df["Sales"].max()
}

print(kpis)
```

This structure can later be used to build a dashboard.

---

# 17.4 Analyze Sales by Region

Use `groupby()`:

```python
region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
)

print(region_sales)
```

Output will show total sales for:

```text
North
South
East
```

For multiple metrics:

```python
region_analysis = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Average_Sale=("Sales", "mean"),
    Total_Quantity=("Quantity", "sum"),
    Orders=("Sales", "count")
)

print(region_analysis)
```

This provides a much more useful business view.

---

# 17.5 Analyze Sales by Product

```python
product_analysis = df.groupby("Product").agg(
    Total_Sales=("Sales", "sum"),
    Quantity=("Quantity", "sum"),
    Average_Sale=("Sales", "mean")
)

print(product_analysis)
```

Now you can answer questions such as:

```text
How much revenue did each product generate?
How many units were sold?
What was the average transaction value?
```

---

# 17.6 Trend Analysis

First extract the month:

```python
df["Month"] = df["Date"].dt.to_period("M")
```

Then calculate monthly sales:

```python
monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

print(monthly_sales)
```

This produces a time-based trend:

```text
2026-01
2026-02
2026-03
```

You can calculate monthly quantity similarly:

```python
monthly_quantity = (
    df.groupby("Month")["Quantity"]
    .sum()
)
```

---

# 17.7 Month-over-Month Change

Suppose:

```python
monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)
```

Calculate percentage change:

```python
monthly_growth = monthly_sales.pct_change() * 100

print(monthly_growth)
```

Conceptually:

```text
Current Month - Previous Month
-------------------------------- × 100
       Previous Month
```

This helps identify periods where sales increased or decreased.

---

# 17.8 Segmentation

Segmentation means dividing data into meaningful groups.

Common customer/business segments:

```text
Region
Product
Customer Type
Age Group
Income Group
Order Value
Purchase Frequency
```

For example, segment sales by both region and product:

```python
segment = (
    df.groupby(
        ["Region", "Product"]
    )["Sales"]
    .sum()
)

print(segment)
```

This produces a two-dimensional business analysis.

You can also create a report:

```python
segment = df.pivot_table(
    index="Region",
    columns="Product",
    values="Sales",
    aggfunc="sum",
    fill_value=0
)

print(segment)
```

---

# 17.9 Detecting Outliers

An outlier is an observation that is unusually far from the rest of the data.

One common statistical method is the **IQR method**.

### Step 1 — Calculate Q1

```python
Q1 = df["Sales"].quantile(0.25)
```

### Step 2 — Calculate Q3

```python
Q3 = df["Sales"].quantile(0.75)
```

### Step 3 — Calculate IQR

```python
IQR = Q3 - Q1
```

### Step 4 — Define boundaries

```python
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
```

### Step 5 — Find outliers

```python
outliers = df[
    (df["Sales"] < lower) |
    (df["Sales"] > upper)
]

print(outliers)
```

---

# 17.10 Finding High-Value Transactions

Sometimes you don't need statistical outliers. You simply want transactions above a business threshold.

For example:

```python
high_value = df[
    df["Sales"] > 80000
]

print(high_value)
```

This is a **business rule**, whereas the IQR method is a **statistical rule**.

That distinction is important.

---

# 17.11 Top Products

Find the highest-selling products:

```python
product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(product_sales)
```

You can take the first few records:

```python
top_products = product_sales.head(3)
```

---

# 17.12 Answering Business Questions

A good data analyst starts with questions.

### Question 1

**What is total revenue?**

```python
df["Sales"].sum()
```

### Question 2

**Which region generated the most revenue?**

```python
df.groupby("Region")["Sales"].sum()
```

### Question 3

**Which product generated the most revenue?**

```python
df.groupby("Product")["Sales"].sum()
```

### Question 4

**What is the monthly sales trend?**

```python
df.groupby(
    df["Date"].dt.to_period("M")
)["Sales"].sum()
```

### Question 5

**Which transactions are unusually large?**

```python
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[
    (df["Sales"] < Q1 - 1.5 * IQR) |
    (df["Sales"] > Q3 + 1.5 * IQR)
]
```

---

# 17.13 A Practical Analysis Workflow

A common Pandas analysis workflow is:

```text
Raw Data
   ↓
Inspect
   ↓
Clean
   ↓
Transform
   ↓
Create KPIs
   ↓
Group & Segment
   ↓
Analyze Trends
   ↓
Detect Outliers
   ↓
Generate Insights
   ↓
Visualize
```

For example:

```python
df.info()

df.describe()

df["Date"] = pd.to_datetime(df["Date"])

total_sales = df["Sales"].sum()

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
)

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
)

monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Sales"]
    .sum()
)
```

This is the foundation for turning a raw DataFrame into an analytical dataset.

---

## Keywords Recap

```text
Data Analysis
├── KPI
├── Total Sales
├── Average
├── GroupBy
├── Segmentation
├── Trend Analysis
├── Percentage Change
├── Outliers
├── IQR
├── Business Rules
└── Business Questions
```

# Visualization with Pandas + Matplotlib

Visualization helps convert numerical analysis into **patterns, trends, comparisons, and distributions**.

We will cover:

1. Line chart
2. Bar chart
3. Horizontal bar chart
4. Histogram
5. Box plot
6. Scatter plot
7. Pie chart
8. Pandas plotting
9. Matplotlib integration
10. Practical business visualization

---

## 18.1 Sample Dataset

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [50000, 60000, 55000, 75000, 80000, 90000],
    "Orders": [120, 140, 130, 170, 180, 210]
})
```

---

# 18.2 Line Chart

A line chart is useful for **trends over time**.

```python
plt.plot(df["Month"], df["Sales"])

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")

plt.show()
```

Use a line chart when the order of observations matters, especially for:

```text
Sales over time
Revenue over time
Website traffic
Stock prices
Temperature
Monthly customers
```

---

# 18.3 Bar Chart

A bar chart is useful for **comparing categories**.

```python
plt.bar(df["Month"], df["Sales"])

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")

plt.show()
```

For example:

```text
Jan → 50,000
Feb → 60,000
Mar → 55,000
...
```

---

# 18.4 Horizontal Bar Chart

Use `barh()`:

```python
plt.barh(df["Month"], df["Sales"])

plt.xlabel("Sales")
plt.ylabel("Month")
plt.title("Monthly Sales")

plt.show()
```

Horizontal bars are especially useful when category names are long.

---

# 18.5 Histogram

A histogram shows the **distribution of numerical data**.

```python
plt.hist(df["Sales"], bins=5)

plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.title("Sales Distribution")

plt.show()
```

Unlike a bar chart, a histogram groups numerical values into ranges called **bins**.

Example:

```text
0–20,000
20,000–40,000
40,000–60,000
...
```

Useful for analyzing:

* Salary distribution
* Age distribution
* Sales distribution
* Customer spending
* Exam marks

---

# 18.6 Box Plot

A box plot helps identify:

* Median
* Quartiles
* Spread
* Potential outliers

```python
plt.boxplot(df["Sales"])

plt.ylabel("Sales")
plt.title("Sales Distribution")

plt.show()
```

A box plot is particularly useful during EDA for detecting unusual values.

---

# 18.7 Scatter Plot

A scatter plot shows the relationship between two numerical variables.

```python
plt.scatter(
    df["Orders"],
    df["Sales"]
)

plt.xlabel("Orders")
plt.ylabel("Sales")
plt.title("Orders vs Sales")

plt.show()
```

This can help investigate relationships such as:

```text
Advertising Spend vs Sales
Study Hours vs Marks
Orders vs Revenue
Experience vs Salary
```

---

# 18.8 Pandas `plot()`

Pandas can directly use Matplotlib internally.

For example:

```python
df.plot(
    x="Month",
    y="Sales",
    kind="line"
)

plt.show()
```

Bar chart:

```python
df.plot(
    x="Month",
    y="Sales",
    kind="bar"
)

plt.show()
```

Histogram:

```python
df["Sales"].plot(
    kind="hist",
    bins=5
)

plt.show()
```

Box plot:

```python
df["Sales"].plot(
    kind="box"
)

plt.show()
```

---

# 18.9 Common Pandas Plot Types

The `kind` parameter supports common chart types:

| `kind`      | Chart          |
| ----------- | -------------- |
| `"line"`    | Line chart     |
| `"bar"`     | Vertical bar   |
| `"barh"`    | Horizontal bar |
| `"hist"`    | Histogram      |
| `"box"`     | Box plot       |
| `"scatter"` | Scatter plot   |
| `"pie"`     | Pie chart      |
| `"area"`    | Area chart     |

---

# 18.10 Visualizing GroupBy Results

Suppose we have:

```python
sales = pd.DataFrame({
    "Region": [
        "North", "North",
        "South", "South",
        "East", "East"
    ],
    "Sales": [
        50000, 70000,
        60000, 80000,
        40000, 55000
    ]
})
```

Calculate regional sales:

```python
region_sales = (
    sales.groupby("Region")["Sales"]
    .sum()
)

print(region_sales)
```

Visualize:

```python
region_sales.plot(
    kind="bar",
    title="Sales by Region"
)

plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()
```

This is a very common analytics pattern:

```text
Raw Data
   ↓
groupby()
   ↓
Aggregation
   ↓
Visualization
```

---

# 18.11 Visualizing Monthly Trends

```python
monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

monthly_sales.plot(
    kind="line",
    marker="o",
    title="Monthly Sales Trend"
)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
```

The important analytical idea is that the visualization comes **after the data has been aggregated into a meaningful analytical level**.

---

# 18.12 Scatter Plot with Real Analysis

Consider:

```python
students = pd.DataFrame({
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8],
    "Marks": [45, 52, 58, 65, 70, 78, 85]
})
```

Plot:

```python
plt.scatter(
    students["Study_Hours"],
    students["Marks"]
)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.show()
```

You can also calculate correlation:

```python
correlation = students["Study_Hours"].corr(
    students["Marks"]
)

print(correlation)
```

Now you have both:

```text
Visualization → See relationship
Correlation   → Quantify linear relationship
```

---

# 18.13 Pie Chart

Pie charts can show proportions for a small number of categories.

```python
region_sales = sales.groupby("Region")["Sales"].sum()

region_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.title("Sales Distribution by Region")

plt.show()
```

For business analytics, bar charts are often easier to compare precisely, especially when there are many categories.

---

# 18.14 A Practical Visualization Workflow

A typical Pandas + Matplotlib workflow:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = (
    df.groupby(
        df["Date"].dt.to_period("M")
    )["Sales"]
    .sum()
)

monthly_sales.plot(
    kind="line",
    marker="o"
)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
```

This pattern is directly applicable to real sales datasets.

---

## Which Chart Should You Use?

| Business Question                         | Recommended Chart |
| ----------------------------------------- | ----------------- |
| How are sales changing over time?         | Line              |
| Which region has more sales?              | Bar               |
| What is the distribution of salaries?     | Histogram         |
| Are there outliers?                       | Box plot          |
| Are two numerical variables related?      | Scatter           |
| What percentage belongs to each category? | Pie               |
| Compare long category names               | Horizontal bar    |

---

## Keywords Recap

```text
Visualization
├── Matplotlib
├── Pandas plot()
├── Line Chart
├── Bar Chart
├── Histogram
├── Box Plot
├── Scatter Plot
├── Pie Chart
├── GroupBy + Visualization
└── Trend Analysis
```
