#!/usr/bin/env python3
"""Writing a function that calculates derivative of a polynomial"""


def poly_derivative(poly):
    """function to return a poly derivative"""
    le = len(poly)  # length
    r = []  # result list

    if not isinstance(poly, list) or not poly:
        # is poly in correct format, is poly not NULL
        return None
    if le == 1:  # check if derivative = 0
        return [0]

    for i in poly:  # check whethr poly is valid
        if type(i) not in (int, float):
            return None

    r = [i * poly[i] for i in range(1, le)]
    return r
