#!/usr/bin/python3

"""
    Int Inheritance module
"""


class MyInt(int):
    """
        MyInt has == and != operators inverted
    """

    def __init__(self, value):
        super().__init__()
        self.value = value

    def __eq__(self, other):
        return self.value != other

    def __ne__(self, other):
        return self.value == other
