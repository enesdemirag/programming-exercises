### Theoretical - Linear Regression

todo

### Practical - Linear Regression

```python
import random
import numpy as np
import matplotlib.pyplot as plt

n = 50
err = 10
x = list(range(n))
y = [i + random.random() * 2 * err - err for i in x]

# Estimated Line
a = (np.sum(x[i]*y[i] for i in range(n)) - (1 / n) * np.sum(x) * np.sum(y)) / (np.sum(i*i for i in x) - (1 / n) * (np.sum(x) ** 2))
b = np.mean(y) - a * np.mean(x)

line = [a * i + b for i in x]

plt.xlim((0, n))
plt.scatter(x, y)
plt.plot(x, line, "r-")
plt.legend(["Estimated Line", "Data Points"])
plt.show()
```
