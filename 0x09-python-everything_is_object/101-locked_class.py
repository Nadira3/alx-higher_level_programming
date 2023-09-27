#!/usr/bin/python3

""" LockedClass implementation """


class LockedClass:

    """ Regulates the names of attributes
        an instance initializes
    """

    def __setattr__(self, name, value):
        if name not in ["first_name", "dict"]:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)

    @property
    def dict(self):
        return {k:v for k,v in self.__dict__.items() if k == "first_name"}
