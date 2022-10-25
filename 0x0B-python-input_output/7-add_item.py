#!/usr/bin/python3
"""JSON Module"""


import sys

def argument(*argv):
    """Concatenates function arguments."""
    save_ = __import__('5-save_to_json_file').save_to_json_file
    load_ = __import__('6-load_from_json_file').load_from_json_file

    ls = load_("add_item.json")
    ln = len(sys.argv)
    for a in range(1, ln):
        if sys.argv[a] != "7-add_item.py":
            ls.append(sys.srgv[a])
        save_(ls, "add_item.json")
if __name__ == '__main__':
    argument()
