#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) - 1 == 1:
        print('1 argument:')
    elif len(sys.argv) > 1:
        print('{} arguments:'.format(len(sys.argv) - 1))
    for i in range(len(sys.argv)):
        if i > 0:
            print('{}: {}'.format(i, sys.argv[i]))
