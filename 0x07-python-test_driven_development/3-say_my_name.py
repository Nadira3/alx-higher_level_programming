#!/usr/bin/python3

"""
    say_my_name - prints a sentence
"""

def say_my_name(first_name, last_name=""):

    """
        say_my_name - prints
        My name is <first name> <last name>

        Returns: a sentence
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
