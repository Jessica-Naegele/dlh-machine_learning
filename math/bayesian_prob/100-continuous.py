#!/usr/bin/env python3#!/usr/bin/env python3
"""
calculating the marginal probability
"""

from scipy import special


def posterior(x, n, p1, p2):
    """
    function calculating the posterior -> aka the baysian probability
    x number of patients with side effect
    n total number of patients observed
    p1  is lower bound of the range
    p2 is the upper bound on the range
    p = prior belief follow a uniform distribution
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
    if not isinstance(p1, float) or (p1 <= 0 or p1 >= 1):
        raise ValueError("p1 must be a float in the range [0, 1]")
    if not isinstance(p2, float) or (p2 <= 0 or p2 >= 1):
        raise ValueError("p1 must be a float in the range [0, 1]")
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")
    # needs to be adjusted with a filter
    # Baysian probability - posterior probability
    # P(H|E) = P(E|H)*P(H) / P(E)
    # Posterior = Likelihood * Prior Probability / Evidence
    # (Marginal Likelihood) = evidence
    # return: posterior probability p within range [p1, p2] given x and n
    # p follows uniform distritubion
    # uniform prior means aphla = beta = 1
    area = (
        special.betainc(x + 1, n - x + 1, p2)
        - special.betainc(x + 1, n - x + 1, p1)
    )
    return area
