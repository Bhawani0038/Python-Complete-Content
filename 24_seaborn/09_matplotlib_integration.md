# Matplotlib Integration

Seaborn is built on top of Matplotlib, so in real projects you will often use **both together**.

The basic pattern is:

```python
fig, ax = plt.subplots()

sns.scatterplot(data=df, x="x", y="y", ax=ax)

ax.set_title("My Plot")

plt.show()
```

---

## 9.1 Why Use Matplotlib with Seaborn?

Seaborn is excellent for:

* Creating attractive statistical plots
* Working with DataFrames
* Grouping using `hue`
* Statistical visualizations

Matplotlib gives more control over:

* Figure size
* Titles
* Axis labels
* Multiple plots
* Annotations
* Saving figures
* Subplot layouts

So a common workflow is:

```text
Pandas
   ↓
Data Preparation
   ↓
Seaborn
   ↓
Create Visualization
   ↓
Matplotlib
   ↓
Customize Visualization
```

---

# 9.2 `Figure` and `Axes`

This is one of the most important concepts.

```python
fig, ax = plt.subplots()
```

There are two objects:

### `fig`

The complete figure/canvas.

### `ax`

The individual plotting area.

Think:

```text
Figure
┌───────────────────────────────┐
│                               │
│        Axes                   │
│      ┌─────────────┐          │
│      │             │          │
│      │    Plot     │          │
│      │             │          │
│      └─────────────┘          │
│                               │
└───────────────────────────────┘
```

---

# 9.3 Passing `ax` to Seaborn

```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=ax
)

plt.show()
```

The important part is:

```python
ax=ax
```

It tells Seaborn:

> Draw this plot on this specific Matplotlib Axes.

---

# 9.4 Customize Using `ax`

Instead of:

```python
plt.title()
plt.xlabel()
plt.ylabel()
```

you can use:

```python
ax.set_title()
ax.set_xlabel()
ax.set_ylabel()
```

Example:

```python
fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=ax
)

ax.set_title("Total Bill vs Tip")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip Amount")

plt.show()
```

---

# 9.5 Multiple Subplots

This is where Matplotlib becomes especially useful.

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
```

This creates:

```text
┌────────────────┬────────────────┐
│                │                │
│    axes[0]     │    axes[1]     │
│                │                │
└────────────────┴────────────────┘
```

Now we can put different Seaborn plots into each Axes.

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=axes[0]
)

sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    ax=axes[1]
)

plt.tight_layout()
plt.show()
```

---

# 9.6 Two Rows and Two Columns

```python
fig, axes = plt.subplots(
    2,
    2,
    figsize=(12, 8)
)
```

Structure:

```text
┌───────────────┬───────────────┐
│   axes[0,0]    │   axes[0,1]   │
├───────────────┼───────────────┤
│   axes[1,0]    │   axes[1,1]   │
└───────────────┴───────────────┘
```

Example:

```python
fig, axes = plt.subplots(
    2,
    2,
    figsize=(12, 8)
)

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=axes[0, 0]
)

sns.histplot(
    data=df,
    x="total_bill",
    ax=axes[0, 1]
)

sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    ax=axes[1, 0]
)

sns.barplot(
    data=df,
    x="day",
    y="tip",
    ax=axes[1, 1]
)

plt.tight_layout()
plt.show()
```

This creates a small **EDA dashboard**.

---

# 9.7 Different Titles for Each Plot

```python
fig, axes = plt.subplots(
    1, 2,
    figsize=(12, 5)
)

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=axes[0]
)

axes[0].set_title("Bill vs Tip")

sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    ax=axes[1]
)

axes[1].set_title("Bill by Day")

plt.tight_layout()
plt.show()
```

---

# 9.8 Sharing Axes

Sometimes multiple plots should use the same axis scale.

```python
fig, axes = plt.subplots(
    1,
    2,
    figsize=(12, 5),
    sharey=True
)
```

`sharey=True` means both plots share the same Y-axis.

Similarly:

```python
sharex=True
```

shares the X-axis.

---

# 9.9 Combining Different Seaborn Plots

A practical EDA dashboard:

```python
fig, axes = plt.subplots(
    2,
    2,
    figsize=(14, 10)
)

# 1. Relationship
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=axes[0, 0]
)
axes[0, 0].set_title("Bill vs Tip")


# 2. Distribution
sns.histplot(
    data=df,
    x="total_bill",
    kde=True,
    ax=axes[0, 1]
)
axes[0, 1].set_title("Bill Distribution")


# 3. Category comparison
sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    ax=axes[1, 0]
)
axes[1, 0].set_title("Bill by Day")


# 4. Category average
sns.barplot(
    data=df,
    x="day",
    y="tip",
    ax=axes[1, 1]
)
axes[1, 1].set_title("Average Tip by Day")

plt.tight_layout()
plt.show()
```

This is a very common **Data Analyst / Data Scientist EDA pattern**.

---

# 9.10 Adding Annotations

Matplotlib can add text to a Seaborn plot.

```python
fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=ax
)

ax.annotate(
    "High Tip",
    xy=(45, 9),
    xytext=(50, 10)
)

plt.show()
```

This is useful for highlighting:

* Outliers
* Important points
* Maximum values
* Minimum values
* Business events

---

# 9.11 Rotate X-axis Labels

Useful when category names are long.

```python
fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(
    data=df,
    x="day",
    y="total_bill",
    ax=ax
)

ax.tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.show()
```

---

# 9.12 Removing Unnecessary Spines

```python
sns.despine()
```

Or with an Axes:

```python
sns.despine(ax=ax)
```

Example:

```python
fig, ax = plt.subplots()

sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    ax=ax
)

sns.despine(ax=ax)

plt.show()
```

---

# 9.13 Save the Final Visualization

Use:

```python
plt.savefig(
    "sales_analysis.png",
    dpi=300,
    bbox_inches="tight"
)
```

Example:

```python
fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=ax
)

ax.set_title("Total Bill vs Tip")

plt.tight_layout()

plt.savefig(
    "bill_vs_tip.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
```

---

# 9.14 Professional Visualization Pattern

For projects, this pattern is worth remembering:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="time",
    ax=ax
)

ax.set_title("Total Bill vs Tip")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")

sns.despine(ax=ax)

plt.tight_layout()
plt.show()
```

### Mental model

```text
plt.subplots()
      ↓
Create Figure + Axes
      ↓
Seaborn plot
      ↓
Pass ax=ax
      ↓
Customize with ax
      ↓
tight_layout()
      ↓
show() / savefig()
```

---

## Quick Reference

| Task                | Code                       |
| ------------------- | -------------------------- |
| Create figure       | `fig, ax = plt.subplots()` |
| Set size            | `figsize=(10, 6)`          |
| Use Seaborn on Axes | `ax=ax`                    |
| Title               | `ax.set_title()`           |
| X label             | `ax.set_xlabel()`          |
| Y label             | `ax.set_ylabel()`          |
| Multiple plots      | `plt.subplots(rows, cols)` |
| Rotate labels       | `ax.tick_params()`         |
| Remove spines       | `sns.despine(ax=ax)`       |
| Adjust layout       | `plt.tight_layout()`       |
| Save                | `plt.savefig()`            |

#
