# Styling & Customization

Seaborn provides several functions for controlling the **appearance, readability, and presentation** of visualizations.

The main topics:

```text
set_theme()
set_style()
set_context()
set_palette()
figure size
titles
labels
legends
axis limits
```

---

# 1. `set_theme()`

A common starting point for Seaborn projects is:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
```

Then:

```python
df = sns.load_dataset("tips")

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

`set_theme()` applies a consistent Seaborn/Matplotlib visual theme.

---

# 2. `set_style()`

Seaborn provides several built-in styles.

Common styles include:

```text
darkgrid
whitegrid
dark
white
ticks
```

### `darkgrid`

```python
sns.set_style("darkgrid")

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

### `whitegrid`

```python
sns.set_style("whitegrid")

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

### `white`

```python
sns.set_style("white")

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

### `ticks`

```python
sns.set_style("ticks")

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

---

# 3. Which Style to Use?

| Style       | Typical Use                   |
| ----------- | ----------------------------- |
| `darkgrid`  | General EDA                   |
| `whitegrid` | Business/data reports         |
| `dark`      | Dark-background visualization |
| `white`     | Clean presentation            |
| `ticks`     | Publication-style plots       |

A common EDA setup:

```python
sns.set_theme(style="whitegrid")
```

---

# 4. `set_context()`

`set_context()` controls the **scale of plot elements**, such as fonts and lines.

Available contexts:

```text
paper
notebook
talk
poster
```

### Notebook

```python
sns.set_context("notebook")
```

### Presentation

```python
sns.set_context("talk")
```

### Large presentation

```python
sns.set_context("poster")
```

For example:

```python
sns.set_theme(
    style="whitegrid",
    context="talk"
)

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

---

# 5. Figure Size

You can control the figure size using Matplotlib:

```python
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()
```

The format is:

```python
figsize=(width, height)
```

For example:

```python
figsize=(12, 6)
```

means:

```text
Width  = 12 inches
Height = 6 inches
```

---

# 6. Titles

Use Matplotlib's `plt.title()`:

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.title("Total Bill vs Tip")

plt.show()
```

You can also use the axes object:

```python
ax = sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

ax.set_title("Total Bill vs Tip")

plt.show()
```

For production-style plotting, working with `ax` is often more flexible.

---

# 7. Axis Labels

```python
ax = sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")

plt.show()
```

You can also use:

```python
ax.set(
    xlabel="Total Bill",
    ylabel="Tip",
    title="Total Bill vs Tip"
)
```

---

# 8. Axis Limits

Use:

```python
plt.xlim()
plt.ylim()
```

For example:

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.xlim(0, 60)
plt.ylim(0, 12)

plt.show()
```

This restricts the visible range.

---

# 9. Color Palettes

Seaborn provides many built-in palettes.

```python
sns.color_palette()
```

You can specify a palette:

```python
sns.set_palette("deep")
```

Or directly:

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex",
    palette="Set2"
)

plt.show()
```

---

# 10. Common Palette Types

Some commonly used palettes:

```text
deep
muted
bright
pastel
dark
colorblind
Set1
Set2
Set3
viridis
magma
rocket
```

Example:

```python
sns.set_palette("colorblind")
```

For categorical visualizations:

```python
sns.barplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex",
    palette="Set2"
)

plt.show()
```

---

# 11. Sequential vs Diverging Palettes

This is important for data visualization.

### Sequential

Used when values progress from low → high.

Examples:

```text
viridis
magma
Blues
Greens
```

Example:

```python
sns.heatmap(
    df.select_dtypes("number").corr(),
    cmap="viridis"
)

plt.show()
```

### Diverging

Useful when values have a meaningful center, such as:

```text
negative ← 0 → positive
```

For example:

```python
sns.heatmap(
    df.select_dtypes("number").corr(),
    cmap="coolwarm",
    annot=True
)

plt.show()
```

---

# 12. Removing Spines

Seaborn provides:

```python
sns.despine()
```

Example:

```python
sns.set_theme(style="white")

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

sns.despine()

plt.show()
```

This removes unnecessary plot borders.

---

# 13. Rotating Axis Labels

Suppose category names are long.

```python
sns.countplot(
    data=df,
    x="day"
)

plt.xticks(rotation=45)

plt.show()
```

For more control:

```python
plt.xticks(rotation=45, ha="right")
```

This is especially useful for:

```text
Long product names
Long department names
Dates
City names
Categories
```

---

# 14. Legend Position

You can control the legend through Matplotlib.

```python
ax = sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex"
)

ax.legend(
    title="Gender",
    loc="upper left"
)

plt.show()
```

---

# 15. Removing the Legend

If the legend isn't needed:

```python
ax = sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex"
)

ax.legend_.remove()

plt.show()
```

---

# 16. Professional Plot Example

A clean reusable pattern:

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(
    style="whitegrid",
    context="notebook"
)

fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex",
    style="smoker",
    ax=ax
)

ax.set_title("Relationship Between Total Bill and Tip")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")

sns.despine()

plt.tight_layout()
plt.show()
```

Notice the use of:

```text
fig
ax
```

This becomes particularly important when building **multiple charts in a single figure**.

---

# 17. Why Use `ax`?

Instead of:

```python
sns.scatterplot(...)
plt.title(...)
```

you can explicitly work with an Axes object:

```python
fig, ax = plt.subplots()

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    ax=ax
)

ax.set_title("Bill vs Tip")
```

This is more flexible because you can control exactly **which axes** the Seaborn plot belongs to.

---

# 18. `tight_layout()`

Use:

```python
plt.tight_layout()
```

before displaying or saving the figure.

It helps prevent:

* Overlapping labels
* Cut-off titles
* Crowded axes

Example:

```python
plt.tight_layout()
plt.show()
```

---

# 19. Saving a Seaborn Plot

Since Seaborn uses Matplotlib underneath, you can save the figure with:

```python
plt.savefig(
    "sales_analysis.png",
    dpi=300,
    bbox_inches="tight"
)
```

For example:

```python
fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(
    data=df,
    x="day",
    y="total_bill",
    ax=ax
)

ax.set_title("Average Bill by Day")

plt.tight_layout()

plt.savefig(
    "average_bill_by_day.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
```

For reports and presentations, `dpi=300` is commonly useful for raster images.

---

# 20. A Reusable Seaborn Configuration

For an EDA notebook:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(
    style="whitegrid",
    context="notebook"
)
```

Then individual plots can focus on the data:

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex"
)

plt.title("Total Bill vs Tip")
plt.tight_layout()
plt.show()
```

---

# 21. Important Styling Functions

| Function             | Purpose                   |
| -------------------- | ------------------------- |
| `sns.set_theme()`    | Global theme              |
| `sns.set_style()`    | Background/grid style     |
| `sns.set_context()`  | Scale of plot elements    |
| `sns.set_palette()`  | Default color palette     |
| `sns.despine()`      | Remove unnecessary spines |
| `plt.figure()`       | Create/configure figure   |
| `plt.subplots()`     | Create figure + axes      |
| `plt.tight_layout()` | Prevent layout overlap    |
| `plt.savefig()`      | Save visualization        |

---

# 22. Styling Mental Model

```text
                  Seaborn Styling
                        │
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
       Theme          Context       Palette
          │             │             │
     set_theme()   set_context()  set_palette()
          │
      set_style()
          │
          ↓
       Plot
          │
     ┌────┴────┐
     ↓         ↓
  Labels     Legend
     │         │
     └────┬────┘
          ↓
      tight_layout()
          ↓
      savefig()
```
