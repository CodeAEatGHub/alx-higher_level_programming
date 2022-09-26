#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
<<<<<<< HEAD
    if my_list is None:
        pass
    else:
        for rev in my_list[::-1]:
            print('{:d}'.format(rev))
=======
    my_list.reverse()
    for i in range(len(my_list)):
        print('{}'.format(my_list[i]))
<<<<<<< HEAD
    my_list.reverse()        
=======
    my_list.reverse()
>>>>>>> dd163bc92c38a23598067873ece7b7ad4f249c0e
>>>>>>> f0e37b5cb2f0a54f5892bd9d1676f371f51203a5
