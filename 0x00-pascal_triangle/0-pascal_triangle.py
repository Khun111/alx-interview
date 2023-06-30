#!/usr/bin/python3
'''Module for Pascal triangle'''
def pascal_triangle(n):
    '''Function that returns pascal_triangle'''
    triangle = []
    for row in range(n):
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                previous_row = triangle[row - 1]
                current_row.append(previous_row[col - 1] + previous_row[col])
        triangle.append(current_row)
    return (triangle)
