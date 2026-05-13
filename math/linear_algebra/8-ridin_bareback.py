#!/usr/bin/env python3
"""Function that performs matrix multiplication
You can assume that mat1 and mat2 are 2D matrices containing ints/floats
You can assume all elements in the same dimension are of the same type/shape
You must return a new matrix
If the two matrices cannot be multiplied, return None
"""


def mat_mul(mat1, mat2):
    if len(mat1[0]) == len(mat2):
        """multiplication"""
        new_mat = []
        for i in range(0, len(mat1)):  # row in mat1
            row = []
            for k in range(0, len(mat2[0])):  # row in mat 2
                # row 1 mat 1 col 1 mat 2
                z = 0  # sum aka new value of the matrix
                for j in range(0, len(mat2)):  # column in mat2
                    # column 1 mat 1 row 1 mat 2
                    x = mat1[i][j] * mat2[j][k]
                    z += x
                row.append(z)
            new_mat.append(row)
        return new_mat
    else:
        return None
