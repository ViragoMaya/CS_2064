# -*- coding: utf-8 -*-
"""
This program draws a heart using MatPlotLib.

You don't have to worry about how it does it, just make sure that it runs.
If it's successful, a heart will be saved in your folder as heartImage.png.
"""

import matplotlib 

# Since we're running Python inside a container via VS Code,
# we need to use a non-interactive backend for plotting,
# because GUI-based backends may not be supported in this environment.
matplotlib.use("Agg") # Use non-interactive backend

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm

cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)

t = np.arange(0,2*np.pi, 0.1)
x = 16*np.sin(t)**3
y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)

plt.plot(x,y, c='r')
plt.suptitle("Ghazal Tanavade")
plt.savefig("heartImage.png")
