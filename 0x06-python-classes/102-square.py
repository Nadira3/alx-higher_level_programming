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
        self.__area = size ** 2

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
    @property
    def area(self):
        return self.__size ** 2
    @area.setter
    def area(self):
        self.__area = self.__size ** 2
    
    def  __eq__(self, other):
        if self.__area == other.__area:
            return True
        else:
            return False
    def  __ne__(self, other):
        if self.__area != other.__area:
            return True
        else:
            return False
    def  __lt__(self, other):
        if self.__area < other.__area:
            return True
        else:
            return False
    def  __gt__(self, other):
        if self.__area > other.__area:
            return True
        else:
            return False
    def  __le__(self, other):
        if self.__area <= other.__area:
            return True
        else:
            return False
    def  __ge__(self, other):
        if self.__area >= other.__area:
            return True
        else:
            return False
