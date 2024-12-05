#!/usr/bin/python3
""" Moudule """


def island_perimeter(grid):
    """island_perimeter"""
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                for k in range(len(dx)):
                    ind1 = i + dx[k]
                    ind2 = j + dy[k]
                    if (ind1 < len(grid) and ind1 >= 0 and ind2 < len(grid[i])
                       and ind2 >= 0 and grid[ind1][ind2] == 0):
                        res += 1
    return res
