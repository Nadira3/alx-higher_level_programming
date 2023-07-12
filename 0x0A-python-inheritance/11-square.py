#!/usr/bin/python3

"""
    Square module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        inherits attributes from BaseGeometry
    """

    def __init__(self, size):
        """
            init method for Rectangle class
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
