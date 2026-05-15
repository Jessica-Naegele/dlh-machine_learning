#!/usr/bin/env python3
"""writing a function that adds two matrices"""


def matrix_shape(matrix):
    """function defines matrix size"""
    size = []
    current_layer = matrix
    while isinstance(current_layer, list):
        size.append(len(current_layer))
        current_layer = current_layer[0]
    return size


def add_recursive(item1, item2):
    """Recursively drills down to add elements at the lowest layer."""
    if not isinstance(item1, list):
        return item1 + item2
    return [add_recursive(sub1, sub2) for sub1, sub2 in zip(item1, item2)]


def add_matrices(mat1, mat2):
    """Adds two matrices of any dimension if they have the same shape."""
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    return add_recursive(mat1, mat2)
