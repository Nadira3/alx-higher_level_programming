#!/usr/bin/python3

"""
    write_file module
"""


def write_file(filename="", text=""):
    """
        writes a text file (UTF8)

        Returns: the number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
