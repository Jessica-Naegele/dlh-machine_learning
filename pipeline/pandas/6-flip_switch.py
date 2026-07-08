#!/usr/bin/env python3
"""sort data in reverse chornological order and transposes sorted dataframe"""

import pandas as pd


def flip_switch(df):
    """transpose and sort a dataframe"""
    df_sorted = df.sort_values(by="Timestamp", ascending=False)
    return df_sorted.T
