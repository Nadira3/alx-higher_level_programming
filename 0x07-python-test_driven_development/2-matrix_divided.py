#!/usr/bin/python3

"""
    matrix_divided - divides all elements of
    a matrix
"""


def matrix_divided(matrix, div):

    """
        divides elements of a matrix

        Returns: a new matrix
    """
    var = matrix
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(var, list) or \
            any(not isinstance(li, list) for li in var) \
            or any(not isinstance(n, (int, float)) for li in var for n in li):
        raise TypeError(err)
    if any(len(matrix[0]) != len(li) for li in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in li] for li in matrix]
