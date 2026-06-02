#!/usr/bin/env python3
"""Writing a function that calculates derivative of a polynomial"""


def poly_derivative(poly):
    """function to return a poly derivative"""
    r = []  # result list

    if not isinstance(poly, list) or not poly:
        # is poly in correct format, is poly not NULL
        return None
    
    if len(poly) == 1:  # check if derivative = 0
        return [0]

    for i in poly:  # check whethr poly is valid
        if type(i) not in (int, float):
            return None

    r = [i * poly[i] for i in range(1, len(poly))]

    while len(r) > 1 and r[-1] == 0:
        r.pop()

    return r
