#!/usr/bin/python3
"""rectangle module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    __width__ = 0
    __height__ = 0

    def __init__(self, width, height):
        """Initializes new instances."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width__ = width
        self.__height__ = height

    def area(self):
        """Returns the area of the square."""
        return (self.__width__ * self.__height__)

    def __str__(self):
        """Returns the string representation of the instances."""
        if self.__width__ and self.__height__:
            return f"[Rectangle] {self.__width__}/{self.__height__}"
        elif self.__size__ and not self.__height__:
            return f"[Rectangle] {self.__size__}/{self.__size__}"
        elif not self.__width__ and self.__size__:
            return f"[Rectangle] {self.__size__}/{self.__size__}"
