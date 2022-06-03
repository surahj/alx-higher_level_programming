#!/usr/bin/python3
import sys

sys.path.insert(0, '/alx/alx-higher_level_programming/0x03-python-data_structures')

element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
