#!/usr/bin/python3

"""
    returns the list of available attributes
    and methods of an object
"""

def lookup(obj):
    """
        lookup - finds the list of attributes
        of an object

        Returns: dir content
    """

    return list(obj.__dict__)
