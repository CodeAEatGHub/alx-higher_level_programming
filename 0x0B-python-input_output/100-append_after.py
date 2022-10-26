#!/usr/bin/python3
"""JSON module"""

def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file."""
    contents = []
    index = 0
    with open(filename, 'r', encoding="utf-8") as f:
        contents = f.readlines()
    for i in contents:
        if search_string in i:
            contents.insert(index + 1, new_string)
        index = index + 1
    with open(filename, 'w', encoding="utf-8") as f:
        contents = "".join(contents)
        f.write(contents)



