#!/usr/bin/python3

class Square:
    """ A class to hold square objects. """
    __size = 0

    def __init__(self, size = 0):
        """ Initializes square objects. """
        self.size = size

    @property
    def size(self):
        """ Returns its value."""
        return (self.__size)

    @size.setter
    def size(self, size):
        """ A setter property for size."""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ Returns the area of the square."""
        return (self.__size * self.__size)
