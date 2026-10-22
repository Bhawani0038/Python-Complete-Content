# Seaborn Module — Part 4: Matplotlib, Styling & Grids

The earlier parts focused on *which* plot to use. This part covers how to **control, style and arrange** plots.

Order of this file:

1. Matplotlib integration (`fig`, `ax`, subplots), taught first because styling code depends on it
2. Styling and customization
3. Faceting and plot grids (`FacetGrid`, `PairGrid`)

> Assumes the imports and `df = sns.load_dataset("tips")` from [Part 1](01_basics_and_relational_plots.md).

---

# A. Matplotlib Integration

Seaborn draws with Matplotlib, so real projects use both: **Seaborn creates the plot, Matplotlib controls the canvas.**

## 4.1 `Figure` and `Axes`

```python
fig, ax = plt.subplots(figsize=(10, 6))
```

- `fig`: the whole canvas (size, saving, overall title).
- `ax`: one plotting area inside it.

Pass `ax` to any **axes-level** Seaborn function (see Part 1) to draw on it:

```python
fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(data=df, x="total_bill", y="tip", ax=ax)

ax.set_title("Total Bill vs Tip")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip Amount")
plt.show()
```

`ax.set(title=..., xlabel=..., ylabel=...)` sets all three in one call.

## 4.2 Multiple Subplots (an EDA Dashboard)

`plt.subplots(rows, cols)` returns an array of Axes. Index it and pass each Axes to a different plot:

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.scatterplot(data=df, x="total_bill", y="tip", ax=axes[0, 0])
axes[0, 0].set_title("Bill vs Tip")

sns.histplot(data=df, x="total_bill", kde=True, ax=axes[0, 1])
axes[0, 1].set_title("Bill Distribution")

sns.boxplot(data=df, x="day", y="total_bill", ax=axes[1, 0])
axes[1, 0].set_title("Bill by Day")

sns.barplot(data=df, x="day", y="tip", ax=axes[1, 1])
axes[1, 1].set_title("Average Tip by Day")

plt.tight_layout()
plt.show()
```

```text
┌────────────────┬────────────────┐
│ axes[0, 0]     │ axes[0, 1]     │
├────────────────┼────────────────┤
│ axes[1, 0]     │ axes[1, 1]     │
└────────────────┴────────────────┘
```

For a 1-row layout (`plt.subplots(1, 2)`), use a single index: `axes[0]`, `axes[1]`.
Add `sharey=True` (or `sharex=True`) so panels use the same scale and can be compared fairly.

**Important:** this works only with axes-level functions. Figure-level functions (`relplot`, `displot`, `catplot`, `lmplot`) create their own figure and cannot be placed into `axes[i]`.

## 4.3 Annotations

Highlight outliers or events with Matplotlib text:

```python
ax.annotate("High tip", xy=(45, 9), xytext=(50, 10),
            arrowprops={"arrowstyle": "->"})
```

`xy` is the point being highlighted and `xytext` is where the label sits.

---

# B. Styling and Customization

## 4.4 Theme, Style and Context

`sns.set_theme()` sets everything at once:

```python
sns.set_theme(style="whitegrid", context="talk", palette="colorblind")
```

| Setting | Controls | Options |
| --- | --- | --- |
| `style` | Background and grid | `darkgrid` (default), `whitegrid`, `dark`, `white`, `ticks` |
| `context` | Scale of fonts and lines | `paper`, `notebook` (default), `talk`, `poster` |
| `palette` | Default colours | see below |

Common choices: `whitegrid` for reports, `ticks` for publications, `talk`/`poster` for slides. Individual functions `sns.set_style()`, `sns.set_context()` and `sns.set_palette()` exist if you want to change one thing.

## 4.5 Colour Palettes

Pass a palette to a single plot, or set it globally.

```python
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex", palette="Set2")
```

Choose the palette type to match the data:

| Data type | Palette type | Examples |
| --- | --- | --- |
| Unordered categories | Qualitative | `deep`, `muted`, `Set2`, `colorblind` |
| Low → high values | Sequential | `viridis`, `magma`, `Blues`, `rocket` |
| Values around a meaningful centre (e.g. correlation) | Diverging | `coolwarm`, `vlag` |

`colorblind` is a safe default when plots will be shared widely.

## 4.6 Titles, Labels, Limits, Ticks, Legend

```python
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex", ax=ax)

ax.set(title="Bill vs Tip", xlabel="Total Bill", ylabel="Tip",
       xlim=(0, 60), ylim=(0, 12))                       # axis limits
