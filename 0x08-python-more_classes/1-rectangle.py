#!/usr/bin/python3

"""Rectangle: defines a rectangle"""


class Rectangle:

    """
        Rectangle: a class Rectangle that defines a square

        width: defines a width
        height: defines a height
    """

    def __init__(self, width=0, height=0):
        self.size = width
        self.height = height

    """ getter for width """
    @property
    def width(self):
        return self.__width
    
    """ setter for width """
    @width.setter
    def width(self, value):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    """ getter for height """
    @property
    def height(self):
        return self.__height

    """ setter for height """
    def height(self, value):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value