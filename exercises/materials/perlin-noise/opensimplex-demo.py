from opensimplex import OpenSimplex
import numpy as np
from mayavi import mlab

def generate_terrain(n):
    noise = OpenSimplex()
    z = [[0 for x in range(n)] for y in range(n)] # Create empty 2D matrix
    for i in range(n):
        for j in range(n):
            z[i][j] = (noise.noise2d(((i + 1) / 10), ((j + 1) / 10)) + 1) * 10 # Add noise value
    return z

z = generate_terrain(100) # 100*100 terrain
mlab.surf(z) # Surface Plot
mlab.show()