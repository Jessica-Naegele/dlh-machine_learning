#!/usr/bin/env python3

matrix_shape = __import__('2-size_me_please').matrix_shape

mat1 = [[1, 2], [3, 4]]
print(matrix_shape(mat1))
mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
print(matrix_shape(mat2))
mat3 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]],
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]]
print(matrix_shape(mat3))


#print(len(mat1))
#print(len(mat2))


# A 2x1x1x2x2 matrix
test_matrix_5d = [
    [ # Level 1: First "block"
        [ # Level 2
            [ # Level 3
                [[10, 11], [12, 13]] # Level 4 & 5: A 2x2 matrix
            ]
        ]
    ],
    [ # Level 1: Second "block"
        [ 
            [ 
                [[20, 21], [22, 23]] 
            ]
        ]
    ]
]
print(matrix_shape(test_matrix_5d))
print(len(matrix_shape(test_matrix_5d)))
testerli = matrix_shape(test_matrix_5d)
print(testerli[len(testerli)-1])