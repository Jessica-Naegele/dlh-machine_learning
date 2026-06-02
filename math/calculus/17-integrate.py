#!/usr/bin/env python3
"""Writing a function that calculates integral of a polynomial"""


def poly_integral(poly, C=0):
    """function to return a poly derivative"""
    r = []  # result list

    if not isinstance(C, int):
        # is C in correct format
        return None

    if not isinstance(poly, list) or not poly:
        # is poly in correct format, is poly not NULL
        return None

    for i in poly:  # check whethr poly is valid
        if not isinstance(i, int):
            return None

    r = r = [int(poly[i] / (i + 1)) if (poly[i] / (i + 1)) % 1 == 0
             else (poly[i] / (i + 1)) for i in range(0, len(poly))]

    integral = [C]
    integral.extend(r)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
