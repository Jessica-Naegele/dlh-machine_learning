#!/usr/bin/env python3
"""Das Freaquancy hat dieses Jahr ein nettes Lineup"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Histogram"""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # your code here
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

    plt.show()
