#!/usr/bin/python3
""" Defines a dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    return a dictionary representation of an object
    """
    return obj.__dict__
