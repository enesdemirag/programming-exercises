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
x_sum = np.sum(x)
y_sum = np.sum(y)
x2_sum = np.sum(i*i for i in x)
y2_sum = np.sum(i*i for i in y)
xy_sum = np.sum(x[i]*y[i] for i in range(n))

num = xy_sum - (1 / n) * x_sum * y_sum
dem = x2_sum - (1 / n) * (x_sum ** 2)
a = num / dem
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
