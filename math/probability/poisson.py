#!/usr/bin/env python3
"""Create class to calculate Poisson distribution

data is a list of the data to be used to estimate the distribution
lambtha is the expected number of occurences in a given time frame
Sets the instance attribute lambtha
Saves lambtha as a float
If data is not given, (i.e. None (be careful:
not data has not the same result as data is None)):
Use the given lambtha
If lambtha is not a positive value or equals to 0,
raise a ValueError with the message lambtha must be a positive value
If data is given:
Calculate the lambtha of data
"""


class Poisson():
    """Calculates Poisson distribution"""

    def __init__(self, data=None, lambtha=1):
        """initialisation with default values"""
        self._data = None
        self._lambtha = 1.0

        self.data = data
        self.lambtha = lambtha

    # getter data
    @property
    def data(self):
        return self._data

    # setter: data is a list of the data to be used to estimate
    # the distribution
    @data.setter
    def data(self, data):
        """
        If data is not a list, raise a TypeError with the message
        data must be a list
        If data does not contain at least two data points, raise a
        ValueError with the message data must contain multiple values
        """
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self._data = data

    # getter lambtha
    @property
    def lambtha(self):
        lambtha = self._lambtha
        return lambtha

    # setter lambtha
    @lambtha.setter
    def lambtha(self, lambtha):
        """
        lambtha is the expected number of occurences in a given time frame
        Sets the instance attribute lambtha
        Saves lambtha as a float
        If data is not given,
        (i.e. None (be careful: not data has not the same result as
        data is None)):
        Use the given lambtha
        If lambtha is not a positive value or equals to 0, raise a ValueError
        with the message lambtha must be a positive value
        """
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        elif self._data is None:
            self._lambtha = lambtha
        else:
            # Lambtha : sample arithmetic mean.
            su = sum(self._data)
            le = len(self._data)
            lambtha = su / le
            self._lambtha = lambtha

    # instance method: pmf - Probability Mass Function
    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of "successes"
        k is the number of "successes"
        If k is not an integer, convert it to an integer
        If k is out of range, return 0
        Returns the PMF value for k
        P(X=k)= (λ^k * e ^(-λ))/k!
        e = 2.7182818285
        """
        e = 2.7182818285
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        prod_k = 1
        h_k = k
        while h_k > 0:
            prod_k = prod_k * h_k
            h_k += -1
        pmf = ((self._lambtha ** k) * (e ** (-self.lambtha))) / prod_k
        return pmf
