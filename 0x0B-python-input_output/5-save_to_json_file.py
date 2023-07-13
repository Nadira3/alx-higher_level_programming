#!/usr/bin/python3

"""
    write_json_to_file module
"""


import json


def save_to_json_file(my_obj, filename):
    """
        writes a text file (UTF8)

        Returns: the number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
