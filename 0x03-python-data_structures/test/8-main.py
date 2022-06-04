#!/usr/bin/python3

import sys
sys.path.insert(0, '/alx/alx-higher_level_programming/0x03-python-data_structures')

multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
