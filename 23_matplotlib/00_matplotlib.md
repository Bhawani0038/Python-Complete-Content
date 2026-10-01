# Matplotlib for Data Science & Data Analysis

## Complete Learning Roadmap

| Module | Topics |
| --- | --- |
| 1. Fundamentals | What Matplotlib is, installation, importing `pyplot` |
| 2. Figure and Axes | Creating figures, axes, and multiple plots |
| 3. Basic Charts | Line, bar, scatter, histogram, and box plots |
| 4. Labels and Legends | Titles, axis labels, ticks, legends, annotations |
| 5. Pandas Visualization | Plotting Series and DataFrames |
| 6. Data Analysis | Trends, comparisons, distributions, relationships, outliers |
| 7. Styling and Export | Colors, styles, layout, saving figures |
| 8. Good Practices | Choosing chart types and avoiding misleading charts |
| 9. Practice | Exercises using a small sales dataset |

---

## 1. What is Matplotlib?

**Matplotlib** is a Python library for creating charts and visualizations. It is widely used in data science for:

* Exploratory Data Analysis (EDA)
* Comparing values across categories
* Finding trends over time
* Studying distributions and outliers
* Presenting analysis in reports

Matplotlib works well with **NumPy** and **Pandas**. Its `pyplot` interface is commonly imported as `plt`:

```python
import matplotlib.pyplot as plt
```

---

## 2. Installing Matplotlib

Install Matplotlib with pip:

```bash
pip install matplotlib
```

For a data-analysis environment, install Pandas too:

```bash
pip install pandas matplotlib
```

Check the installed version:

```python
import matplotlib

print(matplotlib.__version__)
```

---

## 3. Figure and Axes

A **Figure** is the whole image. An **Axes** is an individual plotting area inside the figure. Most charts use one Figure and one Axes.

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [1200, 1500, 1350, 1800, 2100]

fig, ax = plt.subplots()
ax.plot(months, revenue)
ax.set_title("Monthly Revenue")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue ($)")
plt.show()
```

`plt.subplots()` is a useful starting point because it gives you explicit `fig` and `ax` objects. Use the Axes methods (`ax.plot()`, `ax.set_title()`, and so on) to control a chart.

---

## 4. Line Charts: Trends Over Time

Use a line chart when the order of values matters, especially for dates or continuous measurements.

```python
days = [1, 2, 3, 4, 5, 6, 7]
website_visits = [120, 145, 132, 190, 220, 205, 260]

fig, ax = plt.subplots()
ax.plot(days, website_visits, marker="o", label="Visits")
ax.set(title="Website Visits This Week", xlabel="Day", ylabel="Visits")
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()
```

Plot multiple series on the same axes to compare trends:

```python
days = [1, 2, 3, 4, 5]
product_a = [20, 25, 23, 30, 35]
product_b = [18, 22, 27, 26, 32]

fig, ax = plt.subplots()
ax.plot(days, product_a, marker="o", label="Product A")
ax.plot(days, product_b, marker="s", label="Product B")
ax.set(title="Daily Units Sold", xlabel="Day", ylabel="Units")
ax.legend()
plt.show()
```

---

## 5. Bar Charts: Comparing Categories

Use a bar chart to compare a small number of categories. Bars should generally start at zero so their lengths represent the values honestly.

```python
departments = ["Books", "Clothing", "Food", "Electronics"]
sales = [4200, 6100, 5300, 7800]

fig, ax = plt.subplots()
ax.bar(departments, sales, color="teal")
ax.set(title="Sales by Department", xlabel="Department", ylabel="Sales ($)")
plt.show()
```

For long category names, use a horizontal bar chart:

```python
fig, ax = plt.subplots()
ax.barh(departments, sales, color="steelblue")
ax.set(title="Sales by Department", xlabel="Sales ($)", ylabel="Department")
plt.show()
```

---

## 6. Scatter Plots: Relationships Between Variables

A scatter plot helps investigate whether two numerical variables are related. A relationship does not prove that one variable causes the other.

```python
advertising_spend = [100, 150, 200, 250, 300, 350]
orders = [18, 24, 31, 35, 43, 49]

fig, ax = plt.subplots()
ax.scatter(advertising_spend, orders, color="darkorange")
ax.set(title="Advertising Spend and Orders", xlabel="Advertising Spend ($)", ylabel="Orders")
ax.grid(True, alpha=0.3)
plt.show()
```

Look for clusters, unusual points, and upward or downward patterns. Add a third variable only when the visual encoding remains easy to interpret.

---

## 7. Histograms: Understanding Distributions

A histogram groups numerical values into bins. Use it to inspect the shape, spread, and skew of a distribution.

```python
delivery_times = [22, 25, 27, 28, 29, 30, 31, 32, 34, 35, 38, 42, 55]

fig, ax = plt.subplots()
ax.hist(delivery_times, bins=6, edgecolor="white", color="cornflowerblue")
ax.set(title="Delivery Time Distribution", xlabel="Minutes", ylabel="Number of Deliveries")
plt.show()
```

The choice of `bins` affects how the distribution looks. Try a few sensible values and avoid interpreting small visual differences as important findings.

---

## 8. Box Plots: Spread and Outliers

A box plot summarizes a distribution using quartiles and can help compare spread across groups. Points beyond the whiskers may be potential outliers; they are not automatically errors.

```python
weekday_sales = [18, 20, 22, 24, 25, 27, 29, 33]
weekend_sales = [25, 28, 30, 31, 35, 38, 45, 52]

