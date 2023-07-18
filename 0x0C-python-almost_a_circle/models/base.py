#!/usr/bin/python3

"""
    Base module
"""


import json


class Base:
    """
        'base' of all other classes in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            returns the JSON string representation
            of list_dictionaries
        """

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        flist = ["Rectangle", "Square"]
        if list_objs is None:
            for arg in flist:
                file = arg + ".json"
            with open(file, "w", encoding="utf-8") as f:
                f.write(cls.to_json_string([]))
        else:
            for arg in list_objs:
                file = str(arg.__class__.__name__) + ".json"
            with open(file, "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
            returns the JSON string representation
            of list_dictionaries
        """

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
