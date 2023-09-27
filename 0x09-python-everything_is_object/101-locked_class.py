#!/usr/bin/python3

""" LockedClass implementation """


class LockedClass:

    """ Regulates the names of attributes
        an instance initializes
    """

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name not in self.__dict__:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__getattr__(name)
