#!/usr/bin/env python3
""" representing a normal distritubion"""


class Normal:
    """
    Class representing a normal distribution
    """

    def __init__(self, data=None, mean=0., stddev=1):
        """
        Class contructor def __init__(self, data=None, mean=0., stddev=1.):
        data is a list of the data to be used to estimate the distribution
        mean is the mean of the distribution
        stddev is the standard deviation of the distribution
        """
        self._data = None
        self._mean = 0.0
        self._stddev = 1.0

        self.data = data
        self.mean = mean
        self.stddev = stddev

    # getter data
    @property
    def data(self):
        """list of data to be used to estimate the distribution"""
        return self._data

    # getter mean
    @property
    def mean(self):
        """mean of the distribution"""
        return self._mean

    # getter stddev
    @property
    def stddev(self):
        """standard deviation"""
        return self._stddev

    # data setter
    @data.setter
    def data(self, data):
        """If data is given:
        Calculate the mean and standard deviation of data
        If data is not a list, raise a TypeError with the
        message data must be a list
        If data does not contain at least two data points,
        raise a ValueError with the message data must contain
        multiple values
        """
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data muts be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self._data = data

    # mean setter
    @mean.setter
    def mean(self, mean):
        """
        Saves mean and stddev as floats
        Calculate the mean and standard deviation of data
        If data is not given (i.e. None (be careful: not data
        has not the same result as data is None))
        Use the given mean and stddev
        """
        if self._data is None:
            self._mean = float(mean)
        else:
            self._mean = float(sum(self.data) / len(self.data))

    # stddev setter
    @stddev.setter
    def stddev(self, stddev):
        """
        If stddev is not a positive value or equals to 0,
        raise a ValueError with the message stddev
        must be a positive value
        """
        if self._data is None:
            self._stddev = float(stddev)
        else:
            if stddev < 0:
                raise ValueError("stddev must be a positive value")
            # calculate the variance
            mn = self._mean
            h_var = 0
            for i in self._data:
                h_var += (i - mn) ** 2  # sum of difference btw data and mn
            var = h_var / len(self._data)
            self._stddev = var ** 0.5
