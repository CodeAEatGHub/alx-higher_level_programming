#!/usr/bin/python3
output = ''
for i in range(122, 96, -1):
    if i % 2:
        output += chr(i - 32)
    else:
        output += chr(i * 1)
print('{}'.format(output), end='')
