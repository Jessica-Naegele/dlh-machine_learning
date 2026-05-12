#!/usr/bin/env python3

matrix_transpose = __import__('3-flip_me_over').matrix_transpose

mat1 = [[1, 2], [3, 4]]
print(mat1)
print(matrix_transpose(mat1))
mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
print(mat2)
print(matrix_transpose(mat2))


"""
print("--- test mat 2")
"""
"""    current_layer = matrix
    while isinstance(current_layer, list):
        size.append(len(current_layer))
        current_layer = current_layer[0]"""
"""size = []
current_layer = mat1
while isinstance(current_layer, list):
    size.append(len(current_layer))
    current_layer = current_layer[0]
print(size)

print("---") 

transpose = []
if len(size) == 2:
    
    for i in range(0, size[1]):
        r = []
        for row in mat2:
           # print(row[i])
           r.append(row[i])
        transpose.append(r)

print(transpose)
"""

"""

size = []
current_layer = mat2
while isinstance(current_layer, list):
    size.append(len(current_layer))
    current_layer = current_layer[0]
print(size)

print("---") 

transpose = []
if len(size) == 2:
    
    for i in range(0, size[1]):
        r = []
        for row in mat2:
           # print(row[i])
           r.append(row[i])
        transpose.append(r)
else:
    l = len(size)
    # column
    for i in range(0, size(l-1)): 
        for 

print(transpose)

"""