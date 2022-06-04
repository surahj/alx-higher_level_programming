#!/usr/bin/python3

import sys
sys.path.insert(0, '/alx/alx-higher_level_programming/0x03-python-data_structures')

max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
