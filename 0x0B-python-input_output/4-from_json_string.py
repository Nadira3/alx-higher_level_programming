#!/usr/bin/python3

"""
    json_loads to string module
"""


import json


def from_json_string(my_str):
    """
        Returns: the object of a JSON representation
    """

    return json.loads(my_str)
