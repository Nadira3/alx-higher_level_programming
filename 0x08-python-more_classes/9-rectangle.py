#!/usr/bin/python3

"""Rectangle: defines a rectangle"""


class Rectangle:

    """
        Rectangle: a class Rectangle that defines a square

        width: defines a width
        height: defines a height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        self.increment_instance()

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
        if self.print_symbol:
            return self.instprint()
        else:
            return self.classprint(self.__width, self.__height)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        self.decrement_instance()

    @classmethod
    def increment_instance(cls):
        cls.number_of_instances += 1

    @classmethod
    def decrement_instance(cls):
        cls.number_of_instances -= 1

    @classmethod
    def classprint(cls, width, height):
        result = ""
        for h in range(height):
            end = "" if h == height - 1 else "\n"
            result += (str(cls.print_symbol) * width)
            result += end
        return result

    def instprint(self):
        result = ""
        for h in range(self.__height):
            end = "" if h == self.__height - 1 else "\n"
            result += (str(self.print_symbol) * self.__width)
            result += end
        return result

    def __ge__(self, other):
        if self.area() > other.area() or\
                self.area() == other.area():
            return self
        return other

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 >= rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size) 
