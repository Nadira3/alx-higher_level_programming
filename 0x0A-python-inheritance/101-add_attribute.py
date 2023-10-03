#!/usr/bin/python3
"""
    module containing function
    typechecking __setattr__
"""


def add_attribute(obj, key, value):
    """
        __setattr__ with error typecheck
    """

    if not isinstance(obj, object) or key not in obj.__slots__:
        raise TypeError("can't add new attribute")
    else:
        obj.__setattr__(key, value)
