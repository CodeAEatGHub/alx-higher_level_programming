#!/usr/bin/python3
"""rectangle module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    __width = 0
    __height = 0

    def __init__(self, width, height):
        """Initializes new instances."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the square."""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns the string representation of the instances."""
        if self.__width and self.__height:
            return f"[Rectangle] {self.__width}/{self.__height}"
        elif self.__size and not self.__height:
            return f"[Rectangle] {self.__size}/{self.__size}"
        elif not self.__width and self.__size:
            return f"[Rectangle] {self.__size}/{self.__size}"
