#!/usr/bin/python3

"""Rectangle: defines a rectangle"""


class Rectangle:

    """
        Rectangle: a class Rectangle that defines a square

        width: defines a width
        height: defines a height
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter for width """

        return self.__width

    @width.setter
    def width(self, width):
        """ setter for width """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """ getter for height """

        return self.__height

    @height.setter
    def height(self, height):
        """ setter for height """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        for height in range(self.__height):
            end = "" if height == self.__height - 1 else "\n"
            print("#" * self.__width, end=end)
        return ""

    def __repr__(self):
        result = str(self.__class__)[-11:-2] + "("
        if self.__width:
            result += str(self.__width)
        if self.__height:
            if self.__width:
                result += ", "
            result += str(self.__height)
        return result + ")"
#        return f"Rectangle({self.__width}, {self.__height})"
