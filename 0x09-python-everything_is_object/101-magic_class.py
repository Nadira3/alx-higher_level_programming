#!/usr/bin/python3

"""
    magic_class: creates a magic string
"""


class magic_class:
    """
        magic_class: returns a string “BestSchool”
    """
    count = 0

    def __init__(self):
        magic_class.increment_count()

    @classmethod
    def increment_count(cls):
        cls.count += 1

    def __str__(cls):
        if cls.count < 2:
            return "BestSchool"
        else:
            result = ""
            for i in range(cls.count):
                result += "BestSchool"
                if i < cls.count - 1:
                    result += ", "
            return result


def magic_string():
    string = magic_class()
    return string
