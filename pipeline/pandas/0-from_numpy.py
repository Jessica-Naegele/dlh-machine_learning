#!/usr/bin/env python3
""" function creating a data from from a np ndarray"""

import numpy as np
import pandas as pd 


def from_numpy(array):
    """Create a dataframe from a np ndarray
    DataFrame is a two-dimensional data structure by passing a
    dictionary keys = column labels and values = column values
    """
    s = array.shape
    # print(f"s: {s}") #helper #A s = 5,8 --> 5 rows 8 columns
    r_in = s[0]
    c_in = s[1]
    # print(f"r_in: {r_in}, c_in: {c_in}") #helper
    c_range = list(chr(65 + i) for i in range(c_in)) 
    r_range = np.arange(0, r_in)
    # print(f"c_range: {c_range}") #helper
    # print(f"r_range: {r_range}") #helper

    df = pd.DataFrame(array, index=np.arange(0, r_in), columns=c_range)
    return df


