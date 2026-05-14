#!/usr/bin/env python3
"""function concatenates two matrices along a specifc axis"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """documentation"""
    new_mat = np.concatenate((mat1, mat2), axis=axis)
    return new_mat
