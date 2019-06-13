#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

grid_size = 99
if grid_size % 2 ==0:
    grid_size -= 1
center = grid_size//2

def topple(grid):
    mask = grid > 3
    grid += np.roll(mask, 1, axis=1)
    grid += np.roll(mask, -1, axis=1)
    grid += np.roll(mask, 1, axis=0)
    grid += np.roll(mask, -1, axis=0)
    grid -= mask*4

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

    while grid[center,center] > 3 or grid.max() > 3:
        topple(grid)
        if grid[center,0] != 0:
            print("canvas is too small!!")
            break
    return grid

if __name__ == "__main__":
    grid = run(20000)
    draw_graph(grid)
