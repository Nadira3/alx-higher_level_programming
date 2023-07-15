#!/usr/bin/python3

"""
    json dictionary module
"""


import json


def class_to_json(obj):
    """
        converts a class object to json
    """

    return json.loads(json.dumps(obj.__dict__))
