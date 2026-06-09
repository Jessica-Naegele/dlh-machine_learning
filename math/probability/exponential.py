#!/usr/bin/env python3
"""Class representing an exponential distribution"""


class Exponential():
    """data is a list of the data to be used to estimate the distribution
        lambtha is the expected number of occurences in a given time frame
        Sets the instance attribute lambtha
        If data is not given (i.e. None):
        Use the given lambtha
        If lambtha is not a positive value, raise a ValueError with the message
        lambtha must be a positive value
        If data is given:
        Calculate the lambtha of data
        """

    def __init__(self, data=None, lambtha=1):
        """Initialization of a data and none"""
        self._data = None
        self._lambtha = 1.0

        self.data = data
        self.lambtha = lambtha

    # getter lambtha
    @property
    def lambtha(self):
        """gets lambhta as float
        Saves lambtha as a float"""
        return float(self._lambtha)

    # getter data
    @property
    def data(self):
        """gets data"""
        return self._data

    # setter data
    @data.setter
    def data(self, data):
        """
        If data is not a list, raise a TypeError with the message data must
        be a list
        If data does not contain at least two data points, raise a ValueError
        with the message data must contain multiple values
        """
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self._data = data

    # setter lambtha
    @lambtha.setter
    def lambtha(self, lambtha):
        """lambtha is the expected number of occurences in a
        given time frame"""
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        elif self._data is None:
            self._lambtha = lambtha
        else:
            # calculate lambda
            # calculate mean of data
            mean = sum(self._data) / len(self._data)
            # 1/ mean = lambda
            self._lambtha = 1 / mean
