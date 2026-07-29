#!/usr/bin/python3
"""Module that prints a person's full name."""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first name> <last name>'.

    Args:
        first_name: the first name, must be a string.
        last_name: the last name, must be a string, defaults to "".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
