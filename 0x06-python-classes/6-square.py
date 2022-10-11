#!/usr/bin/python3

class Square:
    """A class to hold square objects. """
    __size = 0

    def __init__(self, size = 0, position=(0, 0)):
        """Initializes square objects. """
        self.size = size
        self.__position = position
    @property
    def size(self):
        """Returns its value."""
        return (self.__size)

    @property
    def position(self):
        """Returns the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if value is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
    @size.setter
    def size(self, size):
        """A setter property for size."""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a square."""
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        if self.__size == 0:
            print()
