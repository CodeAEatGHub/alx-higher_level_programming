#!/usr/bin/python3
def best_score(a_dictionary):
    b = 0
    biggest = ""
    if a_dictionary == None:
        return None
    for i in list(a_dictionary):
        if a_dictionary[i] >= b:
            b = a_dictionary[i]
            biggest = i
    return biggest
