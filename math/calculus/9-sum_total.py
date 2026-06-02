#!/usr/bin/env python3
"""Writing a function that calculates summation i sqaured"""


def recursion(i, n):
    """recursion for the calculation"""
    # Base Case: n and i are equal
    if i == n:
        return n * n
    elif n < 0:
        return i * i + recursion(i-1, n)
    else:
        return i * i + recursion(i+1, n)


def summation_i_squared(n):
    """Function to calculate summation of i squared"""
    if not isinstance(n, int):
        return None
    return recursion(0, n)
