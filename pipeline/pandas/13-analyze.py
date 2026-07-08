#!/usr/bin/env python3
"""function describing """


def analyze(df):
    """descripte statistics for all columns except Timestamp"""
    return df.drop(columns=["Timestamp"]).describe()
