#!/usr/bin/python3
""" Moudule """


def rotate_2d_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    a = 0
    x = []
    for i in range(n):
        y = []
        for j in range(m):
            y.append(0)
        x.append(y)
    for i in range(m):
        b = 0
        for j in range(n-1, -1, -1):
            x[a][b] = matrix[j][i]
            b += 1
        a += 1
    matrix.clear()
    matrix.extend(x)
