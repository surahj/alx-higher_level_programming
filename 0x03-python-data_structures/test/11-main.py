#!/usr/bin/python3

import sys
sys.path.insert(0, '/alx/alx-higher_level_programming/0x03-python-data_structures')

delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
