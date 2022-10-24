#!/usr/bin/python3
"""MyInt module"""


class MyInt(int):
    """MyInt class"""
    __value__ = 0
    def __init__(self, value):
        """Initializes new instances."""
        self.__value__ = value

