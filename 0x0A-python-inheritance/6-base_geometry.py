#!/usr/bin/python3
"""
Check for inheritance
"""


class BaseGeometry(object):
    """
    A blueprint for base geometry
    """

    def __init__(self):
        """
        Initialize the base geometry
        """
        pass

    def area(self):
        """
        Just raise NotImplementedError()
        """
        raise Exception("area() is not implemented")
