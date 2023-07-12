#!/usr/bin/python3

"""
    is_same_class module
"""


def is_same_class(obj, a_class):
    """
        checks the type of an object

        Returns: True if the object is exactly an
        instance of the specified class;
        otherwise False
    """
    if type(obj) is not a_class:
        return False
    return True
