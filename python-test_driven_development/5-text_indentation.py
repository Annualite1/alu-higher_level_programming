#!/usr/bin/python3
"""Module that prints text with indentation after ., ? and :."""


def text_indentation(text):
    """Print text with two new lines after each ., ? and : character.

    Args:
        text: the string to print, must be a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i], end="\n\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1
