#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    j = 0
    new = matrix.copy()
    for i in new:
        new[j] = list(map(lambda x: x ** 2, i))
        j = j + 1
    return new
