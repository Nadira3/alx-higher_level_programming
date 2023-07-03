#!/usr/bin/python3

"""Square: defines a square"""


class Square:

    """
        Square: a class Square that defines a square

        size: to compute the area of the square
        many others
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position #initially had __ but didnt work

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2 or\
                not isinstance(position[0], int) or\
                not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
            end = "\n" if count != self.__size - 1 else ""
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end=end)
        print()
