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
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file = cls.__name__ + ".json"
        with open(file, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                f.write(cls.to_json_string(list_objs))

    def from_json_string(json_string):
        """
            returns the JSON string representation
            of list_dictionaries
        """

        if not json_string:
            return json.loads("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(3, 1, 1)
        return dummy.update(dictionary)

    @classmethod
    def load_from_file(cls):
        file = cls.__name__ + ".json"
        return json.load(file)