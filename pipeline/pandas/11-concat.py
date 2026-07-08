#!/usr/bin/env python3
"""concatinating two dataframes"""

import pandas as pd


def concat(df1, df2):
    """
    x indexes both dataframes on their Timestamp columns.
    Includes all timestamps from df2 (bitstamp) up to and including
    timestamp 1417411920.
    Concatenates the selected rows from df2 to the top of df1 (coinbase).
    Adds keys to the concatenated data, labeling the rows from df2 as
    bitstamp and the rows from df1 as coinbase.
    x You should use index = __import__('10-index').index
    Returns the concatenated pd.DataFrame.
    """
    index = __import__('10-index').index
    df1_in = index(df1)
    df2_in = index(df2)
    df2_inq = df2_in.loc[:1417411920]
    return pd.concat([df2_inq, df1_in], keys=['bitstamp', 'coinbase'])
