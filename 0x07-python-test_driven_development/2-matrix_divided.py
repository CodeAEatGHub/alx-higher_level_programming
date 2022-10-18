#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = matrix[:]
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    for k in new_matrix:
        for l in k:
            l = l / div
            print(l, end=' ')
    return (new_matrix)
    
