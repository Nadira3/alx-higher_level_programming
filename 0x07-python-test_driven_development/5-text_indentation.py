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

    for idx in range(len(text)):
        if text[idx] == ' ' and text[idx - 1] in\
                ['?', '.', ':']:
            continue
        print(text[idx], end="")
        if text[idx] in ['?', '.', ':']:
            print("\n")
