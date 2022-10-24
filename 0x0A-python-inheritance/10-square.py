#!/usr/bin/python3
"""Square Geometry"""


Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """Square class"""
    __side__ = 0
    def __init__(self, size):
        """Initializes new instances."""
        self.integer_validator("size", size)
        self.__size__ = size
    def area(self):
        """Returns the area of a square."""
        return (self.__size__ * self.__size__)
