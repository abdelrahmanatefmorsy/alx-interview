#!/usr/bin/python3
""" Moudule """


def pascal_triangle(n):
    """ Function """
    lst = []

    if (n <= 0):
        return lst

    lst.append([1])

    for i in range(1, n):
        tmp = []
        for j in range(i + 1):
            sum = 0
            if (j < len(lst[i - 1])):
                sum += lst[i-1][j]
            if (j - 1 >= 0):
                sum += lst[i - 1][j - 1]
            tmp.append(sum)
        lst.append(tmp)
    return lst
