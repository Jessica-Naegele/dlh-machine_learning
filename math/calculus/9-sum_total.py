#!/usr/bin/env python3
"""Writing a function that calculates summation i sqaured"""


def summation_i_squared(n):
    """Calculates the sum of i squared from 1 to n"""
    if not isinstance(n, int) or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
