#!/usr/bin/env python3
"""function slicing a matrix with np"""


def np_slice(matrix, axes={}):
    """function slicing a matrix"""
    """ axes={1: (1, 3)}
        1: key 
        (1,3) -  
        print(arr[1, 1:4])
        axes={0: (2,), 2: (None, None, -2)})
        print(arr[0:2, 1:4])
    """
    selection = [slice(None)] * matrix.ndim
    for axis, values in axes.items():
        selection[axis] = slice(*values)
    return matrix[tuple(selection)]
