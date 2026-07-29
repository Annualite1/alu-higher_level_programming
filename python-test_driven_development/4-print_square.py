#!/usr/bin/python3
"""Module that prints a square using the character #."""


def print_square(size):
    """Print a square of size x size using the character #.

    Args:
        size: the length of the square's side, must be a
            non-negative integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
