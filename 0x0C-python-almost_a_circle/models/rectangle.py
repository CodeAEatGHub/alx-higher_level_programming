#!/usr/bin/python3
"""Base Rectangle"""


from models.base import Base
import sys


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
        if type(width) not in [int]:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) not in [int]:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) not in [int]:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) not in [int]:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        if id is not None and type(id) is not int:
            raise TypeError("id must be an integer")
        if id is not None and id < 0:
            raise ValueError("id must be > 0")
        Base.__init__(self, id)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) not in [int]:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """Width setter"""
        if type(height) not in [int]:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """X setter"""
        if type(x) not in [int]:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """Y getter"""
        if type(y) not in [int]:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of the rectangle."""
        return (self.__width * self.__height)

    def display(self):
        """Displays the rectangle using # characters."""
        for i in range(0, self.__y):
            print()
        for j in range(0, self.__height):
            for k in range(0, self.__x):
                print(" ", end="")
            for wd in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Prints the string representation of the class."""
        return (f'[{Rectangle.__name__}] ({self.id}) {self.x}'
                f'/{self.y} - {self.__width}/{self.__height}')

    def update(self, *args, **kwargs):
        """Updates the class attributes."""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]
        if 'width' in kwargs.keys():
            self.__width = kwargs['width']
        if 'height' in kwargs.keys():
            self.__height = kwargs['height']
        if 'x' in kwargs.keys():
            self.__x = kwargs['x']
        if 'y' in kwargs.keys():
            self.__y = kwargs['y']
        if 'id' in kwargs.keys():
            self.id = kwargs['id']

    def to_dictionary(self):
        """Returns a dictionary representation of the instance."""
        return ({'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y, 'id': self.id})
