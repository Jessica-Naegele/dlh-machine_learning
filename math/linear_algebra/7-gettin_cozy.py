#!/usr/bin/env python3
""" Function concatenates two matrices along a specific axis
You can assume that mat1 and mat2 are 2D matrices containing ints/floats
You can assume all elements in the same dimension are of the same type/shape
You must return a new matrix
If the two matrices cannot be concatenated, return None

"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Function concatenates two matrices along a specific axis"""
    try:
        if axis == 0:
            # Check if widths (number of columns) match
            if len(mat1[0]) != len(mat2[0]):
                return None
            return [row[:] for row in mat1] + [row[:] for row in mat2]
        elif axis == 1:
            if len(mat1) != len(mat2):
                return None
            new_mat = []
            for i in range(len(mat1)):
                new_row = mat1[i][:] + mat2[i][:]
                new_mat.append(new_row)
            return new_mat
        return None
    except (IndexError, TypeError):
        return None
