

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
