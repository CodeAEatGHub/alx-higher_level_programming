#!/usr/bin/python3
'''Rectangle module'''


class Rectangle:
    '''Rectangle class'''

    def __init__(self, width=0, height=0):
        '''Initializer.
        Args:
            width: Width of a rectangle.
            height: Height of a rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Property for the width of a rectangle.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width property.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Property for the height of a rectangle.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height property.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
