#!/usr/bin/env python3
""" represents a binomial distritubion"""


class Binomial:
    """class representing a binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """initializing binomial distribution"""
        self._data = None
        self._n = 1  # int
        self._p = 0.5  # float

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
        if p <= 0 or p >= 1:
            raise ValueError("p must be greater than 0 and less than 1")
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

    # instant methode pmf - probability mass function
    def pmf(self, k):
        """Calculates the value for agiven number of success
        k = number of successes
        pmf = n! /(x!(n-x)!) * p ^x (1-p)^(n-x)
        """
        n = self._n
        p = self._p
        if not isinstance(k, int):
            k = int(k)
        if k < 0 or k > n:
            return 0
        else:
            prod_x = 1
            for i in range(1, n + 1):
                prod_x = prod_x * i
            prod_k = 1
            for j in range(1, k + 1):
                prod_k = prod_k * j
            prod_diff = 1
            for m in range(1, (n - k) + 1):
                prod_diff = prod_diff * m

            pmf = (prod_x / (prod_k*prod_diff)) * p ** k * (1 - p) ** (n - k)
            return pmf
