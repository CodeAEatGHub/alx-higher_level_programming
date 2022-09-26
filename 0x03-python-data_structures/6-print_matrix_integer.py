#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        for sl in l:
            print('{:d}'.format(sl), end='')
            if sl != l[-1]:
                print(end=' ')
        print()
