#!/usr/bin/env python3
"""
Complete the following source code to plot x ↦ y as a scatter plot:
The x-axis should be labeled Height (in)
The y-axis should be labeled Weight (lbs)
The title should be Men's Height vs Weight
The data should be plotted as magenta points
"""
import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """this is a documentation - I will not be tricked twice"""
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180
    plt.figure(figsize=(6.4, 4.8))

    # your code here
    plt.scatter(x, y, color='magenta')
    plt.title("Men's Height vs Weight")
    plt.xlabel('Height (in)')
    plt.ylabel('Weight (lbs)')
    # plt.xlim(0, 10)  # limits the x achsis
    plt.show()