ax.tick_params(axis="x", rotation=45)                    # rotate long labels
ax.legend(title="Gender", loc="upper left")              # reposition legend
sns.despine(ax=ax)                                       # remove top/right borders
plt.tight_layout()
plt.show()
```

To remove a legend: `ax.get_legend().remove()`.

`plt.tight_layout()` prevents overlapping labels and cut-off titles. Call it just before `show()` or `savefig()`.

## 4.7 Saving a Figure

```python
fig.savefig("bill_vs_tip.png", dpi=300, bbox_inches="tight")
```

`dpi=300` is suitable for reports and slides, and `bbox_inches="tight"` avoids clipped labels. Save **before** `plt.show()`, otherwise the figure may be saved blank.

## 4.8 Reusable Pattern

```python
sns.set_theme(style="whitegrid", context="notebook")

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x="total_bill", y="tip", hue="time", ax=ax)
ax.set(title="Total Bill vs Tip", xlabel="Total Bill", ylabel="Tip")
sns.despine(ax=ax)
plt.tight_layout()
fig.savefig("plot.png", dpi=300, bbox_inches="tight")
plt.show()
```

```text
set_theme -> subplots -> Seaborn plot (ax=ax) -> customize with ax -> tight_layout -> savefig/show
```

---

# C. Faceting and Plot Grids

**Faceting** means splitting a dataset into several small plots, one per group. You have already seen the shortcut: `col=` and `row=` in `relplot`, `displot`, `catplot` and `lmplot`. `FacetGrid` and `PairGrid` are the lower-level classes behind them and give you full control.

## 4.9 `FacetGrid` — Split Data into Groups

```python
g = sns.FacetGrid(df, row="sex", col="time", hue="smoker", margin_titles=True)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.set_axis_labels("Total Bill", "Tip")
g.add_legend()
plt.show()
```

```text
                 time
             Lunch      Dinner
Male        [ plot ]   [ plot ]
Female      [ plot ]   [ plot ]
                       colour inside each plot = smoker
```

- `col=` makes panels side by side, `row=` stacks them, and both together give a 2-D grid.
- `hue=` colours groups *inside* each panel; call `g.add_legend()` to show it.
- `margin_titles=True` puts row names on the right margin for a cleaner look.
- `map_dataframe(func, x=..., y=...)` is the convenient way to use named columns. `map(func, "col1", "col2")` is the older positional style.

When to use `FacetGrid` directly: when you need a plot function that has no figure-level wrapper, or want to run custom code on each panel. Otherwise prefer `relplot`/`displot`/`catplot`.

## 4.10 `PairGrid` — Compare Variables with Each Other

`PairGrid` builds the same grid as `pairplot()` (Part 3) but lets you choose different plots for the diagonal and off-diagonal cells.

```python
pg = sns.load_dataset("penguins")

g = sns.PairGrid(pg, vars=["bill_length_mm", "bill_depth_mm", "flipper_length_mm"], hue="species")
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()
plt.show()
```

You can go further, such as `g.map_lower(sns.kdeplot)` and `g.map_upper(sns.scatterplot)` to give the two triangles different plots.

| | `pairplot()` | `PairGrid` |
| --- | --- | --- |
| Ease of use | Easiest | More code |
| Control over cells | Limited (`kind`, `diag_kind`) | Full (`map_diag`, `map_lower`, `map_upper`, `map_offdiag`) |
| Best for | Quick EDA | Customized multivariate analysis |

## 4.11 `FacetGrid` vs `PairGrid`

```text
FacetGrid  -> "Split my data into groups"       (same x/y, one panel per group)
PairGrid   -> "Compare my variables together"   (different x/y in each panel)
```

Customer example (explicit values, so results are reproducible):

```python
cust = pd.DataFrame({
    "age":            [22, 25, 28, 35, 40, 45],
    "income":         [30, 35, 42, 60, 75, 90],
    "spending_score": [80, 75, 70, 55, 40, 30],
    "gender":         ["F", "M", "F", "M", "F", "M"],
})

g = sns.FacetGrid(cust, col="gender")                       # groups: does it differ by gender?
g.map_dataframe(sns.scatterplot, x="income", y="spending_score")

sns.pairplot(cust, hue="gender")                            # variables: how do all relate?
plt.show()
```

This toy table is only for demonstrating the calls. With six rows, no real conclusion can be drawn.

## Recap

| Task | Tool |
| --- | --- |
| Place plots in your own layout | `plt.subplots()` + `ax=` |
| Look and feel | `set_theme()`, palettes, `despine()` |
| Panels by group (simple) | `col=`/`row=` on figure-level functions |
| Panels by group (custom) | `FacetGrid` |
| Variable-vs-variable grid (custom) | `PairGrid` |
