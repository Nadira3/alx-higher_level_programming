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
