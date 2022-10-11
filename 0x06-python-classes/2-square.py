#!/usr/bin/python3

class Square:
    """ A class to hold square objects. """
    __size = 0

    def __init__(self, size = 0):
        """ Initializes square objects. """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
