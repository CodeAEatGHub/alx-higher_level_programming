#!/usr/bin/python3
"""Sorted print module"""


import doctest


class MyList(list):
    def print_sorted(self):
        p = self.copy()
        p.sort()
        print(p)


doctest.testfile("tests/1-my_list.txt")
