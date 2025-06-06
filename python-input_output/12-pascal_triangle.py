#!/usr/bin/python3
"""
This Module is an algorithm to reproduct Pascal triangle
"""


def pascal_triangle(n):
    """
    Function that return a list of Pascal's triangle
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        line = [1]
        for j in range(i):
            if j + 1 < i:
                line.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        line.append(1)
        triangle.append(line)
    return triangle
