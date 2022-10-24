#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    __width__ = 0
    __height__ = 0
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width__ = width
        self.__height__ = height
    def area(self):
        return (self.__width__ * self.__height__)
    def __str__(self):
        return ("[Rectangle] self.__width__/self.__height__")

