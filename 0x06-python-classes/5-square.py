#!/usr/bin/python3

"""Square: defines a square"""


class Square:

    """
        Square: a class Square that defines a square

        size: to compute the area of the square
        many others
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """
        area: computes the area of a square

        Return: area of a square of size 'size'
    """
    def area(self):
        return self.__size ** 2

    """
        my_print: prints a square
    """
    def my_print(self):
        for count in range(self.__size):
            print("#" * self.__size)
        print()
