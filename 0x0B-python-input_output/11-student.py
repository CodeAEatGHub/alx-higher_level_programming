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
        ls_t = self.__dict__
        if attrs:
            for i in attrs:
                if i in l:
                    lst[i] = ls_t[i]
            return (lst)
        else:
            return (ls_t)

    def reload_from_json(self, json):
        """Replaces all attributes of the student instance."""
        ls = dict()
        ls = self.__dict__
        for i in json.keys():
            ls[i] = json[i]
