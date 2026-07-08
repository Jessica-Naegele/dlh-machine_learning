#!/usr/bin/env python3
"""function to change hierarchy"""

import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """
    Rearranges the MultiIndex so that Timestamp is the first level.
    Concatenates the bitstamp and coinbase tables from timestamps 1417411980 to 1417417980, inclusive.
    Adds keys to the data, labeling rows from df2 as bitstamp and rows from df1 as coinbase.
    Ensures the data is displayed in chronological order.
    Returns: the concatenated pd.DataFrame.
    """
    df1_in = index(df1)
    df2_in = index(df2)
    df1_inq = df1_in.loc[1417411980:1417417980]
    df2_inq = df2_in.loc[1417411980:1417417980]
    con_df = pd.concat([df2_inq, df1_inq], keys=['bitstamp', 'coinbase'])
    return con_df.swaplevel(0, 1).sort_index()
