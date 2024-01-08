#!/usr/bin/python3
"""
Checks for inheritance
"""


def inherits_from(obj, a_class):
    """
    A function that checks for inheritance.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
