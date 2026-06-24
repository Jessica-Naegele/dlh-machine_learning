#!/usr/bin/env python3
"""function that calculates a correlation matrix"""

import numpy as np


def correlation(C):
    """function that calculates a correlation
    Step 1: find Variances (aka i=j)
    Step 2: find Standard deviation (aka var ** 0.5)
    Step 3: calculate correlation (Rij = Cij / stdi * stdj)
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if C.shape[0] != C.shape[1] or len(C.shape) != 2:
        raise ValueError("C must be a 2D square matrix")
    # Step 1: find variances
    var = []
    for i, row in enumerate(C):
        for j, col in enumerate(row):
            if i == j:
                var.append(col)
    # Step 2: standard deviation
    std = list(map(lambda x: x ** 0.5, var))
    # Step 3: calculate correlation (Rij = Cij / stdi * stdj)
    R = []
    for i, row in enumerate(C):
        h_row = []
        for j, col in enumerate(row):
            r = col / (std[i] * std[j])
            h_row.append(r)
        # print(f"h_row: {h_row}") # helper
        R.append(h_row)
    R_arr = np.array(R)
    # print(f"R: {np.ndarray(R_arr)}") # helper
    return R_arr
