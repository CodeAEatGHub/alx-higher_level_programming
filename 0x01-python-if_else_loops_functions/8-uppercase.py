#!/usr/bin/python3
def uppercase(str):
    upper_case = ''
    for letter in str:
        uni = ord(letter)
        if uni >= 97 and uni <= 122:
            upper_case += chr(uni - 32)
        elif uni >= 65 and uni <= 90:
            upper_case += chr(uni)
        else:
            upper_case += chr(uni)
    print('{}'.format(upper_case))
