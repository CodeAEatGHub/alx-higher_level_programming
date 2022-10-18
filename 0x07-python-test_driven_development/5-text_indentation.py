#!/usr/bin/python3
def text_indentation(text):
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    for i in text:
        if i not in [' ']:
            print(i, end='')
        if i in ['.', '?', ':']:
            print('\n', end='')
