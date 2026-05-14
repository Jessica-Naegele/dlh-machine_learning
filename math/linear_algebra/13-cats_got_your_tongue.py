#!/usr/bin/env python3
"""function concatenates two matrices along a specifc axis"""


def np_cat(mat1, mat2, axis=0):
    import numpy as np
    print(f"axis: {axis}")
    new_mat = np.concatenate((mat1, mat2), axis)
    return new_mat
