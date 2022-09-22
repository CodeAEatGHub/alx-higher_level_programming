#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    result = 0
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if not sys.argv[2] in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        exit (1)
    if sys.argv[2] == '+':
        result = add(a, b)
    elif sys.argv[2] == '-':
        result = sub(a, b)
    elif sys.argv[2] == '*':
        result = mul(a, b)
    elif sys.argv[2] == '/':
        result = div(a, b)
    print('{} {} {} = {}'.format(a, sys.argv[2], b, result))
