#!/usr/bin/env python3
"""slices a dataframe"""


def slice(df):
    """extract column High, Low, close and Volumne_(BTC)
    selects every 60th row from these columns"""
    df_sliced = df[['High', 'Low', 'Close', 'Volume_(BTC)']]
    return df_sliced[::60]