#!/usr/bin/python3
"""Square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes new square instances."""
        Rectangle.__init__(self, size, size, x, y, id=None)

    def __str__(self):
        """Prints the string representation of the class."""
        return f'[{Square.__name__}]" "({self.id})
    {self.x}/{self.y} - {self.height}'

    @property
    def size(self):
        """Returns the value of size."""
        return self.width

    @size.setter
    def size(self, size):
        """Sets the size of an instance."""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates the Square instance."""
        b = ()
        if len(args) > 1:
            a = list(args)
            a.insert(2, args[1])
            b = tuple(a)
            Rectangle.update(b)
        Rectangle.update(args, kwargs)

    def to_dictionary(self):
        """Returns a dictionary representation of the instance."""
        return (self.__dict__)
