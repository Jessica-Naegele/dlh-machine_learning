#!/usr/bin/env python3
"""
Write a function def determinant(matrix): 
that calculates the determinant of a matrix:

matrix is a list of lists whose determinant should be calculated
If matrix is not a list of lists, raise a TypeError with the 
message matrix must be a list of lists
If matrix is not square, raise a ValueError with the message 
matrix must be a square matrix
The list [[]] represents a 0x0 matrix
Returns: the determinant of matrix
"""


def matrix_shape(matrix):
    """function defines matrix size"""
    size = []
    current_layer = matrix
    while isinstance(current_layer, list):
        size.append(len(current_layer))
        current_layer = current_layer[0]
    return size





def determinant(matrix):
    """Function to calculate the determinant"""
    try:
        size = matrix_shape(matrix)
        print(f"size: {size}")  # helper
        det = 0
        if matrix == [[]]:
            return det
        elif size == (1):
            det = matrix[0][0]
        elif size == (2, 2):
            det = matrix[0][0] * matrix[0][0] - matrix[1][0] * matrix[1][1]
        else: 
            for i in range(len(matrix)):
                if (i % 2) == 0:
                    a = matrix[i][i]
                else:
                    a = - matrix[i][i]
                for j in range(len(matrix[0])):
                    h_mat = matrix[1:]
                    print(f"h_mat : {h_mat}")





    except TypeError:
        """If matrix is not a list of lists, raise a 
        TypeError with the message matrix must be a 
        list of lists"""
        raise "matrix must be a list of lists"
    except ValueError:
        raise "matrix must be a square matrix"