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
