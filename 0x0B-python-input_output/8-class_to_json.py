#!/usr/bin/python3

"""
    json dictionary module
"""


def class_to_json(obj):
    """
        converts a class object to json
    """

    return obj.__dict__
