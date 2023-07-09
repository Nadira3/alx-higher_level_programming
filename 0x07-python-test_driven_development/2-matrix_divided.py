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

    if not isinstance(matrix, list) or any(not isinstance(li, list) for li in matrix) or any(not isinstance(num, (int, float)) for li in matrix for num in li):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(matrix[0]) != len(li) for li in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in li] for li in matrix]
