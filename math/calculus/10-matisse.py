#!/usr/bin/env python3
"""Writing a function that calculates derivative of a polynomial"""


def poly_derivative(poly):
    """function to return a poly derivative"""
    l2 = len(poly)  # length
    print(f"len: {l2}") #helper
    r = []  # result list
    
    if l2 == 1:  # check if derivative = 0
        return [0]
    
    for i in poly:  # check whethr poly is valid
        if type(i) not in (int, float):
            return None
    
    h_poly = poly[:-1]
    l = len(h_poly)
    print(f"h_poly: {h_poly}") #helper
    print(f"len: {l}") #helper

    while type(poly) == list:
        m = l2 - len(h_poly)
        d = h_poly.pop() * m 
        r.append(d)
    
    print(f"r: {r}") #helper
    return r




