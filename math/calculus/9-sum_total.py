#!/usr/bin/env python3
"""Writing a function that calculates summation i sqaured"""


def summation_i_squared(n):
    """Calculates the sum of i squared from 1 to n.

    Args:
        n (int): The stopping condition.

    Returns:
        int: The total sum, or None if n is invalid or less than 0.
    """
    # Reject booleans (since isinstance(True, int) is True)
    if type(n) is not int:
        return None

    # Handle negative numbers or 0
    if n < 0:
        return None
    if n == 0:
        return 0

    # Using the direct mathematical formula instead of recursion
    # Using integer division // to ensure we return an int type
    return (n * (n + 1) * (2 * n + 1)) // 6
