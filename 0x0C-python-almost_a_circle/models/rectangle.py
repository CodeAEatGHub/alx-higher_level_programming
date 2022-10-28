#!/usr/bin/python3
"""Base Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    __nb_objects = 0
    __width = 0
    __height = 0
    __x = 0
    __y = 0
    id = 0


    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes new instances."""
        self.__width = width
        self.__height = height
        if type(id) not in [int, float]:
            raise TypeError("id must be an integer")
        if id < 0:
            raise ValueError("id must be > 0")
        Base.__init__(self, id)
        self.x(x)
        self.y(y)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) not in [int, float]:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """Width setter"""
        if type(height) not in [int, float]:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """X setter"""
        if type(x) not in [int, float]:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @property
    def y(self):
        """Y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """Y getter"""
        if type(y) not in [int, float]:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")
        self.__y = y
