#!/usr/bin/python3
"""JSON Module"""


import sys

def argument(*argv):
    """Concatenates function arguments."""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    ls = []
    with open("add_item.json", 'r', encoding="utf-8") as f:
        check = f.read()
    if check != "":
        ls = load_from_json_file("add_item.json")
    ln = len(sys.argv)
    for a in range(1, ln):
        ls.append(sys.argv[a])
    save_to_json_file(ls, "add_item.json")
if __name__ == '__main__':
    argument()
