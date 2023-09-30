#!/usr/bin/python3

def add_attribute(obj, key, value):
    if isinstance(obj, (float, int, str, list, dict, tuple)):
        raise TypeError("can't add new attribute")
    else:
        obj.__setattr__(key, value)
