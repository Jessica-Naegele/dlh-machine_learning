#!/usr/bin/env python3
"""loading data from a file"""

import pandas as pd


def from_file(filename, delimiter):
    """function to upload data from a file as a pd.DataFrame"""

    df = pd.read_csv(filename, sep=delimiter)
    return df
