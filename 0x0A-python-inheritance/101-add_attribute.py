#!/usr/bin/python3
"""
    module containing function
    typechecking __setattr__
"""


def add_attribute(obj, key, value):
    """
        __setattr__ with error typecheck
    """

    if obj.__class__.__name__ in ("float", "dict", "int", "str", "tuple", "list")\
            or hasattr(obj, "__slots__") and key not in obj.__class__.__slots__:
        raise TypeError("can't add new attribute")
    obj.__setattr__(key, value)
