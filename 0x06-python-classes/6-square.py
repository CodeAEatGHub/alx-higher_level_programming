#!/usr/bin/python3

"""Square module"""


class Square:
    """Square class"""

    def __str__(self):
        self.my_print()

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square instance
        Args:
            size: Length of the square.
            position: Position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property for the length of a square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Property for the position of a square.
        Raises:
            TypeError: If value is not tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
         len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Returns the area of a square.
        """
        return self.__size ** 2

    def my_square_print(self):
        """Returns a square for printing."""
        ret = ""
        if not self.size:
            return "\n"

        for i in range(self.position[1]):
                ret += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                ret += " "
            for j in range(self.size):
                ret += "#"
            ret += "\n"
        return ret

    def my_print(self):
        """Prints a square."""
        print(self.my_square_print(), end="")
