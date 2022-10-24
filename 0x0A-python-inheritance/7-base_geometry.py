#!/usr/bin/python3
"""BaseGeometry module"""


import doctest


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Returns the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


doctest.testfile("tests/7-base_geometry.txt")
