#!/usr/bin/python3
""" Moudule """


def island_perimeter(grid):
    x1 = 1000
    y1 = 1000
    x2 = 0
    y2 = 0    
    for i in range(len(grid)):
        tmp2 = 0
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                x1 = min(x1,i)
                y1 = min(y1,j)
                x2 = max(x2,i)
                y2 = max(y2,j)
    h = x2 - x1 + 1
    w = y2 - y1  + 1
    return ((w + h) * 2)
