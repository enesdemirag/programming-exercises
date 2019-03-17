### Theoretical - Linear Regression

Linear Regression is a statistical analysis for predicting the value of a quantitative variable. Based on a set of independent variables, we try to estimate the magnitude of a dependent variable which is the outcome variable.

### Practical - Linear Regression

Write a function which returns the best fitting line for given data points.

```python
import random
import numpy as np
import matplotlib.pyplot as plt

# Generating the data
n = 100
err = 20
x = list(range(n)) # [0,1,...,99]
# y = a*x + b (a = 1 and b values change between - error and + error
y = [i + random.random() * 2 * err - err for i in x]

# Simple Linear Regression
def simple_regression(x, y):
    a = (np.sum(x[i]*y[i] for i in range(n)) - (1 / n) * np.sum(x) * np.sum(y)) / (np.sum(i*i for i in x) - (1 / n) * (np.sum(x) ** 2))
    b = np.mean(y) - a * np.mean(x)
    line = [a * i + b for i in x]
    return line

# Least Squares Regression
def least_squares_regression(x, y):
    m = np.sum((x[i] - np.mean(x)) * (y[i] - np.mean(y)) for i in range(n)) / np.sum((x[i] - np.mean(x)) ** 2 for i in range(n))
    b = np.mean(y) - m * np.mean(x)
    line = [m * i  + b for i in x]
    return line

simple_regression_line = simple_regression(x, y)
least_squares_regression_line = least_squares_regression(x, y)

fig, ax = plt.subplots(nrows=2, ncols=1) # 2 Subplots

ax[0].scatter(x, y) # Data Points
ax[0].plot(x, simple_regression_line, "r-") # Estimated Line
ax[0].legend(["Simple Regression Line"])

ax[1].scatter(x, y) # Data Points
ax[1].plot(x, least_squares_regression_line, "g-") # Estimated Line
ax[1].legend(["Least Squares Regression Line"])

plt.show()
```

The result should be like this.

<p align="center">
  <img width="765" height="431" src="https://web.itu.edu.tr/demirag16/img/linear-regression.png">
</p>
