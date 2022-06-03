#!/usr/bin/python3
import sys
sys.path.insert(0, '/alx/alx-higher_level_programming/0x03-python-data_structures')

print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
