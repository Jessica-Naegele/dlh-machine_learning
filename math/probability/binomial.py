#!/usr/bin/env python3
""" represents a binomial distritubion"""


class Binomial:
    """class representing a binomial distribution
    Class contructor def __init__(self, data=None, n=1, p=0.5):
    data is a list of the data to be used to estimate the 
    distribution
    n is the number of Bernoulli trials
    p is the probability of a "success"
    Sets the instance attributes n and p
    Saves n as an integer and p as a float
    If data is not given (i.e. None)
    Use the given n and p
    If n is not a positive value, raise a ValueError with the message n
    must be a positive value
    If p is not a valid probability, raise a ValueError with the message
    p must be greater than 0 and less than 1
    If data is given:
    Calculate n and p from data
    Round n to the nearest integer (rounded, not casting! The difference
    is important: int(3.7) is not the same as round(3.7))
    Hint 1: Calculate p first and then calculate n. Then recalculate p.
    Think about why you would want to do it this way?
    Hint 2: Method of Moments
    If data is not a list, raise a TypeError with the message data must
    be a list
    If data does not contain at least two data points, raise a ValueError
    with the message data must contain multiple values    
    """

    def __init__(self, data=None, n=1, p=0.5):
        """initializing binomial distribution"""
        self._data = None
        self._n = 1  # int
        self._p = 0.5  #float

        if data is not None:
            self.data = data
        else:
            self.n = n
            self.p = p

    # getter data
    @property
    def data(self):
        """data"""
        return self._data

    # getter n
    @property
    def n(self):
        """n"""
        return self._n

    # getter p
    @property
    def p(self):
        """p"""
        return self._p

    # setter data
    @data.setter
    def data(self, data):
        """if data is given"""
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
        self._data = data

        mn = sum(data) / len(data)
        var = sum((x - mn) ** 2 for x in data) / len(data)

        calculated_p = 1.0 - (var / mn)

        self._n = int(round(mn / calculated_p))
        self._p = float(mn / self._n)

    # setter p
    @p.setter
    def p(self, p):
        """ calculate p
        p = probabilzx of success
        p = 1 - sigma^2/mean
        """
        d = self._data
        if p < 0 or p > 1:
            raise ValueError("p must be a greater than 0 and less than 1")
        self._p = float(p)

    # setter n 
    @n.setter
    def n(self, n):
        """integer
        n = number of Bernoulli trails
        n = mean / p
        """
        # print("n setter")
        # print(f"data: {self._data}")
        if n <= 0:
            raise ValueError("n must be a positive value")
        self._n = int(n)
