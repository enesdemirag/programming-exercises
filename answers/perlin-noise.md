### Answer - Perlin Noise

```python
from opensimplex import OpenSimplex
import numpy as np
import matplotlib.pyplot as plt

noise = OpenSimplex()
n = 100
x = [i for i in range(n)]
y = []

for i in np.linspace(0, 10, n):
    y.append(noise.noise2d(i, 0))

plt.xlim((0, n))
plt.ylim((-1, 1))
plt.scatter(x, y)
plt.plot(x, y, 'r')
plt.show()

```

_Go to [question](https://github.com/enesdemirag/programming-exercises/blob/master/questions/perlin-noise.md)._
