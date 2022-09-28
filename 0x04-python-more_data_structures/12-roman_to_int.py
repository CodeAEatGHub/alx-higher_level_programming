#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_num = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    num = [1, 5, 10, 50, 100, 500, 1000]
    j = 0
    k = 0
    r = []
    if roman_string is None:
        return (0)
    for i in rom_num:
        if roman_string == i:
            r[k] =  num[j]
            k = k + 1
        j = j + 1
    for i in r:
        if i > r[j + 1]:
            op[j] = 1
        else:
            op[j] = 0
        j = j + 1
    for i in r:
        if op[j + 1] is 1
        sum = sum + 
    return (0)
