#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    exc = 0
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        exc = 1
        return None
    except ValueError:
        exc = 1
        return None
    finally:
        if not exc:
            print('Inside result:{}'.format(c))
        else:
            print('Inside result: None')
