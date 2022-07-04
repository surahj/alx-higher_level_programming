#!/usr/bin/python3
""" checks for Exact same object """


def is_same_class(obj, a_class):
    """ return true if it is exact same object
        otherwise false
    """

    if type(obj) == a_class:
        return True

    return False
