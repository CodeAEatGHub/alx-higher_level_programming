#!/usr/bin/python3
"""Square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes new square instances."""
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """Prints the string representation of the class."""
        return (f'[{Square.__name__}] ({self.id})'
                f' {self.x}/{self.y} - {self.height}')

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
        if len(args) == 1 and len(kwargs) == 0:
            Rectangle.update(self, *args)
        if len(args) > 1 and len(kwargs) == 0:
            a = list(args)
            a.insert(2, args[1])
            b = tuple(a)
            Rectangle.update(self, *a)
        if len(kwargs) > 0 and 'size' in kwargs.keys():
            kwargs['width'] = kwargs['size']
            kwargs['height'] = kwargs['size']
            Rectangle.update(self, **kwargs)
        if len(kwargs) > 0:
            Rectangle.update(self, **kwargs)

    def to_dictionary(self):
        """Returns a dictionary representation of the instance."""
        return (self.__dict__)
