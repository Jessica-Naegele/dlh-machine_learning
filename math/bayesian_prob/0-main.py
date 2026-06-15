#!/usr/bin/env python3

if __name__ == '__main__':
    import numpy as np
    likelihood = __import__('0-likelihood').likelihood

    P = np.linspace(0, 1, 11) # [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    # print(type(P))
    
    # print(f"likelihood(26, 130, {P})")

    print(likelihood(26, 130, P))
    """
    print("--- negative n")

    print(likelihood(26, -130, P))
    """
    """
    print("--- negative 0")

    print(likelihood(26, 0, P))
    """
    
    print("--- negative 0")

    print(likelihood(26, 'test', P))


