#!/usr/bin/env python3
"""Class that represents a Multivariate Normal distribution"""

import numpy as np


class MultiNormal():
    """Class representing a Multivariate Normal Distribution"""

    def __init__(self, data):
        """Initiate the class
        data is a numpy.ndarray of shape (d, n)
        as mean and cov are public instance variable,
        they all need to be set in __init__
        """
        if not isinstance(data, np.ndarray) or len(np.shape(data)) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        # check on n (data.shape(1))
        elif data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")
        else:
            self.data = data

        # set mean
        self.mean = np.mean(data, axis=1, keepdims=True)

        # set cov (does it work the same way?)
        # Step 1 create a centered matrix
        DataC = data - self.mean
        # Step 2 Multiplication (d, n) - (d, n)
        # * (n, d)) (result should be d, d)
        self.cov = (
            (np.matmul(DataC, np.matrix.transpose(DataC)))
            / (data.shape[1] - 1)
        )
