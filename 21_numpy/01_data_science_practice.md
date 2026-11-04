# NumPy for Data Science & DA — Practice Sheet

## Part A — ML Evaluation Metrics

### Q1. Calculate MAE

A model predicts house prices. Calculate **Mean Absolute Error (MAE)** using NumPy.

| House | Actual Price | Predicted Price |
| ----: | -----------: | --------------: |
|     1 |          250 |             260 |
|     2 |          320 |             310 |
|     3 |          400 |             420 |
|     4 |          280 |             275 |
|     5 |          500 |             530 |

**Task:**

```python
actual = np.array([...])
predicted = np.array([...])
```

Calculate MAE using NumPy.

---

### Q2. Calculate MSE

A model predicts employee salaries.

| Employee | Actual Salary | Predicted Salary |
| -------: | ------------: | ---------------: |
|        1 |         40000 |            42000 |
|        2 |         45000 |            44000 |
|        3 |         50000 |            53000 |
|        4 |         55000 |            54000 |
|        5 |         60000 |            57000 |

**Task:** Calculate MSE using NumPy.

---

### Q3. Calculate RMSE

A model predicts monthly sales.

| Month | Actual Sales | Predicted Sales |
| ----- | -----------: | --------------: |
| Jan   |          120 |             125 |
| Feb   |          150 |             145 |
| Mar   |          180 |             190 |
| Apr   |          200 |             195 |
| May   |          220 |             230 |

**Task:** Calculate RMSE using NumPy.

---

### Q4. Compare MAE, MSE and RMSE

Given:

```python
actual = np.array([100, 120, 150, 180, 200])
predicted = np.array([105, 115, 160, 170, 215])
```

Calculate:

* MAE
* MSE
* RMSE

**Question:** Which metric is in the same unit as the original target?

---

### Q5. Find Maximum Prediction Error

A machine-learning model predicts delivery time.

```python
actual = np.array([30, 45, 60, 75, 90])
predicted = np.array([32, 40, 65, 70, 100])
```

Calculate:

1. Absolute errors
2. Maximum error
3. Index of the observation having maximum error

Useful NumPy functions:

```python
np.abs()
np.max()
np.argmax()
```

---

## Part B — R² Score

### Q6. Calculate R²

Actual and predicted marks:

```python
actual = np.array([50, 60, 70, 80, 90])
predicted = np.array([52, 58, 72, 78, 88])
```

Calculate R² using the formula:

$$
R^2 = 1-\frac{SS_{res}}{SS_{tot}}
$$

Use NumPy functions such as:

```python
np.mean()
np.sum()
```

---

# Part C — Data Preprocessing

## Q7. Min-Max Normalisation

A dataset contains students' study hours:

```python
study_hours = np.array([2, 4, 5, 7, 8, 10])
```

Apply Min-Max Normalisation:

$$
x'=\frac{x-x_{min}}{x_{max}-x_{min}}
$$

**Tasks:**

1. Find minimum.
2. Find maximum.
3. Normalize the data.
4. Verify that minimum is `0` and maximum is `1`.

---

## Q8. Normalise Employee Experience

```python
experience = np.array([1, 3, 5, 8, 10, 15])
```

Convert the values into the range **0–1** using NumPy.

---

## Q9. Standardisation

Given student marks:

```python
marks = np.array([45, 50, 55, 60, 65, 70, 75])
```

Calculate the Z-score:

$$
z=\frac{x-\mu}{\sigma}
$$

**Tasks:**

1. Calculate mean.
2. Calculate standard deviation.
3. Calculate standardized values.
4. Verify the new mean is approximately `0`.

---

## Q10. Standardise Multiple Features

Consider:

```python
data = np.array([
    [20, 30000],
    [25, 35000],
    [30, 40000],
    [35, 45000],
    [40, 50000]
])
```

Columns:

```text
Age | Salary
```

Standardise each column separately.

