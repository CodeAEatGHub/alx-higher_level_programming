#!/usr/bin/python3
"""Triangle"""


def pascal_triangle(n):
    """Creates a triangle from a list of lists."""
    ls1 = []
    ls = []
    prev = []
    if (n <= 0):
        return ("")
    elif (n == 1):
        return ([1])
    elif (n == 2):
        return ([1], [1, 1])
    ls.append([1])
    prev = ls.append([1, 1])
    for i in range(2, n):
        prev = ls[i - 1]
        for j in range(i + 1):
            if j == 0:
                ls1.append(1)
            if j == i:
                ls1.append(1)
            if j != 0 and j != i:
                ls1.append(prev[j] + prev[j - 1])
        ls.append(ls1.copy())
        ls1 = []
    return (ls)
