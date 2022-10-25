#!/usr/bin/python3
"""Triangle"""

def pascal_triangle(n):
    """Creates a triangle from a list of lists."""
    ls1 = []
    ls = []
    if (n <= 0):
        return ("")
    elif (n == 1):
        return ([1])
    elif (n == 2):
        return ([1], [1, 1])
    ls.append(1)
    ls.append([1, 1])
    print(ls)
    prev = []
    for i in range(2, n):
        prev = ls[i - 1]
        for j in range(i):
            if j == 0:
                ls1.append(1)
            if j == i:
                ls1.append(1)
            if j != 0 and j != i:
                print(len(prev))
        ls.append(ls1.copy())
    return (ls)
