#!/usr/bin/env python3
"""Function to return the cofactor of a matrix"""


def matrix_shape(matrix):
    """function defines matrix size"""
    size = []
    current_layer = matrix
    while isinstance(current_layer, list):
        size.append(len(current_layer))
        current_layer = current_layer[0]
    # print(f"size: {size}")  # helper
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


def cut_matrices(mat1, colrow, axis):
    """cuts the columns or row needed"""
    if axis == 0:
        new_mat = mat1[:colrow] + mat1[colrow+1:]
    else:
        new_mat = [row[:colrow] + row[colrow+1:] for row in mat1]
    return new_mat


def determinant(matrix):
    """Function to calculate the determinant"""
    det = 0
    if matrix == [[]]:
        det = 1
        return det
    else:
        size = matrix_shape(matrix)
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
                h_mat2 = cut_matrices(h_mat, i, axis=1)
                det += a * determinant(h_mat2)
    return det


def minor(matrix):
    """Function to calculate the determinant"""
    
    j = 0
    new_mat = []
    for row in matrix:
        new_row = []
        h_mat = cut_matrices(matrix, j, axis=0)
        for i in range(len(matrix)):
            h_mat2 = cut_matrices(h_mat, i, axis=1)
            size = matrix_shape(matrix)
            if size[0] == 2:
                new_row.extend(h_mat2[0])
            else:
                h = determinant(h_mat2)
                new_row.extend([h])
        new_mat.append(new_row)
        # print("new_mat j= {j} : {new_mat}")
        j += 1
    return new_mat


def cofactor(matrix):
    """calculates the cofactor of a matrix"""
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
            raise ValueError("matrix must be a non-empty square matrix")
        if size == [1, 1]:
            new_mat.append([1])
        else:
            h_mat = minor(matrix)
            new_mat = []
            for i in range (len(h_mat)):
                new_row = []
                for j in range(len(h_mat[i])):
                    z = (-1) ** (i+j) * h_mat[i][j]
                    new_row.append(z)
                new_mat.append(new_row)
        return new_mat
