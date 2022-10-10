#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    res = 0
    new_list = []
    if len(my_list_1) > len(my_list_2):
        k = len(my_list_1)
    else:
        k = len(my_list_2)
    for i in range(k):
        try:
            res = my_list_1[i] / my_list_2[i]
            new_list.append(res)
            i = i + 1
            if i == list_length:
                break
        except IndexError:
            print('out of range')
            new_list.append(0)
            pass
        except TypeError:
            print('wrong type')
            new_list.append(0)
            pass
        except ZeroDivisionError:
            print('division by 0')
            new_list.append(0)
            pass
        finally:
            pass
    return (new_list)
