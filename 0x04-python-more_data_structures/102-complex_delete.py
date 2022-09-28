#!/usr/bin/python3
def complex_delete(my_dict, value):
    key_list = []
    for key, key_value in my_dict.items():
        if key_value is value:
            key_list.append(key)
    for i in key_list:
        del my_dict[i]
    return(my_dict)
