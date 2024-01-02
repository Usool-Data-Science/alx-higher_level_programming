#!/usr/bin/python3
"""
A square printer
It take an integer n
And print a square of length n
"""


def print_square(size):
    """
    Prints a # square of size "size".
    """
    if not(isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    for i in range(size):
        print("{}".format('#'*size), end='')
        print('')
