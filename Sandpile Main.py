#!/usr/bin/env python3


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

grid_size = 99
if grid_size % 2 ==0:
    grid_size -= 1
center = grid_size//2
mask = np.zeros([grid_size, grid_size])

def topple(grid):
    mask = grid > 3
    grid += np.roll(mask, 1, axis=1)
    grid += np.roll(mask, -1, axis=1)
    grid += np.roll(mask, 1, axis=0)
    grid += np.roll(mask, -1, axis=0)
    grid -= mask*4

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

    while grid.max() > 3:
        topple(grid)
    return grid

if __name__ == "__main__":
    from timeit import timeit
    print(timeit("run(300)", number=3, setup="from __main__ import run"))
    # 2.6293157510001492 before;  after 0.10332873700099299
