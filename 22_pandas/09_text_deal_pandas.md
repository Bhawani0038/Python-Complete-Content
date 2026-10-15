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

# 13.12 Common String Operations

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
