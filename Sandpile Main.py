#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

def topple(grid):
    mask = grid > 3
    grid[:,1:] += mask[:,:-1]
    grid[:,:-1] += mask[:,1:]
    grid[1:,:] += mask[:-1,:]
    grid[:-1,:] += mask[1:,:]
    grid -= mask*4

def draw_graph(grid, n):
    cmap = colors.ListedColormap(['black','yellow','orange','red'])
    bounds = [-.5, .5, 1.5, 2.5, 3.5]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    heatmap = plt.pcolor(grid, cmap=cmap, norm=norm)

    plt.imshow(grid)
    plt.colorbar(heatmap, ticks=[0, 1, 2, 3])
    plt.title(f"Abelian Sandpile with {n:,} starting grains")
    plt.show()

def run(n, grid_size):
    grid = np.zeros([grid_size, grid_size])
    center = grid_size//2
    grid[center, center] = n

    while grid[center,center] > 3 or grid.max() > 3:
        topple(grid)
    return grid

def main():
    n = 50000
    grid_size = 100

    if grid_size % 2 ==0:
        grid_size -= 1

    grid = run(n, grid_size)
    draw_graph(grid, n)

if __name__ == "__main__":
    main()
