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

    def pdf(self, x):
        """public instance method to calculate PDF at a data point
        x = numpy ndarray (d, 1) containing data point whose PDF
        should be calculated
        d = number of dimenions of this Multnomial instance
        """
        # check x
        # print(f"x: {x}") #helper
        # print(f"shape(x): {x.shape}") #helper
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.mean.shape[0]
        n = x.shape[1]
        if len(x.shape) != 2 or x.shape[1] != 1 or x.shape[0] != d:
            raise ValueError(f"x must have the shape ({d}, 1)")

        # print(f"d: {d}, n: {n}") #helper
        cov_x = self.cov
        mean_x = self.mean
        # print(f"cov: {cov_x}")
        # print(f"mean: {mean_x}")
        # calculate pdf
        # f(x) = sqrt(1/(2pi)**dimenion * determinante(cov))
        # * (-1/2 * dotprod (x-mean *inverse(cov)* diff))
        dif = x - mean_x
        # print(f"dif: {dif}") #helper
        # print(f"dif.shape {dif.shape}") #helüer
        norm = 1.0 / (
            np.sqrt((2 * np.pi) ** d * np.linalg.det(cov_x))
        )
        exp = (
            np.exp(-0.5 * np.dot
                   (np.dot(dif.T, np.linalg.inv(cov_x)), dif).item()
                   ))
        return norm * exp
