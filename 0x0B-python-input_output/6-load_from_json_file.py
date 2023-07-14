#!/usr/bin/python3

"""
    json_loads to string module
"""


import json


def load_from_json_file(filename):
    """
        Returns: the object of a JSON representation
    """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
