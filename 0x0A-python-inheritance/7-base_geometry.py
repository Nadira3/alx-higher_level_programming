#!/usr/bin/python3

"""
    BaseGeometry module
"""


class BaseGeometry:
    """
        BaseGeometry
    """

    def area(self):
        """
            area - finds area
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            integer_validator - validates value
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
        return value
