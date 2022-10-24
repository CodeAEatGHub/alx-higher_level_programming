#!/usr/bin/python3
"""Sorted print module"""


class MyList(list):
    def print_sorted(self):
        p = self.copy()
        p.sort()
        print(p)

