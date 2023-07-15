#!/usr/bin/python3

"""
    append_after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
        appends a line of text after the search string
    """

    file_string = ""
    with open(filename, "r+", encoding="utf-8") as f:
        for line in f:
            file_string += line
            if search_string in line:
                file_string += new_string
        f.seek(0)
        f.write(file_string)
