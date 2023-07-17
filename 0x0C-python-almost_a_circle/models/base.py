#!/usr/bin/python3

"""
    Base module
"""


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
