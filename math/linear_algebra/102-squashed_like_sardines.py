#!/usr/bin/env python3
"""concatenates two matrices along a specific axis"""


def matrix_shape(matrix):
    """function defines matrix size"""
    size = []
    current_layer = matrix
    while isinstance(current_layer, list):
        size.append(len(current_layer))
        current_layer = current_layer[0]
    return size


def con_recursive(item1, item2, axis):
    """recursive function returning two lists to concatinate"""
    if axis == 0:  # Base Camp: that's the aim
        return item1 + item2
    else:  # recursive step (aka the loop which isn't a loop)
        return [con_recursive(sub1, sub2, axis - 1)
                for sub1, sub2 in zip(item1, item2)]


def cat_matrices(mat1, mat2, axis=0):
    """function to concatinate matrixes along an axis"""
    shape1 = matrix_shape(mat1)
    shape2 = matrix_shape(mat2)
    if len(shape1) != len(shape2):  # same number of dimensions?
        return None
    for i in range(len(shape1)):
        # Does every dimension match Except the target axis?
        if i != axis and shape1[i] != shape2[i]:
            return None
    return con_recursive(mat1, mat2, axis)
