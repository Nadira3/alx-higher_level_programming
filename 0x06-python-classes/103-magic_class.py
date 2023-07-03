#!/usr/bin/python3
"""
    math: returns the mathematical constant
    of a circle, π
"""


class math:
    """
        math: returns the mathematical constant
        of a circle, π
    """
    def pi():
        return 3.141592653589793


"""
    MagicClass: finds the area and circumference
    of a circle
"""


class MagicClass:
    """
        MagicClass: finds the area and circumference
        of a circle
    """
    def __init__(self, radius=0):
        self.__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

    def area(self):
        return self.__radius ** 2 * math.pi()

    def circumference(self):
        return 2 * math.pi() * self.__radius
