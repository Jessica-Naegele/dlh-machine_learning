#!/usr/bin/env python3

if __name__ == '__main__':
    import numpy as np
    mean_cov = __import__('0-mean_cov').mean_cov

    np.random.seed(0)
    X = np.random.multivariate_normal([12, 30, 10], [[36, -30, 15], [-30, 100, -20], [15, -20, 25]], 10000)
    print(np.shape(X))
    print(type(X))
    mean, cov = mean_cov(X)
    print(mean)
    print(cov)

    """
    print("____")
    X = np.ndarray([0,2,3])
    print(np.shape(X))
    print(type(X))
    mean, cov = mean_cov(X)
    print(mean)
    print(cov)
    """

    print("____")
    X = np.ndarray([[0,2,3], [1,2,3]])
    print(np.shape(X))
    print(type(X))
    mean, cov = mean_cov(X)
    print(mean)
    print(cov)


    
    print("____")
    X = np.ndarray([[0,2,3], [1,2,3], [4,5,6]])
    print(np.shape(X))
    print(type(X))
    mean, cov = mean_cov(X)
    print(mean)
    print(cov)