#!/usr/bin/env python3
""" function creating a data from from a np ndarray"""

import pandas as pd


def from_numpy(array):
    """Create a dataframe from a np ndarray
    DataFrame is a two-dimensional data structure by passing a
    dictionary keys = column labels and values = column values
    """
    s = array.shape
    r_in = s[0]
    c_in = s[1]
    c_range = list(chr(65 + i) for i in range(c_in))
    r_range = list(range(r_in))

    df = pd.DataFrame(array, index=r_range, columns=c_range)
    return df
