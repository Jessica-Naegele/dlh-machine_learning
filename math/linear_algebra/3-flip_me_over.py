#!/usr/bin/env python3
"""Create function to transpose. using numpy?"""


def matrix_transpose(matrix):
    """Function with numpy to transpose?"""
    size = []
    current_layer = matrix
    while isinstance(current_layer, list):
        current_layer = current_layer[0]
        size.append(len(current_layer))
    # calculate size for mutlidimensional matrix
    transpose = []
#    if len(size) == 2:
    for i in range(0, size[1]):
        r = []
        for row in mat2:
            # print(row[i])
            r.append(row[i])
        transpose.append(r)
    return transpose
