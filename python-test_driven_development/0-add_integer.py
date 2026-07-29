#!/usr/bin/python3
"""Module that adds two integers.

This module defines add_integer, which adds two numbers together,
casting floats to integers first, and validates that both
arguments are numeric.
"""


def add_integer(a, b=98):
    """Add two integers or floats (casted to integers).

    Args:
        a: first number, int or float.
        b: second number, int or float, defaults to 98.

    Returns:
        The integer sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
