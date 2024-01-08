#!/usr/bin/python3
"""
Checking the ancestor of a class
"""


def is_kind_of_class(obj, a_class):
    """
    A function to check lineage of a class
    """
    return (isinstance(obj, a_class) or type(obj) is a_class)
