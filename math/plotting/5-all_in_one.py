#!/usr/bin/env python3
"""
The subplot thickens
Complete the following source code to plot all 5 previous graphs in one figure:

All axis labels and plot titles should have a font size of x-small (to fit nicely in one figure)
The plots should make a 3 x 2 grid
The last plot should take up two column widths (see below)
The title of the figure should be All in One

"""
import numpy as np
import matplotlib.pyplot as plt


def all_in_one():
    """5 graphs in one"""
    # 0-line
    y0 = np.arange(0, 11) ** 3
    # 1-scatter
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    # change scale
    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)

    # 3 two
    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)

    # 4 frequency
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    # your code here
    plt.figure()  # according to matplotlib: plot with various axes scales

    # 0-line
    plt.subplot(one)  # let's see how important it is to have sth in the ()
    #how to define figsize? plt.figure(figsize=(6.4, 4.8))
    plt.plot(np.arange(0, 11), y0, color='red')
    plt.xlim(0, 10)

    #1 -scatter
    plt.subplot(two) # (?)
    # plt.figure(figsize=(6.4, 4.8))
    plt.scatter(x1, y1, color='magenta')
    plt.title("Men's Height vs Weight")
    plt.xlabel('Height (in)')
    plt.ylabel('Weight (lbs)')

    # 2- change_scale
    plt.subplot(three)  # (?)
    # plt.figure(figsize=(6.4, 4.8))
    plt.plot(x2, y2)
    plt.title("Exponential Decay of C-14")
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")
    plt.gca().autoscale(enable=True, axis='x', tight=True)
    plt.yscale('log')  # log scaling of the y achsis

    # 3-two 
    plt.subplot(four)  # (?)
    # plt.figure(figsize=(6.4, 4.8))    
    plt.plot(x3, y31, 'r--', label='C-14')
    plt.plot(x3, y32, 'g-', label='Ra-226')
    plt.title('Exponential Decay of Radioactive Elements')
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.legend(loc='upper right')
    plt.xlim(0, 20000)
    plt.ylim(0, 1)

    # 4 - frequency
    plt.subplot(five)  #(?)
    #plt.figure(figsize=(6.4, 4.8))
    bin = np.arange(0, 101, 10)
    n, bins, patches = plt.hist(
        student_grades, bins=bin, edgecolor='black'
        )
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.xlim(0, 100)
    plt.ylim(0, 30)
    plt.xticks(bin)

    # show them all
    plt.show()
    