#!/usr/bin/env python3
"""Create a function adding two matrices elementwise"""


def add_matrices2D(mat1, mat2):
    """someone forgot the comment to describe the function"""
    new_m = []
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    else:
        for i in range(0, len(mat1)):
            r = []
            for j in range(0, len(mat1[i])):
                r.append(mat1[i][j] + mat2[i][j])
            new_m.append(r)
        return new_m
