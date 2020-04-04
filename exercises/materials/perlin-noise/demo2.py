from opensimplex import OpenSimplex
import matplotlib.pyplot as plt

def heightmap(n):
    noise = OpenSimplex()
    z = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            z[i][j] = (noise.noise2d(((i + 1) / 10), ((j + 1) / 10)) + 1) * 10
    return z

z = heightmap(100)

map = plt.imshow(z, cmap='terrain')
plt.show()