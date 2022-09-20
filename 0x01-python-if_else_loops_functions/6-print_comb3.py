#!/usr/bin/python3
for num in range(0, 100):
    i = num / 10
    j = num % 10
    if num == 89:
        print('{:d}'.format(num))
    elif i < j:
        print('{:02d}'.format(num), end=", ")
