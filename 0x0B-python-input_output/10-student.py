#!/usr/bin/python3
"""JSON module"""


class Student:
    """Student class"""
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """Initializes new student instances."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of an instance."""
        lst = dict()
        ls = self.__dict__
        if attrs:
            for i in attrs:
                if i in ls:
                    lst[i] = ls[i]
            return (lst)
        else:
            return (ls)
