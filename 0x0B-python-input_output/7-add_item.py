#!/usr/bin/python3
"""JSON Module"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
l = []
arg = []
arg = *args
for a in arg:
    l.append(a)
save_to_json_file(l, "add_item.json")