fig, ax = plt.subplots()
ax.boxplot([weekday_sales, weekend_sales], tick_labels=["Weekday", "Weekend"])
ax.set(title="Sales by Day Type", ylabel="Sales ($ thousands)")
plt.show()
```

---

## 9. Labels, Legends, and Annotations

Clear labels make a chart understandable without requiring the reader to inspect your code.

```python
months = ["Jan", "Feb", "Mar", "Apr"]
profit = [320, 410, 390, 520]

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(months, profit, marker="o", color="seagreen", label="Profit")
ax.set_title("Monthly Profit", loc="left")
ax.set_xlabel("Month")
ax.set_ylabel("Profit ($ thousands)")
ax.legend()
ax.annotate("Highest month", xy=(3, 520), xytext=(2, 560), arrowprops={"arrowstyle": "->"})
fig.tight_layout()
plt.show()
```

Use `figsize=(width, height)` to adjust the figure size in inches. `tight_layout()` helps prevent labels from being clipped.

---

## 10. Multiple Charts in One Figure

Subplots are useful when you want related charts to share a page while remaining separate.

```python
months = ["Jan", "Feb", "Mar", "Apr"]
revenue = [120, 150, 140, 190]
customers = [40, 48, 46, 62]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(months, revenue, marker="o")
axes[0].set(title="Revenue", xlabel="Month", ylabel="($ thousands)")

axes[1].bar(months, customers, color="coral")
axes[1].set(title="New Customers", xlabel="Month", ylabel="Customers")

fig.tight_layout()
plt.show()
```

For a grid, pass the number of rows and columns to `plt.subplots(rows, columns)`. The returned `axes` object contains the individual plotting areas.

---

## 11. Plotting Pandas DataFrames

Matplotlib can plot Pandas data directly. This is handy after loading and summarizing data.

```python
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.DataFrame({
	"month": ["Jan", "Feb", "Mar", "Apr"],
	"north": [120, 145, 138, 170],
	"south": [100, 115, 130, 155],
})

fig, ax = plt.subplots()
ax.plot(sales["month"], sales["north"], marker="o", label="North")
ax.plot(sales["month"], sales["south"], marker="o", label="South")
ax.set(title="Monthly Sales by Region", xlabel="Month", ylabel="Sales ($ thousands)")
ax.legend()
plt.show()
```

Pandas also provides a convenient `.plot()` method, which uses Matplotlib by default:

```python
sales.plot(x="month", y=["north", "south"], kind="line", marker="o")
plt.title("Monthly Sales by Region")
plt.ylabel("Sales ($ thousands)")
plt.tight_layout()
plt.show()
```

Common Pandas plot kinds include `"line"`, `"bar"`, `"barh"`, `"hist"`, `"box"`, and `"scatter"`. For more detailed formatting, use Matplotlib's Figure and Axes methods.

---

## 12. Data Analysis Example: Summarize and Visualize

This example groups daily orders by channel, then plots the total for each channel.

```python
import pandas as pd
import matplotlib.pyplot as plt

orders = pd.DataFrame({
	"channel": ["Website", "Store", "Website", "Store", "App", "App", "Website"],
	"amount": [120, 80, 95, 110, 70, 130, 150],
})

channel_totals = orders.groupby("channel")["amount"].sum().sort_values(ascending=False)

fig, ax = plt.subplots()
channel_totals.plot(kind="bar", ax=ax, color="slateblue")
ax.set(title="Revenue by Sales Channel", xlabel="Channel", ylabel="Revenue ($)")
ax.tick_params(axis="x", rotation=0)
fig.tight_layout()
plt.show()
```

The analysis steps are:

1. Group the rows by category.
2. Aggregate the numerical measure.
3. Sort the results to make comparisons easier.
4. Plot the summarized values and label the units.

---

## 13. Styling and Saving Charts

Use colors and styles to clarify the data, not to decorate it. Matplotlib includes built-in styles:

```python
print(plt.style.available)
```

Apply a style before creating the chart:

```python
plt.style.use("ggplot")
```

Save a figure before `plt.show()` when writing a report or exporting an image:

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 6, 5], marker="o")
ax.set(title="Example Trend", xlabel="Period", ylabel="Value")
fig.tight_layout()
fig.savefig("example_trend.png", dpi=300, bbox_inches="tight")
plt.show()
```

Common formats include PNG, PDF, and SVG. Use a high `dpi` for raster images intended for print.

---

## 14. Choosing the Right Chart

| Analysis question | Useful chart |
| --- | --- |
| How does a value change over time? | Line chart |
| Which categories have larger values? | Bar chart |
| How are two numerical variables related? | Scatter plot |
| What does one numerical variable's distribution look like? | Histogram |
| How do distributions compare across groups? | Box plot |

### Visualization tips

* Give every chart a clear title and label axes with units.
* Use line charts for ordered data and bar charts for category comparisons.
* Keep category order intentional; sort when it improves comparison.
* Avoid 3D effects and unnecessary decoration.
* Do not truncate bar-chart axes in a way that exaggerates differences.
* Use a legend only when it helps distinguish multiple series.
* Check missing values and data types before interpreting a chart.

---

## 15. Practice Questions

Use this dataset:

```python
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 135, 128, 160, 175, 190]
expenses = [80, 90, 86, 105, 112, 120]
```

1. Plot monthly sales as a line chart with markers and labeled axes.
2. Plot sales and expenses on the same chart with a legend.
3. Create a bar chart showing the difference between sales and expenses each month.
4. Add an annotation to the month with the highest sales.
5. Save one chart as a PNG image.
6. Create a histogram from a list of at least 20 numerical observations and describe its shape.

---

## Summary

Matplotlib turns data into visual evidence. In data analysis, choose a chart based on the question, label it clearly, and interpret only what the data supports. Start with `plt.subplots()`, build the chart with its Axes, and use Pandas or NumPy to prepare the values you need to visualize.
