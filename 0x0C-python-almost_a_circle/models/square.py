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

    @property
    def size(self):
        """ getter function for size """

        return self.width

    @size.setter
    def size(self, size):
        """ setter function for size """

        if type(size) is not int:
            raise TypeError("width must be an integer")

        if size <= 0:
            raise ValueError("width must be > 0")

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ updates an object instance attributes """

        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            attr = ['id', 'size', 'x', 'y']
            i = 0
            for arg in args:
                setattr(self, attr[i], arg)
                i += 1
