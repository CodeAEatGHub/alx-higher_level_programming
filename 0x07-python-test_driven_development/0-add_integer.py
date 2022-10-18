#!/usr/bin/python3
""" Add integers """


def add_integer(a, b=98):
    """ Adds two integers or floats.
    >>> add_integer(2, 3)
    5
    """
    if type(a) != int or type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int or type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
if __name__ == "__main__":
    import doctest
        doctest.testfile("tests/0-add_integer.txt")
