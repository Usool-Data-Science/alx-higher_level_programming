#!/usr/bin/python3
"""
A module that checks the class of an object
"""


def is_same_class(obj, a_class):
    """
    Compare the class of an object with a predefined class.
    """
    if type(obj).__name__ == a_class:
        return True
    else:
        return False
