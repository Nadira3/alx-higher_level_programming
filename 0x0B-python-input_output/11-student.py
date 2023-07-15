#!/usr/bin/python3

"""
    json dictionary module
"""


class Student:
    """
        creates a student instance
    """

    def __init__(self, first_name, last_name, age):
        """
            initializes the class Student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            converts a class object to json
        """

        if attrs:
            return {attr: value for attr, value in
                    self.__dict__.items() if attr in attrs}
        return self.__dict__ if attrs is None or len(attrs) else {}

    def reload_from_json(self, json):
        """
            retrieves a dictionary representation
            of a Student instance
        """

        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
