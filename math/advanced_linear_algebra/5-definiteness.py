#!/usr/bin/env python3
"""Function to return the cofadefinitness of a matrix"""

import numpy as np


def definiteness(matrix):
    """Function returns the definitness of a matrix"""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    shape = matrix.shape
    if 0 in shape:
        return None
    elif shape[0] != shape[1]:
        return None
    elif not np.allclose(matrix, matrix.T):
        return None
    eigvals = np.linalg.eigvalsh(matrix)
    # print(f"eigvals: {eigvals}")
    pos_def = False
    neg_def = False
    ind = False
    pos_sem = False
    neg_sem = False
    if 0 in eigvals:
        # print("has 0")
        for i in eigvals:
            if i > 0:
                pos_sem = True
                return "Positive semi-definite"
            elif i < 0:
                # print("is partially negative")
                neg_sem = True
        if pos_sem is True and neg_sem is False:
            return "Positive semi-definite"
        elif pos_sem is False and neg_sem is True:
            return "Negative semi-definite"
        elif pos_sem is True and neg_sem is True:
            return "Indefinite"
        else:
            return None
    else:
        for i in eigvals:
            if i > 0:
                pos_def = True
            if i < 0:
                neg_def = True
        # print(f"pos_def: {pos_def}, neg_def: {neg_def}")
        if pos_def is True and neg_def is False:
            return "Positive definite"
        elif neg_def is True and pos_def is False:
            return "Negative definite"
        elif pos_def is True and neg_def is True:
            return "Indefinite"
        else:
            return None
