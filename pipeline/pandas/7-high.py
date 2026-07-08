#!/usr/bin/env python3
"""sorts high price in  descending order"""


def high(df):
    return df.sort_values(by="High", ascending=False)
