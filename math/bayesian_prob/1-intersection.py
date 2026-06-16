#!/usr/bin/env python3
"""
intersection of obtaining this data with various hypothetical probabilities
"""

import numpy as np


def faculty(z):
    """this is a sub function to create the faculty"""
    t = 1
    for i in range(1, z+1):
        t *= i
    return t


def likelihood(x, n, P):
    """
    Function for calculating the likelihood
    applying bayseian & binominal distribution
    """
    # Sanity Checks
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
    # binom formula (n! / (x! (n-x)!) * p ** x * (1-p) ** (n-x))
    combination_factor = faculty(n) / (faculty(x) * (faculty(n-x)))
    Pp = np.array(list(map(
        lambda v: combination_factor * (v ** x) * ((1 - v) ** (n - x)),
        P
        )))
    return Pp


def intersection(x, n, P, Pr):
    """
    Function to calculate intersection of obtaining this data with
    various hypothetical probabilities
    x = number of patients with severe side effects
    n = total number of patients obersverd
    P = 1D numpy.ndarray - with various hyptohetical probabilities
    Pr = Prior believs of P 1D numpy.ndarray
    """
    # Sanity Checks
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
    if not isinstance(Pr, np.ndarray) or P.shape != Pr.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    # needs to be adjusted with a filter
    pf = list(filter(lambda x: x < 0 or x > 1, P))
    if len(pf) > 0:
        raise ValueError(
            f"All values in P must be in the range [0, 1]"
            )
    prf = list(filter(lambda x: x < 0 or x > 1, P))
    if len(prf) > 0:
        raise ValueError(
            f"All values in P must be in the range [0, 1]"
            )
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")    # ----
    # Intersection = Likelihood * Prior
    ll = likelihood(x, n, P)
    inter = np.multiply(Pr, ll)
    return inter
