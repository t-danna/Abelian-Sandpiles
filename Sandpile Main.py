#!/usr/bin/env python3

import os
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

grid_size = 99
if grid_size % 2 ==0:
    grid_size -= 1
center = grid_size//2

def topple(grid, i, j):
    grid[i, j + 1] += 1
    grid[i, j - 1] += 1
    grid[i + 1, j] += 1
    grid[i - 1, j] += 1
    grid[i, j] -= 4

def unstable(grid):
    unstable_list = []
    for (x,y), i in np.ndenumerate(grid):
        if i > 3:
            unstable_list.append((x,y))
    return unstable_list

def draw_graph(grid):
    cmap = colors.ListedColormap(['black','yellow','orange','red'])
    bounds = [-.5, .5, 1.5, 2.5, 3.5]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    heatmap = plt.pcolor(grid, cmap=cmap, norm=norm)

    plt.imshow(grid)
    plt.colorbar(heatmap, ticks=[0, 1, 2, 3])
    plt.show()

def run(n):
    topple_counter = 0

    grid = np.zeros([grid_size, grid_size])
    grid[center, center] = n

    to_topple = [(center, center)]
    while to_topple:
        for (i, j) in to_topple:
            topple(grid, i, j)
        to_topple = unstable(grid)

    return grid

if __name__ == "__main__":
    # ~ grid = run(300)
    # ~ draw_graph(grid)
    from timeit import timeit
    print(timeit("run(300)", number=3, setup="from __main__ import run"))
    # 4.965258703000018 before; 2.6293157510001492 after
