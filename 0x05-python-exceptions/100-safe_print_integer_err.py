#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print('{:d}'.format(value), end='')
        print()
        return (True)
    except (ValueError, TypeError) as ve:
        sys.stderr.write('Exception: ')
        print(ve, file=sys.stderr)
        return (False)
