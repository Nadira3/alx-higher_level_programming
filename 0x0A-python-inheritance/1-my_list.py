#!/usr/bin/python3

"""
    inherits attributes from a class
"""


class MyList(list):

    """
        inherits attributes from a class
    """

    class_list = []

    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        """
            prints a sorted list
        """
        new_list = self.copy()
        print(sorted(new_list))
