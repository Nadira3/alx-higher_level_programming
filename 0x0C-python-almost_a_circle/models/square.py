#!/usr/bin/python3

"""
    square module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        inherits from class rectangle and
        defines a square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ print implementation in class """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
