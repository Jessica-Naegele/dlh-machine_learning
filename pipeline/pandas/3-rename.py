#!/usr/bin/env python3
"""function to rename column Timestamp to Datetime"""

import pandas as pd


def rename(df):
    """function renaming Timestamp to Datetime
    convert timestamp values to datemtimes
    only show datetime and close"""
    df_rename = df.rename(columns={"Timestamp": "Datetime"})  # rename the column
    df_rename['Datetime'] = pd.to_datetime(df_rename['Datetime'])  # datetime for Datetime
    return df_rename[['Datetime', "Close"]]
