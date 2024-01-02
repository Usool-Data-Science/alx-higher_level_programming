#!/usr/bin/python3
"""
A divisor function that returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    Divides each subelement of matrix by div
    """
    if not (
            isinstance(matrix, list) and
            all([isinstance(x, list) for x in matrix]) and
            all([isinstance(x, int) for row in matrix for x in row])):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for ind, mat in enumerate(matrix):
        if (ind > 0 and len(mat) != len(matrix[ind - 1])):
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
