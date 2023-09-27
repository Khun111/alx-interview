#!/usr/bin/python3
'''Module for island perimeter task'''


def island_perimeter(grid):
    '''Island perimeter function'''
    perimeter = 0
    if not grid or len(grid) == 0:
        return
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
