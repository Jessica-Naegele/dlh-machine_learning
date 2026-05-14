#!/usr/bin/env python3
"""function slicing a matrix with np"""


def np_slice(matrix, axes={}):
    """function slicing a matrix"""
    selection = [slice(None)] * matrix.ndim
    for axis, values in axes.items():
        selection[axis] = slice(*values)
    return matrix[tuple(selection)]
