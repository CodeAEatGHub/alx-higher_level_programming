#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if not my_string[i] == 'c':
            if not my_string[i] == 'C':
                print('{}'.format(my_string[i]), end='')
    print()
