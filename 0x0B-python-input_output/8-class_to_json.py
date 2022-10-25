#!/usr/bin/python3
"""JSON module"""


def class_to_json(obj):
    """Return the dicitionary description of an object."""
    return (obj.__dict__)
