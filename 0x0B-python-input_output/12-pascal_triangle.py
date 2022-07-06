#!/usr/bin/python3
""" Defines pascal's triangle """


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n

    args:
        n (int)
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) != n:
        temp = [1]
        pascal = triangle[-1]

        for i in range(len(pascal) - 1):
            temp.append(pascal[i] + pascal[i + 1])

        temp.append(1)
        triangle.append(temp)

    return triangle
