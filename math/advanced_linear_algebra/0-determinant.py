#!/usr/bin/env python3
"""
Write a function def determinant(matrix)
"""


def matrix_shape(matrix):
    """function defines matrix size"""
    size = []
    current_layer = matrix
    while isinstance(current_layer, list):
        size.append(len(current_layer))
        current_layer = current_layer[0]
    return size


def cut_matrices(mat1, col):
    """cuts the columns needed"""
    new_mat = [row[:col] + row[col+1:] for row in mat1]
    return new_mat


def determinant(matrix):
    """Function to calculate the determinant"""
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")
    det = 0
    if matrix == [[]]:
        det = 1
        return det
    else:
        size = matrix_shape(matrix)
        if size[0] != size[1]:
            raise ValueError("matrix must be a square matrix")
        if size == [1, 1]:
            det = matrix[0][0]
        elif size == [2, 2]:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            for i in range(len(matrix)):
                if (i % 2) == 0:
                    a = matrix[0][i]
                else:
                    a = - matrix[0][i]
                h_mat = matrix[1:]
                h_mat2 = cut_matrices(h_mat, i)
                det += a * (h_mat2[0][0] * h_mat2[1][1] -
                            h_mat2[0][1] * h_mat2[1][0])
    return det
