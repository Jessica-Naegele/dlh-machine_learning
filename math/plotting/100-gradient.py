#!/usr/bin/env python3
"""creating a gradiant scatter"""
import numpy as np
import matplotlib.pyplot as plt


def gradient():
    """This scatter is a gradiant"""

    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))
    plt.figure(figsize=(6.4, 4.8))

    # your code here
    scatter = plt.scatter(x, y, c=z, cmap='viridis')
    plt.title("Mountain Elevation")
    plt.xlabel('x coordinate (m)')
    plt.ylabel('y coordinate (m)')
    cbar = plt.colorbar(scatter)
    cbar.set_label("elevation (m)")
    # plt.zlabel('elevation (m)')  # z gibt es nicht
    # plt.xlim(0, 10)  # limits the x achsis
    plt.show()
