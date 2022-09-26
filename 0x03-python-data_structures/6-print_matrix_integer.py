#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for slst in lst:
            print('{:d}'.format(slst), end='')
            if slst != lst[-1]:
                print(end=' ')
        print()
