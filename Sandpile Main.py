#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors

def topple(grid):
    mask = grid > 3
    grid[:,1:] += mask[:,:-1]
    grid[:,:-1] += mask[:,1:]
    grid[1:,:] += mask[:-1,:]
    grid[:-1,:] += mask[1:,:]
    grid -= mask*4

def draw_graph(grid_size, n):
    grid = np.zeros([grid_size, grid_size])
    center = grid_size//2
    grid[center, center] = n
    
    fig = plt.figure()
    cmap = colors.ListedColormap(['black','yellow','orange','red'])
    im = plt.imshow(grid, animated=True, cmap=cmap, vmax=3)
    bounds = [-.5, .5, 1.5, 2.5, 3.5]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    heatmap = plt.pcolor(grid, cmap=cmap, norm=norm)
    plt.colorbar(heatmap, ticks=[0, 1, 2, 3])
    plt.title(f"Abelian Sandpile with {n:,} starting grains")

    def ani_update(val):
        if grid[center,center] <= 3 and grid.max() <= 3:
            ani._stop()
        topple(grid)
        im.set_array(grid)
        return im,

    ani = animation.FuncAnimation(fig, ani_update, interval=50, blit=True)
    plt.show()

def main():
    n = 5000
    grid_size = 100

    if grid_size % 2 ==0:
        grid_size -= 1

    draw_graph(grid_size, n)

if __name__ == "__main__":
    main()
