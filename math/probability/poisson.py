#!/usr/bin/env python3
"""Create class to calculate Poisson distribution

data is a list of the data to be used to estimate the distribution
lambtha is the expected number of occurences in a given time frame
Sets the instance attribute lambtha
Saves lambtha as a float
If data is not given, (i.e. None (be careful: not data has not the same result as data is None)):
Use the given lambtha
If lambtha is not a positive value or equals to 0, raise a ValueError with the message lambtha must be a positive value
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

    # setter: data is a list of the data to be used to estimate the distribution
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
            return lambtha
        else:
            # Lambtha : sample arithmetic mean.
            s = sum(self._data)
            l = len(self._data)
            lambtha = s / l
            self._lambtha = lambtha
