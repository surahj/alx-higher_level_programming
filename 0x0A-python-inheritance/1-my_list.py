#!/usr/bin/python3
""" Defines a class MyList that inherits from list"""


class MyList(list):
    """ inherit from built in list
    """
    def print_sorted(self):
        print(sorted(self))
