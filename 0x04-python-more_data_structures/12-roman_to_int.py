#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return (0)
    rom_num = [I, V, X, L, C, D, M]
    num = [1, 5, 10, 50, 100, 500, 1000]
    j = 0
    for i in rom_num:
        if roman_string == i:
            return num[j]
        j = j + 1
    return (0)
