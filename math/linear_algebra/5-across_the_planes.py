#!/usr/bin/env python3
"""Create a function adding two matrices elementwise"""


def add_matrices2D(mat1, mat2):
    size1 = []
    current_layer = mat1
    new_m = []
    while isinstance(current_layer, list):
        size1.append(len(current_layer))
        current_layer = current_layer[0]
    size2 = []
    current_layer = mat2
    while isinstance(current_layer, list):
        size2.append(len(current_layer))
        current_layer = current_layer[0]
    if size1 == [2, 2] and size2 == [2, 2]:
        for i in range(0, len(mat1)):
            r = []
            for j in range(0, len(mat1[i])):
                r.append(mat1[i][j] + mat2[i][j])
            new_m.append(r)
        return new_m
    else:
        return None
