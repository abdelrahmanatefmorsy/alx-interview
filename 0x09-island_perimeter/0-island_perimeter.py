#!/usr/bin/python3
""" Moudule """


def island_perimeter(grid):
    res = 0
    h = 0
    w = 0
    for i in range(len(grid)):
        tmp2 = 0
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                ind = i
                tmp = 0
                tmp2 += 1
                while (ind < len(grid) and grid[ind][j] == 1):
                    ind += 1
                    tmp += 1
                h = max(h, tmp)
        w = max(w, tmp2)
    return ((w + h) * 2)
