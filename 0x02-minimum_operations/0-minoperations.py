#!/usr/bin/python3
""" Moudule """


def minOperations(n):
    """ Function """
    i = 2
    x = n
    res = 0
    while x > 1:
        while x % i != 0:
            i += 1
        res += i
        x /= i
        i = 2
    return res
