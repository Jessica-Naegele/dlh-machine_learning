#!/usr/bin/env python3
"""creting a function that calculates the mean and covariance of a data set"""

import numpy as np


def mean_cov(X):
    """Function that calculates the mean and covariance ofdata set
    X is a numpy.ndarray with shape (n, d)
    n = number of data points
    d = number of dimension in each data point
    """
    # if X is not a 2D numpy.ndarray raise Typerror
    if not isinstance(X, np.ndarray) or len(np.shape(X)) != 2:
        print(type(X))
        print(len(X))
        raise TypeError("X must be a 2D numpy.ndarray")
    n = X.shape[0]
    d = X.shape[1]

    # print(f"n: {n}")  # helper
    # print(f"d: {d}")  # helper 

    # if n is less than 2
    if n < 2:
        raise ValueError("X must contain multiple data points")
    # mean = numpy.ndarray of shape (1, d)
    mean = np.mean(X, axis=0, keepdims=True)
    # print(f"mean: {mean}") #helper

    # covariance numpy.ndarray with shape (d,d)
    # np C o Variance functionality is not to be used
    # Step 1 create a centered matrix
    Xc = X - mean
    # Step 2 Multiplication (d,n) * (n,d)
    cov = (np.matmul(np.matrix.transpose(Xc), Xc)) / (n - 1)
    # print(f"cov: {cov}") # ehlper
    # print(cov.shape)

    return (mean, cov)
