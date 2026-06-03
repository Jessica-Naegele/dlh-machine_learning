#!/usr/bin/env python3
"""
Complete the following source code to plot x ↦ y as a line graph:
The x-axis should be labeled Time (years)
The y-axis should be labeled Fraction Remaining
The title should be Exponential Decay of C-14
The y-axis should be logarithmically scaled
The x-axis should range from 0 to 28650
"""
import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    """labeling, title, scaling"""
    x = np.arange(0, 28651, 5730)
    r = np.log(0.5)
    t = 5730
    y = np.exp((r / t) * x)
    plt.figure(figsize=(6.4, 4.8))

    # your code here
    plt.plot(x, y)
    plt.title("Exponential Decay of C-14")
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")
    plt.gca().autoscale(enable=True, axis='x', tight=True)
    plt.yscale('log')  # log scaling of the y achsis
    plt.show()
