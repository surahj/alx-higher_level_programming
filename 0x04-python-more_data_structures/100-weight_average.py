#!/usr/bin/python3

def weight_average(my_list=[]):
    tuple_sum = 0
    weight_sum = 0

    if len(my_list) == 0:
        return (0)

    for number in my_list:
        tuple_sum += (number[0] * number[1])
        weight_sum += (number[1])

    average = tuple_sum / weight_sum

    return (average)
