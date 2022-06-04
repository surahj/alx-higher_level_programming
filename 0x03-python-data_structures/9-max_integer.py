#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    Max = 0
    for n in range(len(my_list) - 1):
        for i in range(len(my_list) - 1 - 1 - n):
            if my_list[i] > my_list[i + 1]:
                Max = my_list[i]

            else:
                Max = my_list[i + 1]
    return Max
