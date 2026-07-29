#!/usr/bin/python3
"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix: list of lists of integers or floats.
        div: number to divide by.

    Returns:
        A new matrix with all elements divided by div.
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err)
        for n in row:
            if not isinstance(n, (int, float)) or isinstance(n, bool):
                raise TypeError(err)
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
