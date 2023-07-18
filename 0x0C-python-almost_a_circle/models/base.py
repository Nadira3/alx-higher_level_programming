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
                result = []
                for arg in list_objs:
                    result.append(cls.to_dictionary(arg))
                f.write(cls.to_json_string(result))

    @staticmethod
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
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        if cls.__name__ == "Square":
            dummy = cls(3)
        dummy.update(dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        file = cls.__name__ + ".json"
        return json.load(file)
