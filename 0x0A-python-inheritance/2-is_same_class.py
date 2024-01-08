#!/usr/bin/python3
"""
A module that checks the class of an object
"""


def is_same_class(obj, a_class):
    """
    Compare the class of an object with a predefined class.
    """
    return type(obj) is a_class
