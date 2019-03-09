### Answer - Linear Regression

```python
import random
import numpy as np
import matplotlib.pyplot as plt

n = 50
err = 10
x = list(range(n))
y = []

for i in x:
    y.append(i +random.random() * 2 * err - err)

# Estimated Line
x_mean = np.mean(x)
y_mean = np.mean(y)

a = (np.sum(x[i]*y[i] for i in range(n)) - (1 / n) * np.sum(x) * np.sum(y)) / (np.sum(i*i for i in x) - (1 / n) * (np.sum(x) ** 2))
b = y_mean - a * x_mean

line = []
for i in x:
    line.append(a * i + b)

plt.xlim((0, n))
plt.scatter(x, y)
plt.plot(x, line, "r-")
plt.legend(["Estimated Line", "Data Points"])
plt.show()
```
