#!/usr/bin/python3
"""JSON module"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    with open(filename, 'r', encoding="utf-8") as f:
        r = f.read()
        return (json.loads(r))
