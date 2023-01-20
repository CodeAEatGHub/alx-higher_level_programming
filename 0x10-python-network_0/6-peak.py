#!/usr/bin/python3
"""
Peak Module
"""


def divide(array, start, end):
    """divide function"""

    x = int((start + end)/2)
    if array[x-1] <= array[x] >= array[x+1]:
        return array[x]
    elif array[x] > array[x+1]:
        return divide(array, end, x-1)
    elif array[x] < array[x+1]:
        return divide(array, x+1, start)
    
    def find_peak(list_of_integers):
    """Find peak of a list"""
    if not list_of_integers:
        return None
    return divide(list_of_integers, 0, len(list_of_integers)-1)
