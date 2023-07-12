#!/usr/bin/python3

"""
    inherits_from module
"""


def inherits_from(obj, a_class):
    """
        checks the type of an object

        Returns: True if the object inherits
        from the specified class;
        otherwise False
    """
    return issubclass(type(obj), a_class)
