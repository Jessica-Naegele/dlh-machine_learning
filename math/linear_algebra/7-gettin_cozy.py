#!/usr/bin/env python3
""" Function concatenates two matrices along a specific axis
You can assume that mat1 and mat2 are 2D matrices containing ints/floats
You can assume all elements in the same dimension are of the same type/shape
You must return a new matrix
If the two matrices cannot be concatenated, return None

"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Function concatenates two matrices along a specific axis"""
    new_mat = []
    if axis == 0:
        new_mat.extend(mat1)
        new_mat.extend(mat2)
        return new_mat
    elif axis == 1:
        r = []
        for i in range(0, len(mat1)):
            r = mat1[i][:]
            r.extend(mat2[i])
            new_mat.append(r)
        return new_mat
    else:
        print("else")
        return None
