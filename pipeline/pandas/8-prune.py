#!/usr/bin/env python3
"""function removing NaN in Close"""


def prune(df):
    """remove all nan values in Close"""
    return df.dropna()
