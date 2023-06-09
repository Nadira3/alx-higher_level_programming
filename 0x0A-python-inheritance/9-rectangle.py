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
        BaseGeometry.__init__(self)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
