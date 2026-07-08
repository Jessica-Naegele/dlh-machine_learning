#!/usr/bin/env python3
"""sorts high price in  descending order"""


def high(df):
    """I forgot to document this -.-"""
    return df.sort_values(by="High", ascending=False)
