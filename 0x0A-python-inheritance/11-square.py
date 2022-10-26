#!/usr/bin/python3
"""Square Geometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    __size = 0

    def __init__(self, size):
        """Initializes new instances."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of a square."""
        return (self.__size * self.__size)

    def __str__(self):
        """Returns a string representation of class."""
        return f"[Square] {self.__size}/{self.__size}"
