import os
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


grid_size = 349
if grid_size % 2 ==0:
    grid_size -= 1
center = math.floor(grid_size/2)


def run(n):

    grid = np.zeros([grid_size, grid_size])
    grid[center, center] = n

    def topple(i, j):
        grid[i, j + 1] += 1
        grid[i, j - 1] += 1
        grid[i + 1, j] += 1
        grid[i - 1, j] += 1
        grid[i, j] -= 4

    def unstable():
        unstable_list = []
        for (x,y), i in np.ndenumerate(grid):
            if i > 3:
                unstable_list.append((x,y))
        return unstable_list

    def stable():
        counter = 0
        for (x, y), i in np.ndenumerate(grid):
            if i > 3:
                counter += 1
                break
        if counter == 0:
            print('Stable')
            return True
        else:
            return False

    while not stable():
        for (i, j) in [(x, y) for (x, y) in unstable()]:
            topple(i, j)


    cmap = colors.ListedColormap(['black','yellow','orange','red'])
    bounds = [-.5, .5, 1.5, 2.5, 3.5]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    heatmap = plt.pcolor(grid, cmap=cmap, norm=norm)

    plt.imshow(grid)
    plt.colorbar(heatmap, ticks=[0, 1, 2, 3])
    plt.show()
