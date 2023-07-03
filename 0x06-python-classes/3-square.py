#!/usr/bin/python3

"""Square: defines a square"""


class Square:

    """
        Square: a class Square that defines a square

        size: to compute the area of the square
        many others
    """

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size ** 2
