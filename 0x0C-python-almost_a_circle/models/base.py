#!/usr/bin/python3

"""
    Base module
"""


import json
import csv
import io


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
            dum = cls(3, 1)
        elif cls.__name__ == "Square":
            dum = cls(3)
        else:
            dum = None
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        file = cls.__name__ + ".json"
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            return []

        pystring = cls.from_json_string(content)
        return [cls.create(**instance) for instance in pystring]

    @staticmethod
    def to_csv_string(list_file):
        """
            returns the CSV string representation
            of list_dictionaries
        """

    @staticmethod
    def to_csv_string(list_dictionaries):
        """
            Returns the CSV string representation of list_dictionaries.
        """
        if not list_dictionaries:
            return ""

        csv_buffer = io.StringIO()
        fieldnames = list_dictionaries[0].keys()
        csv_writer = csv.writer(csv_buffer)
        csv_writer.writerow(fieldnames)

        for dictionary in list_dictionaries:
            csv_writer.writerow(dictionary.values())

        csv_string = csv_buffer.getvalue()
        return csv_string

    @staticmethod
    def from_csv_string(csv_string):
        """
            returns the JSON string representation
            of list_dictionaries
        """

        if not csv_string:
            return []
        csv_buffer = io.StringIO(csv_string)
        csv_reader = csv.DictReader(csv_buffer)
        list_dictionaries = [row for row in csv_reader]
        return list_dictionaries

    @classmethod
    def save_to_file_csv(cls, list_objs):
        file = cls.__name__ + ".csv"
        with open(file, "w", encoding="utf-8") as f:
            result = []
            if list_objs is None:
                f.write(cls.to_csv_string([]))
            else:
                for arg in list_objs:
                    result.append(cls.to_dictionary(arg))
                f.write(cls.to_csv_string(result))
            return result

    @classmethod
    def load_from_file_csv(cls):
        file = cls.__name__ + ".csv"
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
                list_dict = cls.from_csv_string(content)
                for dic in list_dict:
                    for key, value in dic.items():
                        dic[key] = int(value)
            return [cls.create(**instance) for instance in list_dict]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        ...
