#!/usr/bin/env python3
"""Function perfoming element-wise addition, subtraction,
multiplicaiton and division
You can assume that mat1 and mat2 can be interpreted as numpy.ndarrays
You should return a tuple containing the element-wise sum,
difference, product, and quotient, respectively
You are not allowed to use any loops or conditional statements
You can assume that mat1 and mat2 are never empty
"""


def np_elementwise(mat1, mat2):
    """Function returning add sub mul div"""
    tp = []
    add = mat1 + mat2
    tp.append(add)
    sub = mat1 - mat2
    tp.append(sub)
    mul = mat1 + mat2
    tp.append(mul)
    div = mat1 / mat2
    tp.append(div)

    tp = tuple(tp)

    return tp
