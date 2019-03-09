### Answer - Perlin Noise

[Here](https://gist.github.com/eevee/26f547457522755cb1fb8739d0ea89a1) is a Python implementation of Perlin Noise. You can examine that but for simplicity I will use [OpenSimplex](https://pypi.org/project/opensimplex/) package. Using this package, we can generate 2D, 3D and 4D simplex noise in Python.

Before starting, we import opensimplex module for noise values and matplotlib for plotting the result. First, we create a OpenSimplex object. Then using numpy's ```linspace()``` function, we generate our noise values. We will create 1D noise so we just need to get one of the values of 2D noise. ```noise2d()``` function returns values between -1 and 1. Finally, we plot x values and the data values respectively using matplotlib.

```python
from opensimplex import OpenSimplex
import numpy as np
import matplotlib.pyplot as plt

noise = OpenSimplex()
n = 100 # Number of values
x = [i for i in range(n)] # List of numbers from 0 to 99

y = []
for i in np.linspace(0, 10, n): # Create 100 point from 0 to 10
    y.append(noise.noise2d(i, 0))

plt.xlim((0, n))
plt.ylim((-1, 1))
plt.scatter(x, y)
plt.plot(x, y, 'r')
plt.show()

```

You can use higher dimensional noise functions to make organic looking visuals. [Here](https://necessarydisorder.wordpress.com/2017/11/15/drawing-from-noise-and-then-making-animated-loopy-gifs-from-there/) is and example of using perlin noise to make animated loop GIFs.

_Go to [question](https://github.com/enesdemirag/programming-exercises/blob/master/questions/perlin-noise.md)._
