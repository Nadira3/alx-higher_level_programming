#!/usr/bin/python3

"""
    rectangle module
"""

from models.base import Base

class Rectangle(Base):
    """
        inherits from Base
        defines a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getter function for width """

        return self.__width

    @width.setter
    def width(self, width):
        """ setter function for width """

        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """ getter function for height """

        return self.__height

    @height.setter
    def height(self, height):
        """ setter function for width """

        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """ getter function for variable x """

        return self.__x

    @x.setter
    def x(self, x):
        """ setter function for variable x """

        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """ getter function for variable y """

        return self.__y

    @x.setter
    def y(self, y):
        """ setter unction for variable x """

        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        return self.width * self.height

    def display(self):
        num = self.y
        for count in range(self.height + num):
            if num:
                print()
                num -= 1
                continue
            if (self.x):
                print(" " * self.x)
            print("#" * self.width)
    
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        if not args:
            for key, value in kwargs:
        else:
           attr = ['id', 'width', 'height', 'x', 'y']
           i = 0
           for arg in args:
               i += 1
