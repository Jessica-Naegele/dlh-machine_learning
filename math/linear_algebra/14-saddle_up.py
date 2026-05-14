#!/usr/bin/env python3
"""Create a function for matrix mutliplication"""

import numpy as np


def np_matmul(mat1, mat2):
    """performing a matrix multiplication"""
    new_mat = np.matmul(mat1, mat2)
    return new_mat
