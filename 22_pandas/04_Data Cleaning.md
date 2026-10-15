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

`isna()` (equivalent to `isnull()`) marks missing values. Sum each column to count them:

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

```python
df["customer"] = df["customer"].fillna("Unknown")
df["age"] = df["age"].fillna(df["age"].median())
df["sales"] = df["sales"].fillna(df["sales"].mean())
```

Use a median when outliers may skew the mean; use a mean when it suits the
distribution. Choose a fill value based on the column's meaning.

---

# 8. Detect Duplicate Rows

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

# 9. Remove Duplicates

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

# 10. Handling Extra Spaces

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

# 11. Standardizing Text Case

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

# 12. Cleaning Multiple Text Columns

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

# 13. Detect Incorrect Values

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

# 14. Replace Invalid Values

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

# 15. Replace Specific Values

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

# 16. Data Type Inspection

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

# 17. Converting Data Types

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

# 18. `pd.to_numeric()`

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

# 19. Date Cleaning

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

# 20. Complete Cleaning Pipeline

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

# 21. Cleaning Workflow

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

# 22. Important Cleaning Functions

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

