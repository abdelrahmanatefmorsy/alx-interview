#!/usr/bin/python3
""" Moudule """


def isWinner(x, nums):
    """who is the winner"""
    lst = list(range(10001))
    for i in range(1, len(lst)):
        if i == 1:
            lst[i] = 0
            continue
        j = 2
        lst[i] = 1
        while (j * j <= i):
            if (i % j == 0):
                lst[i] = 0
                break
            j += 1
    for i in range(1, len(lst)):
        lst[i] += lst[i-1]
    a = 0
    b = 0
    for i in range(x):
        if (lst[i] % 2 == 0):
            a += 1
        else:
            b += 1
    if a > b:
        return "Ben"
    elif b > a:
        return "Maria"
    else:
        return None
