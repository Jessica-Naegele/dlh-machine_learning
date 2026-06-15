#!/usr/bin/env python3
"""
calculating the probability of severy side effects using bayesion
and binomial distrubtion
"""

import numpy as np


def prod(z):
    """this is documented"""
    t = 1
    for i in range(1, z+1):
        t *= i
    return t


def likelihood(x, n, P):
    """
    Function for calculating the likelihood
    applying bayseian & binominal distribution
    x = total number of patients with side effects
    n = total number of patients
    P = 1D array --> containing various hypothetical probabilits
    of developing side effects
    """
    # Sanity Checks
    # print(f"type(P): {type(P)}") #helper
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
            )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    for i in P:
        if (i < 0 or i > 1):
            raise ValueError(
                "All values in P must be in the range [0, 1]"
                )
    # actual code
    Pp = np.empty(len(P))  # used for storing the result
    # print(f"Pp: {Pp}")
    # binom formula (n! / (x! (n-x)!) * p ** x * (1-p) ** (n-x))
    # print(f" n: {n}, x {x}")
    prod_n = prod(n)
    prod_x = prod(x)
    prod_d = prod(n-x)
    # print(f"prod_n: {prod_n} ") #helper
    # print(f"prod_x: {prod_x}")
    # print(f"prod_d {prod_d}")
    for i, v in enumerate(P):
        # print(f"({prod_n} / ({prod_x * prod_d})) *
        # ({v ** x}) * (({1 - v}) ** ({n - x}))")
        h = (prod_n / (prod_x * prod_d)) * (v ** x) * ((1 - v) ** (n - x))
        Pp[i] = h
    return Pp
