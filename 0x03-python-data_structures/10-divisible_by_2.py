#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) < 1:
        return None

    copy = my_list.copy()

    for i in range(len(my_list)):
        if (my_list[i] % 2) == 0:
            copy[i] = True

        else:
            copy[i] = False
    return copy
