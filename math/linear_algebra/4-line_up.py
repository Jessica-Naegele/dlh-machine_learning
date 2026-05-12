#!/usr/bin/env python3
"""This function adds two arrays elementwise when they have the same shape"""


def add_arrays(arr1, arr2):
    """Function to add two arrays element wise"""
    new_l = []
    if len(arr1) == len(arr2):
        for i in range(0, len(arr1)):
            new_l.append(arr1[i]+arr2[i])
        return new_l
    else:
        return None
