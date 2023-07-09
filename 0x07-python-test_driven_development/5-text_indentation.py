#!/usr/bin/python3

"""
    text_indentation - indents a stream of text
"""


def text_indentation(text):

    """
        text_indentation - prints a text with 2
        new lines after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delim = ['?', '.', ':']

    for idx in range(len(text)):
        if text[idx] == ' ':
            if text[idx - 1] in delim or text[idx - 1] == ' ':
                continue
        print(text[idx], end="")
        if text[idx] in delim:
            print("\n")
