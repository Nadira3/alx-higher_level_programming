#!/usr/bin/python3

"""
    is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
        checks the type of an object

        Returns: True if the object is exactly an
        instance of the specified class;
        otherwise False
    """
    if not isinstance(a_class):
        return False
    return True
