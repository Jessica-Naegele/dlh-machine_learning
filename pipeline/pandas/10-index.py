#!/usr/bin/env python3
"""Sets the timestamp column as index of dataframe"""


def index(df):
    """sets column timestamp as index"""
    return df.set_index('Timestamp')