**Hint:**

```python
np.mean(data, axis=0)
np.std(data, axis=0)
```

---

# Part D — Creating ML Functions

## Q11. Create MAE Function

Create:

```python
def mae(actual, predicted):
    ...
```

Test it using:

```python
actual = np.array([100, 150, 200, 250, 300])
predicted = np.array([110, 140, 210, 240, 310])
```

---

## Q12. Create MSE Function

Create:

```python
def mse(actual, predicted):
    ...
```

Use:

```python
actual = np.array([50, 70, 90, 110, 130])
predicted = np.array([55, 65, 95, 105, 125])
```

---

## Q13. Create RMSE Function

Create:

```python
def rmse(actual, predicted):
    ...
```

Use:

```python
actual = np.array([200, 250, 300, 350, 400])
predicted = np.array([210, 240, 310, 340, 390])
```

---

# Part E — Activation Functions

## Q14. Create Sigmoid Function

Create:

```python
def sigmoid(x):
    ...
```

Use:

```python
x = np.array([-5, -2, -1, 0, 1, 2, 5])
```

Formula:

$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

**Tasks:**

1. Calculate sigmoid values.
2. Identify the value of sigmoid at `x = 0`.
3. Observe what happens when `x` becomes very positive or negative.

---

## Q15. Create ReLU Function

Create:

```python
def relu(x):
    ...
```

Use:

```python
x = np.array([-10, -5, -2, 0, 3, 7, 10])
```

Formula:

$$
ReLU(x)=max(0,x)
$$

Expected concept:

```text
Negative values → 0
Positive values → unchanged
```

---

# Part F — Classification with NumPy

## Q16. Calculate Classification Accuracy

A model predicts whether customers will leave a company.

```python
actual = np.array([
    1, 0, 1, 1, 0,
    0, 1, 0, 1, 1
])

predicted = np.array([
    1, 0, 0, 1, 1,
    0, 1, 0, 1, 0
])
```

Calculate accuracy using NumPy.

**Hint:**

```python
actual == predicted
np.mean()
```

---

## Q17. Convert Probabilities into Classes

A Logistic Regression model produces these probabilities:

```python
probabilities = np.array([
    0.12, 0.75, 0.43, 0.91,
    0.38, 0.62, 0.55, 0.20
])
```

Using threshold `0.5`, convert them into:

```text
0 → Negative
1 → Positive
```

Use:

```python
np.where()
```

---

## Q18. Compare Different Thresholds

Given:

```python
probabilities = np.array([
    0.15, 0.35, 0.48, 0.52,
    0.65, 0.72, 0.85, 0.95
])
```

Generate predictions using:

* Threshold `0.3`
* Threshold `0.5`
* Threshold `0.7`

Use:

```python
np.where(probabilities >= threshold, 1, 0)
```

**Question:** How does changing the threshold change the predicted classes?

---

# Part G — Combined ML Exercise

## Q19. Complete Model Evaluation

A house-price model produces:

```python
actual = np.array([
    250, 300, 350, 400, 450,
    500, 550, 600
])

predicted = np.array([
    260, 290, 360, 385,
    440, 515, 535, 620
])
```

Calculate all four:

```text
MAE
MSE
RMSE
R²
```

Create separate NumPy calculations for each metric.

---

## Q20. Build Your Own ML Utility Functions

Create the following reusable functions using **only NumPy**:

```python
mae()
mse()
rmse()
r2_score()
normalize()
standardize()
sigmoid()
relu()
accuracy()
```

Then test all functions using appropriate datasets from the previous questions.

### Recommended student progression

```text
Basic NumPy
     ↓
MAE → MSE → RMSE
     ↓
R²
     ↓
Normalization → Standardization
     ↓
Custom Functions
     ↓
Sigmoid → ReLU
     ↓
Accuracy
     ↓
Probability → Class
     ↓
Complete ML Evaluation
```


