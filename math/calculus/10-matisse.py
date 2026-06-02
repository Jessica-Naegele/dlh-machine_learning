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

    h_poly = poly[:]

    for i in range(le):
        d = h_poly[0] * i
        h_poly = h_poly[1:]
        r.append(d)
    r = r[1:]
    return r
