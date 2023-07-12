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
        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
        return value


class Rectangle(BaseGeometry):
    """
        inherits attributes from BaseGeometry
    """

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
