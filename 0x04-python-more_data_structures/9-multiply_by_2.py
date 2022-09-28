#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for i in list(a_dictionary):
        new[i] = a_dictionary[i]
    for i in list(new):
        new[i] = 2 * new[i]
    return new
