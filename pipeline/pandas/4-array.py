#!/usr/bin/env python3
"""function that selects last 10 rows and ocnverst the selected
values in a numpy value"""

import pandas as pd


def array(df):
    """function
    - selecting last 10 rows of High and Close
    Convert them into a numpy ndarray"""
    df_select = df[['High', 'Close']].tail(10)
    return df_select.to_numpy()
