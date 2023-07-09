#!/usr/bin/python3

"""
    print_square - prints a square
    with the character #
"""


def print_square(size):

    """
        print_square - prints a square

        Returns: None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
