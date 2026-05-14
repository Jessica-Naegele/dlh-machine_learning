#!/usr/bin/env python3
""" function that transposes a matrix
You can assume that matrix can be interpreted as a numpy.ndarray
You are not allowed to use any loops or conditional statements
You must return a new numpy.ndarray
"""

import numpy as np


def np_transpose(matrix):
    """function to transpose a matrix with np"""
    new_mat = np.array(matrix)
    return new_mat.transpose()
