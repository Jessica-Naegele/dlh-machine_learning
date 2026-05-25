#!/usr/bin/env python3
"""Function to return the minor of a matrix"""


def matrix_shape(matrix):
    """function defines matrix size"""
    size = []
    current_layer = matrix
    while isinstance(current_layer, list):
        size.append(len(current_layer))
        current_layer = current_layer[0]
    return size


def is_matrix(matrix):
    """is a matrix a matrix"""
    if not isinstance(matrix, list):
        return False
    if matrix == []:
        return False
    for row in matrix:
        if not isinstance(row, list):
            return False
    return True


def is_square(matrix):
    """is a matrix square"""
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for row in matrix:
        if len(row) != num_rows:
            raise ValueError("matrix must be a non-empty square matrix")


def cut_matrices(mat1, col):
    """cuts the columns needed"""
    new_mat = [row[:col] + row[col+1:] for row in mat1]
    return new_mat


def minor(matrix):
    """Function to calculate the determinant"""
    if is_matrix(matrix) is False:
        raise TypeError("matrix must be a list of lists")
    det = 0
    if matrix == [[]] or matrix == []:
        raise ValueError("matrix must be a non-empty square matrix")
    else:
        is_square(matrix)
        size = matrix_shape(matrix)
        new_mat = []
        if size[0] != size[1]:
            raise ValueError("raise ValueError("matrix must be a non-empty square matrix")")
        if size == [1]:
            new_mat.append(1)
        elif size == [1, 1]:
            new_mat.append(matrix[0][0])
        elif size == [2, 2]:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            new_mat.append(det)
        else:
            for i in range(len(matrix)):
                if (i % 2) == 0:
                    a = matrix[0][i]
                else:
                    a = - matrix[0][i]
                h_mat = matrix[1:]
                h_mat2 = cut_matrices(h_mat, i)
                det += a * determinant(h_mat2)
    return det
