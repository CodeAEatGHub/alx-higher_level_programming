#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    ic = 0
    jc = 0
    for i in my_list:
        sum = sum + i
        for j in my_list:
            if j == i and ic < jc:
                sum = sum - i
                jc = 0
                break;
            jc = jc + 1
        ic = ic + 1
        jc = 0
    return sum
