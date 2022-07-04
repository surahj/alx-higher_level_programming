#!/usr/bin/python3
""" checks for Exact same object """


def is_kind_of_class(obj, a_class):
    """ return true if it is exact same object
        otherwise false
    """

    if (isinstance(obj, a_class)):
        return True

    return False
