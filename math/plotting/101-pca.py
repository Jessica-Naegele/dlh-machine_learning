#!/usr/bin/env python3
"""Create a iris flower data set with PCA"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

lib = np.load("pca.npz")  #iris data 
data = lib["data"]  # x achsis
labels = lib["labels"] # y achis?

data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)

# your code here

#data = np.ndarray(150, 4)
# 150 => number of flower
# 4 => petal length, petal width, sepal length, sepal width
#labels = np.ndarray(150,)
# 0 => iris setosa
# 1 => Iris Versicolor
# 2 => Iris virginica
#pca_data = np.ndarray (150, 3)
#  represent the 3 dimensions of the reduced data, i.e., x, y, and z, respectively
# The x, y, and z axes should be labeled U1, U2, and U3, respectively
# x = pca_data [:,0] first column
# y = pca_data[:,1] second column
# z = pca_data [:,2] third column
# The data points should be colored based on their labels using the plasma color map

fig = plt.figure(figsize=(6.4, 4.8))  #?
ax = fig.add_subplot(projection='3d')
ax.scatter(pca_data[:,0], pca_data[:,1], pca_data[:,2], c=labels, cmap='plasma' )
ax.set_title("PCA of Iris Dataset")
ax.set_xlabel('U1')
ax.set_ylabel('U2')
ax.set_zlabel('U3')

plt.show()